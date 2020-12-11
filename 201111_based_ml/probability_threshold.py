from fcmeans import FCM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import time
from scipy.spatial import distance

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def check_different(df):
  dif_indexes = df[(df['pre_class'] != df['class']) == True]
  return dif_indexes

def check_match(df):
  dif_indexes = df[(df['pre_class'] == df['class']) == True]
  return dif_indexes

data = pd.read_csv("dataset/Unknown_data.csv")
X = data.drop(['Label'], axis=1)
col = X.columns
X = X.to_numpy()

y = data['Label']
le = LabelEncoder().fit(y)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

centers = [[45747.855292236476, 921.3124659206626, 407.06764737948333, 919.9929402443679, 186.2265678694155, 360.50848605554114, 119.16421198018449, 5595039.8150694445, 1432236.89777364, 5451485.625738382, 21955.05634316005, 166.3279399863208, 116.3242207005973, 1.1114355393300457, 186.2265678694155, 119.16421198018449, 921.3124659206626, 407.06764737948333, 229.59300510278956], [633.5453868005061, 13.311492579165701, 35.45257318447153, 13.051967221349628, 4.065577055191767, 29.922603051099713, 7.58443241651873, 25286.235250015743, 17660.494008300826, 21851.365482692607, 14800.013759329424, 69.73815264740048, 5.022356752792227, 1233.9959969564013, 4.065577055191767, 7.58443241651873, 13.311492579165701, 35.45257318447153, 1053.2675415630874]]

# fit the fuzzy-c-means
fcm = FCM(n_clusters=2, first_center=centers, max_iter=100)
fcm.fit(X_train)

# outputs
fcm_centers = fcm.centers   # 첫번째는 'Bengin' cetroid, 두번쨰는 'attack' centroid
fcm_labels  = fcm.u.argmax(axis=1)
probability = fcm.predict(X_test)

result_df = pd.DataFrame(data=probability, columns=[0,1,'pre_class'])
result_df['class'] = y_test

print(color.BOLD+"\nValidate records in cluster(find invalid record)"+color.END)
dif_data = check_different(result_df)
print(dif_data.shape)

#probability threshold(pt)를 기준으로 부합한 데이터 추출
# 0.4 <= pt <= 0.6
small_num = [round(i*(0.01),2) for i in range(1,50)]
small_num.reverse()
big_num = [round(i*(0.01),2) for i in range(51,101)]
result_data = pd.DataFrame(index=range(0,len(big_num)),columns=['accuracy','precision','recall','f1-score','time','number of data'])

