from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from fcmeans import FCM
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt
from scipy.spatial import distance

def scoring(df):
   tn, fp, fn, tp = confusion_matrix(df['actual'], df['predict']).ravel()
   accuracy = accuracy_score(df['actual'], df['predict'])
   Precision = precision_score(df['actual'], df['predict'], average=None)
   Precision = sum(Precision) / 2
   Recall = recall_score(df['actual'], df['predict'], average=None)
   Recall = sum(Recall) / 2
   F1 = f1_score(df['actual'], df['predict'], average=None)
   F1 = sum(F1) / 2
   score_list = [accuracy,Precision,Recall,F1,tn,fp,fn,tp]
   return score_list

def check_different(df):
  dif_indexes = df[(df['actual'] != df['predict']) == True]
  true_indexes = df[(df['actual'] == df['predict']) == True]
  return dif_indexes, true_indexes

def roc(name,list):
    # calculate scores
    roc_score_list = []
    for i in range(len(name)):
        temp_auc = roc_auc_score(list[i]['actual'], list[i]['predict'])
        print(name[i]+'ROC AUC=%.3f' %(temp_auc))
        roc_score_list.append(temp_auc)

    # calculate roc curves
    for i in range(len(name)):
        temp_fpr, temp_tpr, _ = roc_curve(list[i]['actual'], list[i]['predict'])
        plt.plot(temp_fpr, temp_tpr, label=name[i])

    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    # show the legend
    plt.legend()

    # show the plot
    plt.show()

def centroid(X_train, NUM_CLUSTERS):
    # k-means 학습 수행
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1, n_init=1)
    km.fit(X_train)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    print("\nInitial centroid 찾기")
    for iter in range(100):
        km = KMeans(n_clusters=NUM_CLUSTERS, init=cents, max_iter=10, n_init=1)
        km.fit(X_train)
        inertia = km.inertia_
        cents = km.cluster_centers_

        cents_list.append(cents)
        inert_list.append(inertia)

    # Get best centroids to use for full clustering
    best_cents = cents_list[inert_list.index(min(inert_list))]
    return best_cents.tolist()

# Some variables
NUM_CLUSTERS = 2
mal_list = ['Bot','DDOS attack-HOIC','DDOS attack-LOIC-UDP','DDoS attacks-LOIC-HTTP','DoS attacks-GoldenEye',
            'DoS attacks-Hulk','DoS attacks-Slowloris','FTP-BruteForce','Infilteration','SSH-Bruteforce']
mal_result = pd.DataFrame(index=range(0,len(mal_list)),columns=['accuracy','Precision','Recall','F1','tn','fp','fn','tp'],)

