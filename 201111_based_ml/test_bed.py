from fcmeans import FCM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import homogeneity_score, adjusted_mutual_info_score, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
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
print("Class to number : ",le.classes_)
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
print(color.BOLD+"Result"+color.END)
print(result_df.shape)

print(color.BOLD+"\nScoring"+color.END)
h_score = homogeneity_score(result_df['class'], result_df['pre_class'])
ar_score = adjusted_rand_score(result_df['class'], result_df['pre_class'])
ami_socre = adjusted_mutual_info_score(result_df['class'], result_df['pre_class'])
print("Homogeneity_score : %.4f" %h_score)
print("Adjusted_rand_score : %.4f" %ar_score)
print("Adjusted_mutual_info_score : %.4f" %ami_socre)
print('Accuracy : %0.4f'%accuracy_score(result_df['class'], result_df['pre_class']))
Precision = precision_score(result_df['class'], result_df['pre_class'], average=None)
Precision = sum(Precision)/2
print('Precision : %0.4f'%Precision)
Recall = recall_score(result_df['class'], result_df['pre_class'], average=None)
Recall = sum(Recall)/2
print('Recall : %0.4f'%Recall)
F1 = f1_score(result_df['class'], result_df['pre_class'], average=None)
F1 = sum(F1)/2
print('F1-score : %0.4f'%F1)

print(color.BOLD+"\nValidate records in cluster(find invalid record)"+color.END)
dif_df = check_different(result_df)
#dif_df.to_csv('probability_data.csv', index=False)
print(dif_df.shape)

#probability threshold(pt)를 기준으로 부합한 데이터 추출
# 0.4 <= pt <= 0.6
print(color.BOLD+"\nCheck probability threshold"+color.END)
for i in dif_df.index:
    if dif_df.loc[i][0] <= 0.45 or dif_df.loc[i][0] >= 0.55:
        dif_df = dif_df.drop([i])
print(dif_df.shape)

print(color.BOLD+"\nSave invalid cluster"+color.END)
test_data = pd.DataFrame(data=X_test, columns=col)
invalid_data = test_data.loc[dif_df.index.values]
#invalid_data.to_csv('dataset/different_data.csv', index=False)
test_data_label = pd.DataFrame(data=y_test, columns=['class'])
invalid_data_label = test_data_label.loc[dif_df.index.values]
#invalid_data_label.to_csv('dataset/different_data_label.csv', index=False)
print(invalid_data.shape)

print(color.BOLD+"\nCheck correct record"+color.END)
corr_df = check_match(result_df)
df_benign = corr_df[(corr_df['class'] == 0) == True]
df_attack = corr_df[(corr_df['class'] == 1) == True]

benign_data = test_data.loc[df_benign.index.values]
attack_data = test_data.loc[df_attack.index.values]
#benign_data.to_csv('dataset/df_benign.csv', index=False)
#attack_data.to_csv('dataset/df_attack.csv', index=False)
print("Benign data set")
print(benign_data.shape)
print("\nAttack data set")
print(attack_data.shape)

print(color.BOLD+"\nCheck centroid vector"+color.END)
print(fcm_centers.tolist())

benign_raw = benign_data
attack_raw = attack_data
standard_data = pd.concat([benign_raw, attack_raw], axis=0)
centroid = fcm_centers.tolist()

std_scaler = StandardScaler()
fitted = std_scaler.fit(standard_data)
benign_data = pd.DataFrame(data=std_scaler.transform(benign_raw), columns=benign_raw.columns)
attack_data = pd.DataFrame(data=std_scaler.transform(attack_raw), columns=attack_raw.columns)
centroid = list(std_scaler.transform(centroid))

benign_distance = pd.DataFrame(index=range(0,len(benign_data)), columns=['distance'])
attack_distance = pd.DataFrame(index=range(0,len(attack_data)), columns=['distance'])

