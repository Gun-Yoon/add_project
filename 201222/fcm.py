from fcmeans import FCM
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance

def centroid_extraction(df):
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=2, init='random', max_iter=1, n_init=1)
    km.fit(df)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    for iter in range(100):
        km = KMeans(n_clusters=2, init=cents, max_iter=1, n_init=1)
        km.fit(df)
        inertia = km.inertia_
        cents = km.cluster_centers_

        cents_list.append(cents)
        inert_list.append(inertia)

    # Get best centroids to use for full clustering
    best_cents = cents_list[inert_list.index(min(inert_list))]
    return best_cents

def scoring(df):
   accuracy = accuracy_score(df['actual'], df['predict'])
   Precision = precision_score(df['actual'], df['predict'], average=None)
   Recall = recall_score(df['actual'], df['predict'], average=None)
   F1 = f1_score(df['actual'], df['predict'], average=None)
   score_list = [accuracy,Precision,Recall,F1]
   return score_list

train = pd.read_csv('dataset/pre_train.csv')
normal_df = train[(train.Label == 'normal') == True]
outlier_df = train[(train.Label != 'normal') == True]
train.loc[(train.Label != 'normal') == True, 'Label'] = 'outlier'
#train.loc[(train.Label == 'normal') == True, 'Label'] = 1

y_train = train.Label.tolist()
x_train = train.drop(['Label'], axis=1)
col = x_train.columns

std_scaler = StandardScaler()
fitted = std_scaler.fit(x_train)
X_train = std_scaler.transform(x_train)

#X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

test = pd.read_csv('dataset/pre_test.csv')
y_test_real = test.Label.tolist()
test.loc[(test.Label != 'normal') == True, 'Label'] = 'outlier'
#test.loc[(test.Label == 'normal') == True, 'Label'] = 0

y_test = test.Label.tolist()
x_test = test.drop(['Label'], axis=1)

X_test = std_scaler.transform(x_test)

#Centroid 추출을 위한 k-means 학습 수행
print("Initial centroid 찾기")
best_cent = centroid_extraction(X_train)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=2, first_center=best_cent, max_iter=100, random_state=42)
fcm.fit(X_train)

# outputs
fcm_centers = fcm.centers   # 첫번째는 'Bengin' cetroid, 두번쨰는 'attack' centroid
fcm_labels  = fcm.u.argmax(axis=1)
probability = fcm.predict(X_test)

result_df = pd.DataFrame(data=X_test, columns=col)
result_df['0'] = probability[:,0]
result_df['real'] = y_test_real
result_df['actual'] = y_test
result_df['predict'] = probability[:,2]
result_df.loc[(result_df.predict == 1) == True, 'predict'] = 'outlier'
result_df.loc[(result_df.predict == 0) == True, 'predict'] = 'normal'
print(result_df.head())
print(result_df.columns)

print("\nScoring")
result_score = scoring(result_df)
print(result_score)
#==========================FCM 기반 정상 anomaly detection 수행을 통한 정상 데이터 검출=====================================
# 결과로 나온 데이터는 result_df이고 여기서 predict 결과가 1인 데이터만을 가지고 연구 진행

#probability threshold(pt)를 기준으로 부합한 데이터 추출
# 0.4 <= pt <= 0.6
print("\nCheck probability threshold")
proba_check = []
for index in result_df.index:
    if 0.5 <= result_df['0'][index] and result_df['0'][index] <= 0.6:
        proba_check.append(index)
print(proba_check)

#df는 probability 확인을 통해 threshold 안에 포함된 데이터만 저장되어 있음
df = result_df.loc[proba_check]
print(df)
df_score = scoring(df)
print(df_score)

print("\n정상데이터 유클리드 거리 측정 및 boundery 데이터 추출")
normal_df = normal_df.drop(['Label'], axis=1)
normal_df = std_scaler.transform(normal_df)
normal_df = pd.DataFrame(data=normal_df, columns=col)

normal_dis = []
for num in range(len(normal_df)):
    normal_dis.append(distance.cityblock(normal_df.loc[num], best_cent[0]))
normal_df['distance'] = normal_dis

normal_mean = np.mean(normal_df.distance.tolist())  # 평균
normal_std = np.std(normal_df.distance.tolist())  # 표준편차

normal_boundery = normal_df[(normal_df.distance >= normal_mean+normal_std) == True]
normal_boundery = normal_boundery.drop(['distance'], axis=1)
#==============================================정상 추출 완료========================================================

print("\n공격데이터 유클리드 거리 측정 및 boundery 데이터 추출")
outlier_df = outlier_df.drop(['Label'], axis=1)
outlier_df = std_scaler.transform(outlier_df)
outlier_df = pd.DataFrame(data=outlier_df, columns=col)

outlier_dis = []
for num in range(len(outlier_df)):
    outlier_dis.append(distance.cityblock(outlier_df.loc[num], best_cent[1]))
outlier_df['distance'] = outlier_dis

outlier_mean = np.mean(outlier_df.distance.tolist())  # 평균
outlier_std = np.std(outlier_df.distance.tolist())  # 표준편차

outlier_boundery = outlier_df[(outlier_df.distance >= outlier_mean+outlier_std) == True]
outlier_boundery = outlier_boundery.drop(['distance'], axis=1)
#==============================================outlier 추출 완료========================================================
print("\n서로의 outlier를 기반으로 거리 재측정 및 relabeling")
cd = df[['0', 'real', 'actual','predict']]
check_df = df.drop(['0', 'real', 'actual','predict'], axis=1)

for num in check_df.index:
    nor_dis = []
    out_dis = []
    for nor in normal_boundery.index:
        nor_dis.append(distance.cityblock(check_df.loc[num], normal_boundery.loc[nor]))
    for out in outlier_boundery.index:
        out_dis.append(distance.cityblock(check_df.loc[num], outlier_boundery.loc[out]))

    if min(nor_dis) > min(out_dis):
        df.loc[num,['predict']] = 'outlier'
    else:
        df.loc[num,['predict']] = 'normal'

print(df)
df_score = scoring(df)
print(df_score)
#==============================================relabeling 완료========================================================

print(color.RED + "\n유클리드 거리 기반 평균 및 표준편차 계산" + color.END)
benign_arr = benign_distance.to_numpy()
attack_arr = attack_distance.to_numpy()

benign_mean = np.mean(benign_arr)  # 평균
benign_std = np.std(benign_arr)  # 표준편차
attack_mean = np.mean(attack_arr)  # 평균
attack_std = np.std(attack_arr)  # 표준편차

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

'''
# 한글 폰트 적용
plt.rc('font', family='NanumBarunGothic')
# 캔버스 사이즈 적용
plt.rcParams["figure.figsize"] = (9,6)

# 배경을 darkgrid 로 설정
sns.set(style='darkgrid')

result_A = result_df[['protocol_type', 'service', 'flag', 'src_bytes', 'count','actual']]
result_B = result_df[['diff_srv_rate', 'dst_host_count', 'dst_host_srv_count','dst_host_same_srv_rate',
                      'dst_host_diff_srv_rate','actual']]
result_C = result_df[['serror_rate','dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate','dst_host_serror_rate',
                      'dst_host_rerror_rate','actual']]

sns.pairplot(result_A, hue="actual")
plt.show()
'''