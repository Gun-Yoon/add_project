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
import matplotlib.pyplot as plt

def centroid_extraction(df):
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=1, init='random', max_iter=1, n_init=1)
    km.fit(df)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    for iter in range(100):
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
   score_list = [accuracy,Precision,Recall,F1]
   return score_list

data = pd.read_csv('dataset/pre_train.csv')
#data = data.sample(n=100, random_state=42)
data = data[(data['Label'] != 'normal') == True]

data_label = data['Label'].tolist()
data = data.drop(['Label'], axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(data)
X = std_scaler.transform(data)

train_data = pd.DataFrame(data=X, columns=data.columns)
train_data['Label'] = data_label

label_list = list(set(train_data['Label']))
#print(label_list)
cents_list = []

#Centroid 추출을 위한 k-means 학습 수행
for label in label_list:
    print("Initial centroid 찾기("+str(label)+")")
    temp_df = train_data[(train_data['Label'] == label) == True]
    temp_df = temp_df.drop(['Label'],axis=1)

    best_cent = centroid_extraction(temp_df)
    cents_list.append(best_cent)

print("\n거리 측정")
dis_df = train_data.drop(['Label'],axis=1)
dis_arr = np.empty((0 ,len(label_list)), float)
for data_num in range(len(train_data)):
    distance_list = []
    for label_num in range(len(label_list)):
        dis = distance.euclidean(cents_list[label_num], dis_df.iloc[data_num])
        distance_list.append(dis)
    #print(distance_list)
    dis_arr = np.vstack([dis_arr,distance_list])

for i in range(len(label_list)):
    dis_df[label_list[i]] = dis_arr[:,i]
dis_df['Label'] = train_data['Label'].tolist()
#print(dis_df.head(10))

weibull_model = []  #순서대로 shape, loc, scale를 입력
mean_list = []
std_list = []
proba_temp = []
for label in label_list:
    temp_df = dis_df[(dis_df['Label'] == label) == True]
    temp_df_label = temp_df['Label'].tolist()
    temp_df = temp_df.drop(['Label'],axis=1)

    mean_temp = [np.mean(temp_df[la_name].to_numpy()) for la_name in label_list]
    std_temp = [np.std(temp_df[la_name].to_numpy()) for la_name in label_list]
    mean_list.append(mean_temp)
    std_list.append(std_temp)

    vector_df = temp_df.iloc[:,[(i+15) for i in range(len(label_list))]]
    #print(vector_df)
    #print([(i+15) for i in range(len(label_list))])
    #print(len(vector_df))

    dis_l = []
    for num in range(len(temp_df)):
        dis = [vector_df.iloc[num][0],vector_df.iloc[num][1],vector_df.iloc[num][2],vector_df.iloc[num][3]]#,vector_df.iloc[num][4]]
        '''
        dis = math.sqrt((vector_df.iloc[num][0] * mean_temp[0]) + (vector_df.iloc[num][1] * mean_temp[1]) +
                        (vector_df.iloc[num][2] * mean_temp[2]) + (vector_df.iloc[num][3] * mean_temp[3])
                        + (vector_df.iloc[num][4] * mean_temp[4]))
        '''
        #distance.euclidean(vector_df.iloc[num], mean_temp)
        #print(dis)
        dis_l.append(min(dis))

    temp_df['distance'] = dis_l
    temp_df['Label'] = temp_df_label
    temp_df = temp_df.sort_values(by=['distance'], axis=0, ascending=False)
    #print(temp_df.head(5))
    # c(shape), loc(location), scale(scale)
    fig, ax = plt.subplots(1, 1)
    temp_df.to_csv("dataset/temp_"+str(label)+".csv", index=False)

    print("\nweibull 구하기(" + str(label) + ")")
    x = temp_df.iloc[:20,15]
    #print(x)
    shape, loc, scale = weibull_min.fit(x, floc=0)
    #print(shape, scale)
    weibull_model.append((shape, loc, scale))
    #t_data = temp_df.drop(['distance'],axis=1)
    #ax.plot(t_data, weibull_min.pdf(t_data, shape, loc, scale), 'bo', ms=1, alpha=0.6, label='weibull_min pdf')
    #plt.show()

    '''
    proba = []  # 각 class에 대한 확률갑 저장
    for data_num in range(len(temp_df)):
        wei = weibull_min.cdf(temp_df[label][data_num], shape, loc, scale)
        proba.append(round(temp_df[label][data_num]*wei, 10))

    proba_temp = np.mean(np.array(proba))
dis_wei = (np.array(dis))
'''

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

label_unknown = label_list#+['dos']

predict = []
#parameter_list = [0.0001,0.0001,0.001,0.01,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0,1]
#=0.001
#print(parameter)
for data_num in range(len(dis_df)):
    probability_cl = []  # 각 class에 대한 확률갑 저장
    for label_num in range(len(label_list)):
        wei = weibull_min.cdf(dis_df[label_list[label_num]][data_num], weibull_model[label_num][0], weibull_model[label_num][1], scale=weibull_model[label_num][2])
        #probability_cl.append(dis_df[label_list[label_num]][data_num]+(dis_df[label_list[label_num]][data_num]*wei))
        probability_cl.append(round(dis_df[label_list[label_num]][data_num]*wei, 10))
    #print(probability_cl)

    #probability_cl.append(np.sum(temp_dis*temp_wei))    #unkwon class 확률값 np.sum(temp_dis*temp_wei)

    '''
    if min(probability_cl) >= parameter:
        predict.append("dos")
    else:
        predict_index = probability_cl.index(min(probability_cl))
        predict.append(label_unknown[predict_index])
    '''

    predict_index = probability_cl.index(min(probability_cl))
    predict.append(label_unknown[predict_index])
    #print(label_unknown[predict_index])
    #print(test_label[data_num], label_unknown[predict_index])

result_df = pd.DataFrame(data=predict, columns=['predict'])
result_df['actual'] = test_label

result_score = scoring(result_df)
print(result_score)

print(pd.crosstab(result_df['actual'], result_df['predict'], rownames=['True'], colnames=['Predicted'], margins=True))

'''
test_data = pd.read_csv('dataset/pre_test.csv')
#test_data = test_data.sample(n=1000, random_state=42)
test_label = test_data['Label'].tolist()
test_data = test_data.drop(['Label'], axis=1)

x_test = std_scaler.transform(test_data)
test_data = pd.DataFrame(data=x_test, columns=test_data.columns)

print("\n각 데이터에 대한 거리 측정")
label_unknown = label_list#+['dos']
predict = []
for data_num in range(len(test_data)):
    temp_dis = []  # 각 class에 대한 거리 측정결과 임시 저장
    temp_wei = []  # 각 class에 대한 weibull결과 임시 저장
    probability_cl = []  # 각 class에 대한 확률갑 저장
    for label_num in range(len(label_list)):
        dis = distance.euclidean(mean_list[label_num], distance.euclidean(cents_list[label_num], test_data.iloc[data_num]))
        temp_dis.append(dis)
        wei = weibull_min.cdf(dis, weibull_model[label_num][0], weibull_model[label_num][1], scale=weibull_model[label_num][2])
        temp_wei.append(wei)
        probability_cl.append(dis-(dis*wei))  #-(dis*wei)
    temp_dis = np.array(temp_dis)
    temp_wei = np.array(temp_wei)
    #probability_cl.append(np.sum(temp_dis*temp_wei))    #unkwon class 확률값 np.sum(temp_dis*temp_wei)
    print(temp_dis)
    print(temp_wei)
    #print(probability_cl)
    predict_index = probability_cl.index(max(probability_cl))
    predict.append(label_unknown[predict_index])
    #print(label_unknown[predict_index])
    print(test_label[data_num], label_unknown[predict_index])

result_df = pd.DataFrame(data=predict, columns=['predict'])
result_df['actual'] = test_label

result_score = scoring(result_df)
print(result_score)

#정규분포 확인
from scipy.stats import norm
import matplotlib.pyplot as plt

rv = norm(loc=dis_mean, scale=dis_std)  # 평균(loc) / 표준편차(scale)
x = temp_df['distance'].tolist()
y = rv.pdf(x)  # X 범위에 따른 정규확률밀도값
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, 'bo', ms=1, label='normal pdf')
plt.show()

#weibull 측정
from scipy.stats import weibull_min #c(shape), loc(location), scale(scale)
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

x = temp_df['distance'].to_numpy()
shape, loc, scale = weibull_min.fit(x)
ax.plot(x, weibull_min.pdf(x, shape), 'r-', lw=1, alpha=0.6, label='weibull_min pdf')
#ax.legend(loc='best', frameon=False)
plt.show()
'''