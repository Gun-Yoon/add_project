from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from fcmeans import FCM
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd
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

# Some variables
NUM_CLUSTERS = 2
k_num = 10
kf = KFold(n_splits=k_num, shuffle=True, random_state=42)

print("\n데이터 호출")
data = pd.read_csv("dataset/Unknown_data.csv")


y = data['Label']
le = LabelEncoder().fit(y)
y = le.transform(y)

X = data.drop(['Label'], axis=1)
col = X.columns
X = X.to_numpy()
#std_scaler = StandardScaler()
#fitted = std_scaler.fit(X)
#X = std_scaler.transform(X)

centers = [[45747.855292236476, 921.3124659206626, 407.06764737948333, 919.9929402443679, 186.2265678694155, 360.50848605554114, 119.16421198018449, 5595039.8150694445, 1432236.89777364, 5451485.625738382, 21955.05634316005, 166.3279399863208, 116.3242207005973, 1.1114355393300457, 186.2265678694155, 119.16421198018449, 921.3124659206626, 407.06764737948333, 229.59300510278956], [633.5453868005061, 13.311492579165701, 35.45257318447153, 13.051967221349628, 4.065577055191767, 29.922603051099713, 7.58443241651873, 25286.235250015743, 17660.494008300826, 21851.365482692607, 14800.013759329424, 69.73815264740048, 5.022356752792227, 1233.9959969564013, 4.065577055191767, 7.58443241651873, 13.311492579165701, 35.45257318447153, 1053.2675415630874]]
centers_arr = np.array(centers)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#K-means
print("\nK-means")
kmeans = KMeans(n_clusters=NUM_CLUSTERS, init=centers_arr, max_iter=100, n_init=1)
kmeans.fit(X_train)
predic_km = kmeans.predict(X_test)
kmeans_df = pd.DataFrame(data=predic_km, columns=['predict'])
kmeans_df['actual'] = y_test
kmeans_result = scoring(kmeans_df)

#K-means++
print("\nK-means++")
kmeans_plus = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', max_iter=100, n_init=1)
kmeans_plus.fit(X_train)
predic_plus = kmeans_plus.predict(X_test)
plus_df = pd.DataFrame(data=predic_plus, columns=['predict'])
plus_df['actual'] = y_test
plus_result = scoring(plus_df)

#fuzzy c-means
print("\nfuzzy c-means")
fcm = FCM(n_clusters=2, first_center=centers, max_iter=100)
fcm.fit(X_train)
probability = fcm.predict(X_test)
probability = np.array(probability)
fcm_df = pd.DataFrame(data=probability, columns=[0,1,'predict'])
fcm_df['actual'] = y_test
fcm_result = scoring(fcm_df)

#Our proposed method
print("\nOur proposed")
fcm = FCM(n_clusters=2, first_center=centers, max_iter=100)
fcm.fit(X_train)
probability = fcm.predict(X_test)
probability = np.array(probability)
fcm_df = pd.DataFrame(data=probability, columns=[0,1,'predict'])
fcm_df['actual'] = y_test

#Validate records in cluster(find invalid record)
dif_df, true_df = check_different(fcm_df)

#probability threshold(pt)를 기준으로 부합한 데이터 추출(0.46 < Threshold < 0.54)
wrong_index = []
for i in dif_df.index:
    if dif_df.loc[i][0] <= 0.46 or dif_df.loc[i][0] >= 0.54:
        wrong_index.append(i)
        dif_df = dif_df.drop([i])

#Save invalid cluster
X_test_df = pd.DataFrame(data=X_test, columns=col)
pt_data = X_test_df.loc[dif_df.index.values]
X_test_df_label = pd.DataFrame(data=y_test, columns=['actual'])
pt_data_label = X_test_df_label.loc[dif_df.index.values]

#Check correct record
df_benign = true_df[(true_df['actual'] == 0) == True]
df_attack = true_df[(true_df['actual'] == 1) == True]
benign_csv = X_test_df.loc[df_benign.index.values]
attack_csv = X_test_df.loc[df_attack.index.values]
benign_csv.to_csv('dataset/benign_cp.csv', index=False)
attack_csv.to_csv('dataset/attack_cp.csv', index=False)

#Check centroid vector
fcm_center = fcm.centers.tolist()

benign_data = pd.read_csv("dataset/benign_cp.csv")
attack_data = pd.read_csv("dataset/attack_cp.csv")

