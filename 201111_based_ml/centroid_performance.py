from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import mean_squared_error, adjusted_mutual_info_score, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
import time
import numpy as np
import pandas as pd

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

# Some variables
NUM_CLUSTERS = 2
k_num = 5
kf = KFold(n_splits=k_num, shuffle=True, random_state=42)

print(color.BOLD+"\n데이터 호출"+color.END)
data = pd.read_csv("dataset/Unknown_data.csv")

y = data['Label']
le = LabelEncoder().fit(y)
print("Class to number : ",le.classes_)
y = le.transform(y)

X = data.drop(['Label'], axis=1).to_numpy()
#std_scaler = StandardScaler()
#fitted = std_scaler.fit(X)
#X = std_scaler.transform(X)

best_cents = [[45747.855292236476, 921.3124659206626, 407.06764737948333, 919.9929402443679, 186.2265678694155, 360.50848605554114, 119.16421198018449, 5595039.8150694445, 1432236.89777364, 5451485.625738382, 21955.05634316005, 166.3279399863208, 116.3242207005973, 1.1114355393300457, 186.2265678694155, 119.16421198018449, 921.3124659206626, 407.06764737948333, 229.59300510278956], [633.5453868005061, 13.311492579165701, 35.45257318447153, 13.051967221349628, 4.065577055191767, 29.922603051099713, 7.58443241651873, 25286.235250015743, 17660.494008300826, 21851.365482692607, 14800.013759329424, 69.73815264740048, 5.022356752792227, 1233.9959969564013, 4.065577055191767, 7.58443241651873, 13.311492579165701, 35.45257318447153, 1053.2675415630874]]
best_cents = np.array(best_cents)

centroid_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
random_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
plus_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
index_num = 0

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Optimized centroid
    km = KMeans(n_clusters=NUM_CLUSTERS, init=best_cents, max_iter=1000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = mean_squared_error(y_test, predic_km)
    ar_score = adjusted_rand_score(y_test, predic_km)
    ami_socre = adjusted_mutual_info_score(y_test, predic_km)
    accuracy = accuracy_score(y_test, predic_km)
    Precision = precision_score(y_test, predic_km, average=None)
    Precision = sum(Precision)/2
    Recall = recall_score(y_test, predic_km, average=None)
    Recall = sum(Recall)/2
    F1 = f1_score(y_test, predic_km, average=None)
    F1 = sum(F1)/2
    Time = (km_end - km_start)
    centroid_df.loc[index_num] = [h_score,ar_score,ami_socre,accuracy,Precision,Recall,F1,Time]

    #Random centroid
    km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = mean_squared_error(y_test, predic_km)
    ar_score = adjusted_rand_score(y_test, predic_km)
    ami_socre = adjusted_mutual_info_score(y_test, predic_km)
    accuracy = accuracy_score(y_test, predic_km)
    Precision = precision_score(y_test, predic_km, average=None)
    Precision = sum(Precision) / 2
    Recall = recall_score(y_test, predic_km, average=None)
    Recall = sum(Recall) / 2
    F1 = f1_score(y_test, predic_km, average=None)
    F1 = sum(F1)/2
    Time = (km_end - km_start)
    random_df.loc[index_num] = [h_score, ar_score, ami_socre, accuracy, Precision, Recall, F1, Time]

    # Random centroid
    km = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', max_iter=1000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = mean_squared_error(y_test, predic_km)
    ar_score = adjusted_rand_score(y_test, predic_km)
    ami_socre = adjusted_mutual_info_score(y_test, predic_km)
    accuracy = accuracy_score(y_test, predic_km)
    Precision = precision_score(y_test, predic_km, average=None)
    Precision = sum(Precision) / 2
    Recall = recall_score(y_test, predic_km, average=None)
    Recall = sum(Recall) / 2
    F1 = f1_score(y_test, predic_km, average=None)
    F1 = sum(F1)/2
    Time = (km_end - km_start)
    plus_df.loc[index_num] = [h_score, ar_score, ami_socre, accuracy, Precision, Recall, F1, Time]

    index_num = index_num+1

print(color.BOLD+"\nk-means(centroid 최적화)"+color.END)
print("mean_squared_error : ", float(centroid_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(centroid_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(centroid_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(centroid_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(centroid_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(centroid_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(centroid_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(centroid_df['time'].sum(axis=0))/k_num)

print(color.BOLD+"\nk-means(랜덤 최적화)"+color.END)
print("mean_squared_error : ", float(random_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(random_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(random_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(random_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(random_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(random_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(random_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(random_df['time'].sum(axis=0))/k_num)

print(color.BOLD + "\nk-means(k-means++ 최적화)" + color.END)
print("mean_squared_error : ", float(plus_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(plus_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(plus_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(plus_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(plus_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(plus_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(plus_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(plus_df['time'].sum(axis=0))/k_num)