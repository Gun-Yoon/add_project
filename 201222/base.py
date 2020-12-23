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
from scipy.stats import weibull_min
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

    for iter in range(500):
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

data_label = data['Label'].tolist()
data = data.drop(['Label'], axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(data)
X = std_scaler.transform(data)

train_data = pd.DataFrame(data=X, columns=data.columns)
train_data['Label'] = data_label

label_list = list(set(train_data['Label']))
cents_list = []
distance_list = []

#Centroid 추출을 위한 k-means 학습 수행
for label in label_list:
    print("Initial centroid 찾기("+str(label)+")")
    temp_df = train_data[(train_data['Label'] == label) == True]
    temp_df = temp_df.drop(['Label'],axis=1)

    best_cent = centroid_extraction(temp_df)
    cents_list.append(best_cent)

print("\n거리 측정")
dis_df = train_data.drop(['Label'],axis=1)
for data_num in range(len(train_data)):
    for label_num in range(len(label_list)):
        if train_data['Label'][data_num] == label_list[label_num]:
            dis = distance.euclidean(cents_list[label_num], dis_df.iloc[data_num])
            distance_list.append(dis)
            print(dis)

dis_df['distance'] = distance_list
dis_df['Label'] = train_data['Label'].tolist()

weibull_model = []  #순서대로 shape, loc, scale를 입력
for label in label_list:
    print("\nweibull 구하기("+str(label)+")")
    temp_df = dis_df[(dis_df['Label'] == label) == True]
    temp_df = temp_df.drop(['Label'],axis=1)

    temp_df = temp_df.sort_values(by=['distance'], axis=0, ascending=False)

    # c(shape), loc(location), scale(scale)
    fig, ax = plt.subplots(1, 1)

    x = temp_df.iloc[:10,15]
    shape, loc, scale = weibull_min.fit(x, floc=0)
    print(shape, scale)
    weibull_model.append((shape, loc, scale))
    #ax.plot(data, weibull_min.cdf(data, shape, loc, scale), '-', lw=1, alpha=0.6, label='weibull_min pdf')
    #plt.show()

test_data = pd.read_csv('dataset/pre_test.csv')
test_label = test_data['Label'].tolist()
test_data = test_data.drop(['Label'], axis=1)

x_test = std_scaler.transform(test_data)
test_data = pd.DataFrame(data=x_test, columns=test_data.columns)

print("\n각 데이터에 대한 거리 측정")
label_unknown = label_list+['unknown']
predict = []
for data_num in range(len(test_data)):
    temp_dis = []  # 각 class에 대한 거리 측정결과 임시 저장
    temp_wei = []  # 각 class에 대한 weibull결과 임시 저장
    probability_cl = []  # 각 class에 대한 확률갑 저장
    for label_num in range(len(label_list)):
        dis = distance.euclidean(cents_list[label_num], test_data.iloc[data_num])
        temp_dis.append(dis)
        wei = weibull_min.pdf(dis, weibull_model[label_num][0], weibull_model[label_num][1], scale=weibull_model[label_num][2])
        temp_wei.append(wei)
        probability_cl.append(dis+(dis*wei))
    temp_dis = np.array(temp_dis)
    temp_wei = np.array(temp_wei)
    probability_cl.append(np.sum(temp_dis*temp_wei))    #unkwon class 확률값
    #print(temp_dis)
    #print(temp_wei)
    #print(probability_cl)
    predict_index = probability_cl.index(min(probability_cl))
    predict.append(label_unknown[predict_index])
    #print(label_unknown[predict_index])
    print(test_label[data_num], label_unknown[predict_index])

result_df = pd.DataFrame(data=predict, columns=['predict'])
result_df['actual'] = test_label

result_score = scoring(result_df)
print(result_score)


"""
#정규분포 확인
from scipy.stats import norm
import matplotlib.pyplot as plt

rv = norm(loc=dis_mean, scale=dis_std)  # 평균(loc) / 표준편차(scale)
x = temp_df['distance'].tolist()
y = rv.pdf(x)  # X 범위에 따른 정규확률밀도값
fig, ax = plt.subplots(1, 1)
ax.plot(x, y, 'bo', ms=1, label='normal pdf')
plt.show()
"""
"""
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
"""