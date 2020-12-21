"""
   ????
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

def scoring(df):
    accuracy = accuracy_score(df['actual'], df['predict'])
    Precision = precision_score(df['actual'], df['predict'], average=None)
    Recall = recall_score(df['actual'], df['predict'], average=None)
    F1 = f1_score(df['actual'], df['predict'], average=None)
    score_list = [accuracy,F1,Precision,Recall]
    return score_list

# Some variables
NUM_CLUSTERS = 1
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
    fitted = std_scaler.fit(train_data)
    X = std_scaler.transform(train_data)
    x_add = std_scaler.transform(data)

    #x_train, x_test, y_train, y_test = train_test_split(data,label, test_size=0.2, random_state=42)
    #x_train = np.append(x_train, train_data,axis=0)

    #k-means 학습 수행
    cents_list = []
    inert_list = []

    km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1, n_init=1)
    km.fit(X)
    inertia = km.inertia_
    cents = km.cluster_centers_
    cents_list.append(cents)
    inert_list.append(inertia)

    print("\nInitial centroid 찾기")
    for iter in range(NUM_ITER):
      km = KMeans(n_clusters=NUM_CLUSTERS, init=cents, max_iter=1, n_init=1)
      km.fit(X)
      cc = km.cluster_centers_.tolist()
      #print('Centroids:', cc)
      inertia = km.inertia_
      cents = km.cluster_centers_

      cents_list.append(cents)
      inert_list.append(inertia)

    # Get best centroids to use for full clustering
    best_cents = cents_list[inert_list.index(min(inert_list))]

    # fit the fuzzy-c-means
    fcm = FCM(n_clusters=2, first_center=best_cents, max_iter=500, random_state=42)
    fcm.fit(X)
    probability = fcm.predict(x_add)
    probability_df = pd.DataFrame(data=probability[:,2], columns=['predict'])
    cluster = collections.Counter(probability[:,2])
    print(cluster)
    if cluster[0.0] >= cluster[1.0]:
        probability_df.loc[probability_df['predict'] == 0.0,'predict'] = name
        probability_df.loc[probability_df['predict'] == 1.0, 'predict'] = 'outlier'
    else:
        probability_df.loc[probability_df['predict'] == 1.0,'predict'] = name
        probability_df.loc[probability_df['predict'] == 0.0, 'predict'] = 'outlier'

    result_df = pd.DataFrame(data=x_add, columns=data.columns)
    result_df['actual'] = list(label)
    result_df['predict'] = probability_df['predict'].tolist()
    #result_df.loc[result_df['actual'] != name, 'actual'] = 'outlier'
    result_df.to_csv('dataset/fcm_result/'+name+'.csv', index=False)
    print(list(set(result_df['actual'])))
    print(len(result_df))
    #score = scoring(result_df)
    #print(score)