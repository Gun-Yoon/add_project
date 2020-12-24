"""
    1) 각 class에 대한 center 값 추출
    2) center와 각 record에 대한 거리 추출
    3) EVT기반 극값(n=20)에 대한 극단치 분포 생성 / n=20은 거리가 가장 먼 20개를 의미
    4) 새로 들어오는 데이터에 대한 각 class 별 distance 측정
    5) 측정 distance기반 극단 확률 계산
    6) 각 class 확률 및 unknown 확률 계산
    7) 결과 산출 및 검증
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler
from scipy.stats import weibull_min, norm
import math

def centroid_extraction(df):
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=1, init='random', max_iter=1, n_init=1)
    km.fit(df)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    for iter in range(10):
        km = KMeans(n_clusters=1, init=cents, max_iter=1, n_init=1)
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
   score_list = [accuracy,F1,Precision,Recall]
   return score_list

#학습 데이터 생성----------------
data = pd.read_csv('dataset/pre_train.csv')
#data = data.sample(n=100, random_state=42)
data = data[(data['Label'] != 'normal') == True]
data = data[(data['Label'] != 'r2l') == True]

data_label = data['Label'].tolist()
data = data.drop(['Label'], axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(data)
X = std_scaler.transform(data)

train_data = pd.DataFrame(data=X, columns=data.columns)
train_data['Label'] = data_label
#------------------------------

#학습 데이터 Label 리스트 생성----
#label별 centeroid 리스트 생성
label_list = list(set(train_data['Label']))
#print(label_list)
cents_list = []
#------------------------------

#Centroid 추출을 위한 k-means 학습 수행
for label in label_list:
    print("Initial centroid 찾기("+str(label)+")")
    temp_df = train_data[(train_data['Label'] == label) == True]
    temp_df = temp_df.drop(['Label'],axis=1)

    best_cent = centroid_extraction(temp_df)
    cents_list.append(best_cent)
#------------------------------

#사전 학습(각 label별 distance와 mean distance와의 거리)된 데이터 호출
import os
path = "dataset/temp/"
file_list = os.listdir(path)
f_list = []
for f in file_list:
    df = pd.read_csv(path+f)
    f_list.append(df)
dis_df = pd.concat([i for i in f_list], axis=0)
dis_df = dis_df[(dis_df['Label'] != 'normal') == True]
dis_df = dis_df[(dis_df['Label'] != 'r2l') == True]
#------------------------------

#사전학습된 데이터 정렬(distance 높은 순서대로) 및 weibull fit 수행
weibull_model = []  #순서대로 shape, loc, scale를 입력
mean_list = []
print(label_list)
for label in label_list:
    temp_df = dis_df[(dis_df['Label'] == label) == True]
    temp_df = temp_df.drop(['Label'],axis=1)

    mean_temp = [np.mean(temp_df[la_name].to_numpy()) for la_name in label_list]
    mean_list.append(mean_temp)

    temp_df = temp_df.sort_values(by=['distance'], axis=0, ascending=False)
    #print(temp_df.head(5))

    print("\nweibull 구하기(" + str(label) + ")")
    x = temp_df.iloc[:20,15]
    shape, loc, scale = weibull_min.fit(x, floc=0)
    #print(shape, scale)
    weibull_model.append((shape, loc, scale))
#------------------------------

#테스트 데이터 생성----------------
test_data = pd.read_csv('dataset/pre_test.csv')
test_data = test_data[(test_data['Label'] != 'normal') == True]
#test_data = test_data.sample(n=1000, random_state=42)
test_label = test_data['Label'].tolist()
test_data = test_data.drop(['Label'], axis=1)

x_test = std_scaler.transform(test_data)
test_data = pd.DataFrame(data=x_test, columns=test_data.columns)
#------------------------------

#테스트 데이터 거리 측정----------
#centroid가 각 label별로 있기 때문에 각 레코드에 대한 각 label centroid와의 거리 생성
print("\n각 데이터에 대한 거리 측정")
dis_df = test_data
dis_arr = np.empty((0 ,len(label_list)), float)
for data_num in range(len(dis_df)):
    distance_list = []
    for label_num in range(len(label_list)):
        dis = distance.euclidean(cents_list[label_num], dis_df.iloc[data_num])
        distance_list.append(dis)
    #print(distance_list)
    dis_arr = np.vstack([dis_arr,distance_list])
#------------------------------

#생성된 distance 저장-----------
for i in range(len(label_list)):
    dis_df[label_list[i]] = dis_arr[:,i]
print(dis_df.head(5))
#------------------------------

'''
#생성된 distance 저장-----------
total_dis = []
for data_num in range(len(dis_df)):
    vector_df = dis_df.iloc[:, [(i + 15) for i in range(len(label_list))]]
    temp_dis = []  # 각 class에 대한 거리 측정결과 임시 저장
    for label in range(len(label_list)):
        dis = [abs(vector_df.iloc[data_num][0] - mean_list[label][0]),abs(vector_df.iloc[data_num][1] - mean_list[label][1]),
               abs(vector_df.iloc[data_num][2] - mean_list[label][2]),abs(vector_df.iloc[data_num][3] - mean_list[label][3]),
               abs(vector_df.iloc[data_num][4] - mean_list[label][4])]
        temp_dis.append(min(dis))
    total_dis.append(temp_dis)
wk_vector = np.array(total_dis)
print(wk_vector)
print(len(wk_vector))

for i in range(len(label_list)):
    dis_df[label_list[i]] = wk_vector[:,i]
'''

label_unknown = label_list+['r2l']

predict = []
parameter_list = [0.0001,0.0001,0.001,0.01,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0,1]
parameter=8
for data_num in range(len(dis_df)):
    probability_cl = []  # 각 class에 대한 확률갑 저장
    for label_num in range(len(label_list)):
        wei = weibull_min.cdf(dis_df[label_list[label_num]][data_num], weibull_model[label_num][0], weibull_model[label_num][1], scale=weibull_model[label_num][2])
        #probability_cl.append(dis_df[label_list[label_num]][data_num]+(dis_df[label_list[label_num]][data_num]*wei))
        probability_cl.append(round(dis_df[label_list[label_num]][data_num], 15)+round(dis_df[label_list[label_num]][data_num]*wei, 15))
    #print(probability_cl)

    #probability_cl.append(np.sum(temp_dis*temp_wei))    #unkwon class 확률값 np.sum(temp_dis*temp_wei)


    if min(probability_cl) >= parameter:
        predict.append("r2l")
    else:
        predict_index = probability_cl.index(min(probability_cl))
        predict.append(label_unknown[predict_index])

    #predict_index = probability_cl.index(min(probability_cl))
    #predict.append(label_unknown[predict_index])
    #print(label_unknown[predict_index])
    #print(test_label[data_num], label_unknown[predict_index])

result_df = pd.DataFrame(data=predict, columns=['predict'])
result_df['actual'] = test_label

print(parameter)
result_score = scoring(result_df)
print(result_score)

print(pd.crosstab(result_df['actual'], result_df['predict'], rownames=['True'], colnames=['Predicted'], margins=True))