print(color.RED+"\n정상/악성 각각의 벡터에 대한 유클리드 거리 측정"+color.END)
for i in range(len(benign_data)):
    benign_distance.loc[i] = distance.euclidean(benign_data.loc[i],centroid[0])

for i in range(len(attack_data)):
    attack_distance.loc[i] = distance.euclidean(attack_data.loc[i],centroid[0])

print(color.RED+"\n유클리드 거리 기반 평균 및 표준편차 계산"+color.END)
benign_arr = benign_distance.to_numpy()
attack_arr = attack_distance.to_numpy()

benign_mean = np.mean(benign_arr)   #평균
benign_std = np.std(benign_arr)     #표준편차
attack_mean = np.mean(attack_arr)   #평균
attack_std = np.std(attack_arr)     #표준편차

print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean,benign_std,attack_mean,attack_std))

print(color.RED+"\n클러스터 결정경계에 위치되어 있는 데이터 추출"+color.END)

print("정상 클러스터 결정 경계 데이터 셋")
benign_bounderies_index = benign_distance[(benign_distance['distance'] >= (benign_mean+benign_std)) == True]
benign_bounderies = benign_raw.loc[benign_bounderies_index.index.values]
#benign_bounderies.to_csv('dataset/benign_bounderies.csv', index=False)
print(benign_bounderies.shape)

print("\n위협 클러스터 결정 경계 데이터 셋")
attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean+attack_std)) == True]
attack_bounderies = attack_raw.loc[attack_bounderies_index.index.values]
#attack_bounderies.to_csv('dataset/attack_bounderies.csv', index=False)
print(attack_bounderies.shape)

benign_bounderies = benign_bounderies
attack_bounderies = attack_bounderies
diff_data = invalid_data
dif_label = invalid_data_label

standard_data = pd.concat([benign_bounderies, attack_bounderies], axis=0)
std_scaler = StandardScaler()
fitted = std_scaler.fit(standard_data)
benign_bounderies = pd.DataFrame(data=std_scaler.transform(benign_bounderies), columns=benign_bounderies.columns)
attack_bounderies = pd.DataFrame(data=std_scaler.transform(attack_bounderies), columns=attack_bounderies.columns)
diff_data = pd.DataFrame(data=std_scaler.transform(diff_data), columns=diff_data.columns)

benign_distance = pd.DataFrame(index=range(0,len(benign_bounderies)), columns=['distance'])
attack_distance = pd.DataFrame(index=range(0,len(attack_bounderies)), columns=['distance'])
dif_prelist = []
print("\n")
print(diff_data.shape)

print(color.RED+"\nEuclidean distance measure between benign/attack boundaries and invalid data"+color.END)
for j in range(len(diff_data)):
    for i in range(len(benign_bounderies)):
        benign_distance.loc[i] = distance.euclidean(benign_bounderies.loc[i],diff_data.loc[j])

    for i in range(len(attack_bounderies)):
        attack_distance.loc[i] = distance.euclidean(attack_bounderies.loc[i],diff_data.loc[j])

    if benign_distance['distance'].min() > attack_distance['distance'].min():
        print("{0}번째 Invalid Data => Attack / {1} : {2}".format(j,benign_distance['distance'].min(),attack_distance['distance'].min()))
        dif_prelist.append(1)
    else:
        print("{0}번째 Invalid Data => Benign / {1} : {2}".format(j,benign_distance['distance'].min(),attack_distance['distance'].min()))
        dif_prelist.append(0)

dif_predict = pd.DataFrame(data=dif_prelist, columns=['predict'])
print("\n")

from sklearn.metrics import accuracy_score
print("\nACCURACY : %0.4f"%accuracy_score(dif_label, dif_predict))
print("PRECISION : %0.4f"%precision_score(dif_label, dif_predict, average=None))
print("RECALL : %0.4f"%recall_score(dif_label, dif_predict, average=None))
print("F1-SCORE : %0.4f"%f1_score(dif_label, dif_predict, average=None))