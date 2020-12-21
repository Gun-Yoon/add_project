"""
   제안하는 방법 알고리즘
"""

from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from fcmeans import FCM
import numpy as np
import collections
import pandas as pd
from scipy.spatial import distance

def scoring(df):
    accuracy = accuracy_score(df['actual'], df['predict'])
    Precision = precision_score(df['actual'], df['predict'], average=None)
    Recall = recall_score(df['actual'], df['predict'], average=None)
    F1 = f1_score(df['actual'], df['predict'], average=None)
    score_list = [accuracy,F1,Precision,Recall]
    return score_list

def check_different(df):
    dif_indexes = df[(df['actual'] != df['predict']) == True]
    return dif_indexes

def check_match(df):
    dif_indexes = df[(df['actual'] == df['predict']) == True]
    return dif_indexes

# Some variables
NUM_CLUSTERS = 2
NUM_ITER = 500

name_list = ['normal','probe','r2l','u2r','dos']
for name in name_list:
    print("\n데이터 호출")
    train_data = pd.read_csv('dataset/pre_train.csv')
    train_data = train_data[(train_data['Label'] == name) == True]
    train_data = train_data.drop(['Label'], axis=1)

    test_data = pd.read_csv('dataset/misuse_result/'+name+'.csv')
    label = test_data['actual']
    data = test_data.drop(['actual','predict'],axis=1)

    std_scaler = StandardScaler()
    fitted = std_scaler.fit(data)
    X = std_scaler.transform(data)
    x_add = std_scaler.transform(train_data)

    x_train, x_test, y_train, y_test = train_test_split(X,label, test_size=0.2, random_state=42)
    x_train = np.append(x_train, x_add,axis=0)

    #k-means 학습 수행
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1, n_init=1)
    km.fit(x_train)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    print("\nInitial centroid 찾기")
    for iter in range(NUM_ITER):
      km = KMeans(n_clusters=NUM_CLUSTERS, init=cents, max_iter=1, n_init=1)
      km.fit(x_train)
      cc = km.cluster_centers_.tolist()
      #print('Centroids:', cc)
      inertia = km.inertia_
      cents = km.cluster_centers_

      cents_list.append(cents)
      inert_list.append(inertia)

    # Get best centroids to use for full clustering
    best_cents = cents_list[inert_list.index(min(inert_list))]

    # fit the fuzzy-c-means
    fcm = FCM(n_clusters=NUM_CLUSTERS, first_center=best_cents, max_iter=500, random_state=42)
    fcm.fit(x_train)
    probability = fcm.predict(x_test)
    probability_df = pd.DataFrame(data=probability[:,2], columns=['predict'])
    cluster = collections.Counter(probability[:,2])
    print(cluster)
    if cluster[0.0] >= cluster[1.0]:
        probability_df.loc[probability_df['predict'] == 0.0,'predict'] = name
        probability_df.loc[probability_df['predict'] == 1.0, 'predict'] = 'outlier'
    else:
        probability_df.loc[probability_df['predict'] == 1.0,'predict'] = name
        probability_df.loc[probability_df['predict'] == 0.0, 'predict'] = 'outlier'

    result_df = pd.DataFrame(data=x_test, columns=data.columns)
    result_df['actual'] = test_data['actual'][y_test.index].tolist()
    result_df['predict'] = probability_df['predict']
    result_df['0'] = probability[:,0]
    # fcm 결과 나옴

    print("\nValidate records in cluster(find invalid record)")
    dif_data = check_different(result_df)
    print(dif_data.shape)

    # probability threshold(pt)를 기준으로 부합한 데이터 추출
    # 0.4 <= pt <= 0.6
    dif_df = dif_data
    print("\nCheck probability threshold : 0.4<=Threshold<=0.6")
    for i in dif_df.index:
        if dif_df.loc[i][17] <= 0.4 or dif_df.loc[i][17] >= 0.6:
            dif_df = dif_df.drop([i])
    print(dif_df.shape)

    print("\nSave invalid cluster")
    invalid_data = dif_df
    print(invalid_data.shape)

    print("\nCheck correct record")
    corr_df = check_match(result_df)
    df_benign = corr_df[(corr_df['actual'] == name) == True]
    df_attack = corr_df[(corr_df['actual'] != name) == True]

    test_data = pd.read_csv('dataset/misuse_result/' + name + '.csv')
    test_data = test_data.drop(['actual','predict'],axis=1)
    benign_data = test_data.loc[df_benign.index.values]
    attack_data = test_data.loc[df_attack.index.values]
    benign_data.to_csv('dataset/improve/df_benign.csv', index=False)
    attack_data.to_csv('dataset/improve/df_attack.csv', index=False)

    benign_raw = pd.read_csv("dataset/improve/df_benign.csv")
    attack_raw = pd.read_csv("dataset/improve/df_attack.csv")
    standard_data = pd.concat([benign_raw, attack_raw], axis=0)
    centroid = fcm.centers.tolist()

    std_scaler = StandardScaler()
    fitted = std_scaler.fit(standard_data)
    benign_data = pd.DataFrame(data=std_scaler.transform(benign_raw), columns=benign_raw.columns)
    attack_data = pd.DataFrame(data=std_scaler.transform(attack_raw), columns=attack_raw.columns)
    centroid = list(std_scaler.transform(centroid))

    benign_distance = pd.DataFrame(index=range(0, len(benign_data)), columns=['distance'])
    attack_distance = pd.DataFrame(index=range(0, len(attack_data)), columns=['distance'])

    print("\n정상/악성 각각의 벡터에 대한 유클리드 거리 측정")
    for i in range(len(benign_data)):
        benign_distance.loc[i] = distance.cityblock(benign_data.loc[i], centroid[0])

    for i in range(len(attack_data)):
        attack_distance.loc[i] = distance.cityblock(attack_data.loc[i], centroid[0])

    print("\n유클리드 거리 기반 평균 및 표준편차 계산")
    benign_arr = benign_distance.to_numpy()
    attack_arr = attack_distance.to_numpy()

    benign_mean = np.mean(benign_arr)  # 평균
    benign_std = np.std(benign_arr)  # 표준편차
    attack_mean = np.mean(attack_arr)  # 평균
    attack_std = np.std(attack_arr)  # 표준편차

    print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean, benign_std, attack_mean,
                                                                          attack_std))

    print("\n클러스터 결정경계에 위치되어 있는 데이터 추출")

    print("정상 클러스터 결정 경계 데이터 셋")
    benign_bounderies_index = benign_distance[(benign_distance['distance'] >= (benign_mean + benign_std)) == True]
    benign_bounderies = benign_raw.loc[benign_bounderies_index.index.values]
    print(benign_bounderies.shape)

    print("\n위협 클러스터 결정 경계 데이터 셋")
    attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean + attack_std)) == True]
    attack_bounderies = attack_raw.loc[attack_bounderies_index.index.values]
    print(attack_bounderies.shape)

    benign_bounderies = benign_bounderies
    attack_bounderies = attack_bounderies

    standard_data = pd.concat([benign_bounderies, attack_bounderies], axis=0)
    std_scaler = StandardScaler()
    fitted = std_scaler.fit(standard_data)
    benign_bounderies = pd.DataFrame(data=std_scaler.transform(benign_bounderies),
                                     columns=benign_bounderies.columns)
    attack_bounderies = pd.DataFrame(data=std_scaler.transform(attack_bounderies),
                                     columns=attack_bounderies.columns)
    diff_data = pd.DataFrame(data=std_scaler.transform(invalid_data), columns=invalid_data.columns)

    benign_distance = pd.DataFrame(index=range(0, len(benign_bounderies)), columns=['distance'])
    attack_distance = pd.DataFrame(index=range(0, len(attack_bounderies)), columns=['distance'])
    dif_prelist = []

    print("\nEuclidean distance measure between benign/attack boundaries and invalid data")
    for j in range(len(diff_data)):
        for i in range(len(benign_bounderies)):
            benign_distance.loc[i] = distance.cityblock(benign_bounderies.loc[i], diff_data.loc[j])

        for i in range(len(attack_bounderies)):
            attack_distance.loc[i] = distance.cityblock(attack_bounderies.loc[i], diff_data.loc[j])

        if benign_distance['distance'].min() > attack_distance['distance'].min():
            dif_prelist.append('outlier')
        else:
            dif_prelist.append(name)

    pt_df = pd.DataFrame(data=dif_prelist, columns=['predict'])
    pt_df['actual'] = invalid_data['actual'].tolist()
    pt_df.to_csv('dataset/improve/test.csv')