standard_data = pd.concat([benign_data, attack_data], axis=0)
centroid = fcm_center

std_scaler = StandardScaler()
std_scaler.fit(standard_data)
benign_scaler = pd.DataFrame(data=std_scaler.transform(benign_data), columns=benign_data.columns)
attack_scaler = pd.DataFrame(data=std_scaler.transform(attack_data), columns=attack_data.columns)
centroid = list(std_scaler.transform(centroid))

benign_distance = pd.DataFrame(index=range(0,len(benign_scaler)), columns=['distance'])
attack_distance = pd.DataFrame(index=range(0,len(attack_scaler)), columns=['distance'])

#정상/악성 각각의 벡터에 대한 유클리드 거리 측정
for i in range(len(benign_data)):
    benign_distance.loc[i] = distance.euclidean(benign_scaler.loc[i],centroid[0])

for i in range(len(attack_data)):
    attack_distance.loc[i] = distance.euclidean(attack_scaler.loc[i],centroid[0])

#유클리드 거리 기반 평균 및 표준편차 계산
benign_dis_arr = benign_distance.to_numpy()
attack_dis_arr = attack_distance.to_numpy()

benign_mean = np.mean(benign_dis_arr)   #평균
benign_std = np.std(attack_dis_arr) #표준편차
attack_mean = np.mean(attack_dis_arr)   #평균
attack_std = np.std(attack_dis_arr)     #표준편차

print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean,benign_std,attack_mean,attack_std))

#클러스터 결정경계에 위치되어 있는 데이터 추출
benign_bounderies_index = benign_distance[(benign_distance['distance'] >= (benign_mean+benign_std)) == True]
benign_bounderies = benign_data.loc[benign_bounderies_index.index]

attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean+attack_std)) == True]
attack_bounderies = attack_data.loc[attack_bounderies_index.index.values]

standard_data = pd.concat([benign_bounderies, attack_bounderies], axis=0)
std_scaler = StandardScaler()
fitted = std_scaler.fit(standard_data)
benign_bounderies_scaler = pd.DataFrame(data=std_scaler.transform(benign_bounderies), columns=benign_bounderies.columns)
attack_bounderies_scaler = pd.DataFrame(data=std_scaler.transform(attack_bounderies), columns=attack_bounderies.columns)
diff_data = pd.DataFrame(data=std_scaler.transform(pt_data), columns=pt_data.columns)

benign_dis = pd.DataFrame(index=range(0,len(benign_bounderies_scaler)), columns=['distance'])
attack_dis = pd.DataFrame(index=range(0,len(attack_bounderies_scaler)), columns=['distance'])
dif_prelist = []

#Euclidean distance measure between benign/attack boundaries and invalid data
for j in range(len(diff_data)):
    for i in range(len(benign_bounderies_scaler)):
        benign_dis.loc[i] = distance.euclidean(benign_bounderies_scaler.loc[i],diff_data.loc[j])

    for i in range(len(attack_bounderies_scaler)):
        attack_dis.loc[i] = distance.euclidean(attack_bounderies_scaler.loc[i],diff_data.loc[j])

    if benign_dis['distance'].min() > attack_dis['distance'].min():
        dif_prelist.append(1)
    else:
        dif_prelist.append(0)

dif_predict = pd.DataFrame(data=dif_prelist, columns=['predict'])

incorrect_data = dif_df.loc[wrong_index]
temp_belist = [0 for i in range(len(df_benign))]
temp_atlist = [1 for i in range(len(df_attack))]
temp_inpredic = incorrect_data['predict'].tolist()
temp_inactual = incorrect_data['actual'].tolist()

dif_prelist = dif_prelist+temp_belist+temp_atlist+temp_inpredic
our_proposed_df = pd.DataFrame(data=dif_prelist, columns=['predict'])

temp_label = pt_data_label['actual'].tolist()
temp_label = temp_label+temp_belist+temp_atlist+temp_inactual
our_proposed_df['actual'] = temp_label

our_proposed_result = scoring(our_proposed_df)

#validation
result_arr = np.array([kmeans_result,plus_result,fcm_result+our_proposed_result])
result_df = pd.DataFrame(data=result_arr,columns=['accuracy','Precision','Recall','F1','tn','fp','fn','tp'],
                         index=['kmeans','kmeans++','fuzzy c-means','our proposed'])
print(result_df)