for mal_num in range(len(mal_list)):
    print("\n데이터 호출")
    data = pd.read_csv("F:/data/ADD/201210/"+mal_list[mal_num]+".csv")


    y = data['Label']
    le = LabelEncoder().fit(y)
    print("Class to number : ",le.classes_)
    y = le.transform(y)

    X = data.drop(['Label'], axis=1)
    col = X.columns
    X = X.to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    centers = centroid(X_train, NUM_CLUSTERS)
    centers_arr = np.array(centers)

    fcm = FCM(n_clusters=2, first_center=centers, max_iter=100, random_state=42)
    fcm.fit(X_train)
    probability = fcm.predict(X_test)
    probability = np.array(probability)
    fcm_df = pd.DataFrame(data=probability, columns=[0,1,'predict'])
    fcm_df['actual'] = y_test

    print("\nScoring")
    print('Accuracy : %0.4f'%accuracy_score(fcm_df['actual'], fcm_df['predict']))
    Precision = precision_score(fcm_df['actual'], fcm_df['predict'], average=None)
    Precision = sum(Precision)/2
    print('Precision : %0.4f'%Precision)
    Recall = recall_score(fcm_df['actual'], fcm_df['predict'], average=None)
    Recall = sum(Recall)/2
    print('Recall : %0.4f'%Recall)
    F1 = f1_score(fcm_df['actual'], fcm_df['predict'], average=None)
    F1 = sum(F1)/2
    print('F1-score : %0.4f'%F1)

    print("\nValidate records in cluster(find invalid record)")
    dif_df, true_df = check_different(fcm_df)
    dif_data = dif_df

    print("\nprobability threshold(pt)를 기준으로 부합한 데이터 추출(0.46 < Threshold < 0.54)")
    wrong_index = []
    for i in dif_df.index:
        if dif_df.loc[i][0] <= 0.46 or dif_df.loc[i][0] >= 0.54:
            wrong_index.append(i)
            dif_df = dif_df.drop([i])

    print("\nSave invalid cluster")
    X_test_df = pd.DataFrame(data=X_test, columns=col)
    pt_data = X_test_df.loc[dif_df.index.values]
    X_test_df_label = pd.DataFrame(data=y_test, columns=['actual'])
    pt_data_label = X_test_df_label.loc[dif_df.index.values]

    print("\nCheck correct record")
    df_benign = true_df[(true_df['actual'] == 0) == True]
    df_attack = true_df[(true_df['actual'] == 1) == True]
    benign_csv = X_test_df.loc[df_benign.index.values]
    attack_csv = X_test_df.loc[df_attack.index.values]
    benign_csv.to_csv('F:/data/ADD/201210/'+mal_list[mal_num]+'_benign_cp.csv', index=False)
    attack_csv.to_csv('F:/data/ADD/201210/'+mal_list[mal_num]+'_attack_cp.csv', index=False)

    print("\nCheck centroid vector")
    fcm_center = fcm.centers.tolist()

    benign_data = pd.read_csv("F:/data/ADD/201210/"+mal_list[mal_num]+"_benign_cp.csv")
    attack_data = pd.read_csv("F:/data/ADD/201210/"+mal_list[mal_num]+"_attack_cp.csv")

    standard_data = pd.concat([benign_data, attack_data], axis=0)
    centroid = fcm_center

    std_scaler = StandardScaler()
    std_scaler.fit(standard_data)
    benign_scaler = pd.DataFrame(data=std_scaler.transform(benign_data), columns=benign_data.columns)
    attack_scaler = pd.DataFrame(data=std_scaler.transform(attack_data), columns=attack_data.columns)
    centroid = list(std_scaler.transform(centroid))

    benign_distance = pd.DataFrame(index=range(0,len(benign_scaler)), columns=['distance'])
    attack_distance = pd.DataFrame(index=range(0,len(attack_scaler)), columns=['distance'])

    print("\n정상/악성 각각의 벡터에 대한 유클리드 거리 측정")
    for i in range(len(benign_data)):
        benign_distance.loc[i] = distance.euclidean(benign_scaler.loc[i],centroid[0])

    for i in range(len(attack_data)):
        attack_distance.loc[i] = distance.euclidean(attack_scaler.loc[i],centroid[0])

    print("\n유클리드 거리 기반 평균 및 표준편차 계산")
    benign_dis_arr = benign_distance.to_numpy()
    attack_dis_arr = attack_distance.to_numpy()

    benign_mean = np.mean(benign_dis_arr)   #평균
    benign_std = np.std(attack_dis_arr) #표준편차
    attack_mean = np.mean(attack_dis_arr)   #평균
    attack_std = np.std(attack_dis_arr)     #표준편차

    print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean,benign_std,attack_mean,attack_std))

    print("\n클러스터 결정경계에 위치되어 있는 데이터 추출")
    benign_bounderies_index = benign_distance[(benign_distance['distance'] >= (benign_mean+benign_std)) == True]
    benign_bounderies = benign_data.loc[benign_bounderies_index.index.values]
    print("\nbenign boundery : %s"%str(benign_bounderies.shape))

    attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean+attack_std)) == True]
    attack_bounderies = attack_data.loc[attack_bounderies_index.index.values]
    print("\nattack boundery : %s"%str(attack_bounderies.shape))

    standard_data = pd.concat([benign_bounderies, attack_bounderies], axis=0)
    std_scaler = StandardScaler()
    fitted = std_scaler.fit(standard_data)
    benign_bounderies_scaler = pd.DataFrame(data=std_scaler.transform(benign_bounderies), columns=benign_bounderies.columns)
    attack_bounderies_scaler = pd.DataFrame(data=std_scaler.transform(attack_bounderies), columns=attack_bounderies.columns)
    diff_data = pd.DataFrame(data=std_scaler.transform(pt_data), columns=pt_data.columns)
    print("\nInvalid Data : %s"%str(diff_data.shape))

    benign_dis = pd.DataFrame(index=range(0,len(benign_bounderies_scaler)), columns=['distance'])
    attack_dis = pd.DataFrame(index=range(0,len(attack_bounderies_scaler)), columns=['distance'])
    dif_prelist = []

    print("\nEuclidean distance measure between benign/attack boundaries and invalid data")
    for j in range(len(diff_data)):
        for i in range(len(benign_bounderies_scaler)):
            benign_dis.loc[i] = distance.euclidean(benign_bounderies_scaler.loc[i],diff_data.loc[j])

        for i in range(len(attack_bounderies_scaler)):
            attack_dis.loc[i] = distance.euclidean(attack_bounderies_scaler.loc[i],diff_data.loc[j])

        if benign_dis['distance'].min() > attack_dis['distance'].min():
            print("{0}번째 Invalid Data => Attack / {1} : {2}".format(j, benign_dis['distance'].min(),attack_dis['distance'].min()))
            dif_prelist.append(1)
        else:
            print("{0}번째 Invalid Data => Benign / {1} : {2}".format(j, benign_dis['distance'].min(),attack_dis['distance'].min()))
            dif_prelist.append(0)

    dif_predict = pd.DataFrame(data=dif_prelist, columns=['predict'])

    incorrect_data = dif_data.loc[wrong_index]
    temp_belist = [0 for i in range(len(df_benign))]
    temp_atlist = [1 for i in range(len(df_attack))]
    temp_inpredic = incorrect_data['predict'].tolist()
    temp_inactual = incorrect_data['actual'].tolist()

    dif_prelist = dif_prelist+temp_belist+temp_atlist+temp_inpredic
    our_proposed_df = pd.DataFrame(data=dif_prelist, columns=['predict'])

    temp_label = pt_data_label['actual'].tolist()
    temp_label = temp_label+temp_belist+temp_atlist+temp_inactual
    our_proposed_df['actual'] = temp_label
    print("Shap : %s"%str(our_proposed_df.shape))
    our_proposed_df.to_csv("F:/data/ADD/201210/"+mal_list[mal_num]+"_predict.csv", index=False)

    our_proposed_result = scoring(our_proposed_df)

    print("\nvalidation")
    result_arr = np.array([our_proposed_result])
    result_df = pd.DataFrame(data=result_arr,columns=['accuracy','Precision','Recall','F1','tn','fp','fn','tp'],index=[mal_list[mal_num]])
    print(result_df)
    result_df.to_csv("F:/data/ADD/201210/"+mal_list[mal_num]+"_result.csv", index=False)