from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import homogeneity_score, adjusted_mutual_info_score, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
import time
import numpy as np
import pandas as pd

# target은 x_train의 예측 label / labels는 x_train의 실제 label
# 0은 정상 / 1은 공격
def matrics_function(target, labels):
  label = np.chararray(target.shape, itemsize=150)
  for i in range(len(target)):
    if target[i] == 0:
      label[i] = 'Benign'
    elif target[i] == 1:
      label[i] = 'attack'

  df = pd.DataFrame({'predict': labels, 'actual': label})
  ct = pd.crosstab(df['predict'], df['actual'])

  return ct

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
kf = KFold(n_splits=10)

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

best_cents = [[0.8780548390411661, 0.9434844754118773, 0.08570221749085585, 0.9441549808772682, 0.9508694103254853, 0.8535406951590411, 0.8905401456770801, 0.39582444741022377, 0.3667930775720254, 0.3952155401243918, 0.0032622049637311616, 0.9069492338739097, 0.7504700387230853, -0.13242523171180198, 0.9508694103254853, 0.8905401456770801, 0.9434844754118773, 0.08570221749085585, 0.11618334316338697], [-0.9412667613865507, -1.0119779944751732, -0.09306364705246235, -1.0126546024310055, -1.019845635380197, -0.9157598569900075, -0.9550845402220292, -0.426040107421912, -0.3949314190439888, -0.4252499970085256, -0.004498061858428147, -0.9732354941599739, -0.8057760992662832, 0.14348119625617362, -1.019845635380197, -0.9550845402220292, -1.0119779944751732, -0.09306364705246235, -0.12494198981745376]]
best_cents = np.array(best_cents)

for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

print(color.BOLD+"\nk-means(centroid 최적화)"+color.END)
km_centroid = KMeans(n_clusters=NUM_CLUSTERS, init=best_cents, max_iter=10000, n_init=1)
km_centroid_start = time.time()
km_centroid.fit(X_train)
km_centroid_end = time.time()
predic_km_centroid = km_centroid.predict(X_test)
km_centroid_df = matrics_function(predic_km_centroid, y_test)

h_score = homogeneity_score(y_test, predic_km_centroid)
ar_score = adjusted_rand_score(y_test, predic_km_centroid)
ami_socre = adjusted_mutual_info_score(y_test, predic_km_centroid)
print("Homogeneity_score : %.4f" %h_score)
print("Adjusted_rand_score : %.4f" %ar_score)
print("Adjusted_mutual_info_score : %.4f" %ami_socre)
print('Accuracy : %0.4f'%accuracy_score(y_test, predic_km_centroid))
print('Precision : ', precision_score(y_test, predic_km_centroid, average=None))
print('Recall : ', recall_score(y_test, predic_km_centroid, average=None))
print('F1-score : ', f1_score(y_test, predic_km_centroid, average=None))
print('Time : ', (km_centroid_end-km_centroid_start))
#print(km_centroid_df)

print(color.BOLD+"\nk-means(랜덤 최적화)"+color.END)
km_random = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=10000, n_init=1)
km_random_start = time.time()
km_random.fit(X_train)
km_random_end = time.time()
predic_km_random = km_random.predict(X_test)
km_random_df = matrics_function(predic_km_random, y_test)

h_score = homogeneity_score(y_test, predic_km_random)
ar_score = adjusted_rand_score(y_test, predic_km_random)
ami_socre = adjusted_mutual_info_score(y_test, predic_km_random)
print("homogeneity_score : %.4f" %h_score)
print("adjusted_rand_score : %.4f" %ar_score)
print("adjusted_mutual_info_score : %.4f" %ami_socre)
print('Accuracy : %0.4f'%accuracy_score(y_test, predic_km_random))
print('Precision : ', precision_score(y_test, predic_km_random, average=None))
print('Recall : ', recall_score(y_test, predic_km_random, average=None))
print('F1-score : ', f1_score(y_test, predic_km_random, average=None))
print('Time : ', (km_random_end-km_random_start))
#print(km_random_df)

print(color.BOLD+"\nk-means(k-means++ 최적화)"+color.END)
km_plus = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', max_iter=10000, n_init=1)
km_plus_start = time.time()
km_plus.fit(X_train)
km_plus_end = time.time()
predic_km_plus = km_plus.predict(X_test)
km_plus_df = matrics_function(predic_km_plus, y_test)

h_score = homogeneity_score(y_test, predic_km_plus)
ar_score = adjusted_rand_score(y_test, predic_km_plus)
ami_socre = adjusted_mutual_info_score(y_test, predic_km_plus)
print("homogeneity_score : %.4f" %h_score)
print("adjusted_rand_score : %.4f" %ar_score)
print("adjusted_mutual_info_score : %.4f" %ami_socre)
print('Accuracy : %0.4f'%accuracy_score(y_test, predic_km_plus))
print('Precision : ', precision_score(y_test, predic_km_plus, average=None))
print('Recall : ', recall_score(y_test, predic_km_plus, average=None))
print('F1-score : ', f1_score(y_test, predic_km_plus, average=None))
print('Time : ', (km_plus_end-km_plus_start))

'''
# plot result
label_list = []
test_data['class'] = y_test
class_list = set(test_data['class'])
for i in class_list:
  label_list.append(i)
label_list.append('centroid')
label_list.append('invalid data')
df_list = []

for c in class_list:
  df_list.append(test_data[test_data['class']==c])

ff, axes = plt.subplots(len(col), len(col), figsize=(120,80))
for garo in range(len(col)):
  for sero in range(len(col)):
    for c_num in range(len(class_list)):
      scatter(x=df_list[c_num][col[garo]], y=df_list[c_num][col[sero]], ax=axes[garo,sero])
    scatter(x=invalid_data_arr[:, garo], y=invalid_data_arr[:, sero], ax=axes[garo,sero], marker='p', color='purple', s=80)
    scatter(x=fcm_centers[:, garo], y=fcm_centers[:, sero], ax=axes[garo, sero], marker='*', color='red', s=120)
    axes[garo,sero].set(xlabel=col[garo], ylabel=col[sero])
ff.tight_layout()
ff.legend([i for i in label_list], ncol=len(label_list), loc='lower center', borderaxespad=-1)
plt.savefig('savefig_default.png')
#plt.show()
'''