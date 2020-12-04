from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import homogeneity_score, adjusted_mutual_info_score, accuracy_score, precision_score,recall_score,f1_score
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
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)

best_cents = [[0.8780548390411661, 0.9434844754118773, 0.08570221749085585, 0.9441549808772682, 0.9508694103254853, 0.8535406951590411, 0.8905401456770801, 0.39582444741022377, 0.3667930775720254, 0.3952155401243918, 0.0032622049637311616, 0.9069492338739097, 0.7504700387230853, -0.13242523171180198, 0.9508694103254853, 0.8905401456770801, 0.9434844754118773, 0.08570221749085585, 0.11618334316338697], [-0.9412667613865507, -1.0119779944751732, -0.09306364705246235, -1.0126546024310055, -1.019845635380197, -0.9157598569900075, -0.9550845402220292, -0.426040107421912, -0.3949314190439888, -0.4252499970085256, -0.004498061858428147, -0.9732354941599739, -0.8057760992662832, 0.14348119625617362, -1.019845635380197, -0.9550845402220292, -1.0119779944751732, -0.09306364705246235, -0.12494198981745376]]
best_cents = np.array(best_cents)

centroid_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
random_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
plus_df = pd.DataFrame(index=range(0,k_num),columns={'h_score','ar_score','ami_score','accuracy','precision','recall','f1','time'})
index_num = 0

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Optimized centroid
    km = KMeans(n_clusters=NUM_CLUSTERS, init=best_cents, max_iter=10000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = homogeneity_score(y_test, predic_km)
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
    km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=10000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = homogeneity_score(y_test, predic_km)
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
    km = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', max_iter=10000, n_init=1)
    km_start = time.time()
    km.fit(X_train)
    km_end = time.time()
    predic_km = km.predict(X_test)

    h_score = homogeneity_score(y_test, predic_km)
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
print("homogeneity_score : ", float(centroid_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(centroid_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(centroid_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(centroid_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(centroid_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(centroid_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(centroid_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(centroid_df['time'].sum(axis=0))/k_num)

print(color.BOLD+"\nk-means(랜덤 최적화)"+color.END)
print("homogeneity_score : ", float(random_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(random_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(random_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(random_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(random_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(random_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(random_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(random_df['time'].sum(axis=0))/k_num)

print(color.BOLD + "\nk-means(k-means++ 최적화)" + color.END)
print("homogeneity_score : ", float(plus_df['h_score'].sum(axis=0))/k_num)
print("adjusted_rand_score : ", float(plus_df['ar_score'].sum(axis=0))/k_num)
print("adjusted_mutual_info_score : ", float(plus_df['ami_score'].sum(axis=0))/k_num)
print("Accuracy : ", float(plus_df['accuracy'].sum(axis=0))/k_num)
print("Precision : ", float(plus_df['precision'].sum(axis=0))/k_num)
print("Recall : ", float(plus_df['recall'].sum(axis=0))/k_num)
print("F1 : ", float(plus_df['f1'].sum(axis=0))/k_num)
print("Time : ", float(plus_df['time'].sum(axis=0))/k_num)