for k in range(len(small_num)):
    dif_df = dif_data
    print(color.BOLD + "\nCheck probability threshold : "+str(small_num[k])+"<=Threshold<="+str(big_num[k])+ color.END)
    for i in dif_df.index:
        if dif_df.loc[i][0] <= small_num[k] or dif_df.loc[i][0] >= big_num[k]:
            dif_df = dif_df.drop([i])
    print(dif_df.shape)

    print(color.BOLD + "\nSave invalid cluster" + color.END)
    test_data = pd.DataFrame(data=X_test, columns=col)
    invalid_data = test_data.loc[dif_df.index.values]
    test_data_label = pd.DataFrame(data=y_test, columns=['class'])
    invalid_data_label = test_data_label.loc[dif_df.index.values]
    print(invalid_data.shape)

    print(color.BOLD + "\nCheck correct record" + color.END)
    corr_df = check_match(result_df)
    df_benign = corr_df[(corr_df['class'] == 0) == True]
    df_attack = corr_df[(corr_df['class'] == 1) == True]

    benign_data = test_data.loc[df_benign.index.values]
    attack_data = test_data.loc[df_attack.index.values]
    benign_data.to_csv('dataset/df_benign.csv', index=False)
    attack_data.to_csv('dataset/df_attack.csv', index=False)

    benign_raw = pd.read_csv("dataset/df_benign.csv")
    attack_raw = pd.read_csv("dataset/df_attack.csv")
    standard_data = pd.concat([benign_raw, attack_raw], axis=0)
    centroid = fcm_centers.tolist()

    std_scaler = StandardScaler()
    fitted = std_scaler.fit(standard_data)
    benign_data = pd.DataFrame(data=std_scaler.transform(benign_raw), columns=benign_raw.columns)
    attack_data = pd.DataFrame(data=std_scaler.transform(attack_raw), columns=attack_raw.columns)
    centroid = list(std_scaler.transform(centroid))

    benign_distance = pd.DataFrame(index=range(0, len(benign_data)), columns=['distance'])
    attack_distance = pd.DataFrame(index=range(0, len(attack_data)), columns=['distance'])

    print(color.RED + "\n정상/악성 각각의 벡터에 대한 유클리드 거리 측정" + color.END)
    for i in range(len(benign_data)):
        benign_distance.loc[i] = distance.cityblock(benign_data.loc[i], centroid[0])

    for i in range(len(attack_data)):
        attack_distance.loc[i] = distance.cityblock(attack_data.loc[i], centroid[0])

    print(color.RED + "\n유클리드 거리 기반 평균 및 표준편차 계산" + color.END)
    benign_arr = benign_distance.to_numpy()
    attack_arr = attack_distance.to_numpy()

    benign_mean = np.mean(benign_arr)  # 평균
    benign_std = np.std(benign_arr)  # 표준편차
    attack_mean = np.mean(attack_arr)  # 평균
    attack_std = np.std(attack_arr)  # 표준편차

    print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean, benign_std, attack_mean,
                                                                          attack_std))

    print(color.RED + "\n클러스터 결정경계에 위치되어 있는 데이터 추출" + color.END)

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
    benign_bounderies = pd.DataFrame(data=std_scaler.transform(benign_bounderies), columns=benign_bounderies.columns)
    attack_bounderies = pd.DataFrame(data=std_scaler.transform(attack_bounderies), columns=attack_bounderies.columns)
    diff_data = pd.DataFrame(data=std_scaler.transform(invalid_data), columns=invalid_data.columns)

    benign_distance = pd.DataFrame(index=range(0, len(benign_bounderies)), columns=['distance'])
    attack_distance = pd.DataFrame(index=range(0, len(attack_bounderies)), columns=['distance'])
    dif_prelist = []

    print(color.RED + "\nEuclidean distance measure between benign/attack boundaries and invalid data" + color.END)
    t_start = time.time()
    for j in range(len(diff_data)):
        for i in range(len(benign_bounderies)):
            benign_distance.loc[i] = distance.cityblock(benign_bounderies.loc[i], diff_data.loc[j])

        for i in range(len(attack_bounderies)):
            attack_distance.loc[i] = distance.cityblock(attack_bounderies.loc[i], diff_data.loc[j])

        if benign_distance['distance'].min() > attack_distance['distance'].min():
            dif_prelist.append(1)
        else:
            dif_prelist.append(0)
    t_end = time.time()

    pt_df = pd.DataFrame(data=dif_prelist, columns=['predict'])
    pt_df['actual'] = invalid_data_label['class'].tolist()
    print(pt_df.shape)

    accuracy = accuracy_score(pt_df['actual'], pt_df['predict'])
    Precision = precision_score(pt_df['actual'], pt_df['predict'], average=None)
    Precision = sum(Precision) / 2
    recall = recall_score(pt_df['actual'], pt_df['predict'], average=None)
    recall = sum(recall) / 2
    f1 = f1_score(pt_df['actual'], pt_df['predict'], average=None)
    f1 = sum(f1) / 2
    #print([accuracy, Precision, recall, f1,t_end-t_start,len(invalid_data)])
    result_data.loc[k] = [accuracy, Precision, recall, f1,t_end-t_start,len(invalid_data)]
    print(result_data.loc[k])
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print(result_data.shape)
result_data.to_csv("dataset/threshold_2.csv", index=False)