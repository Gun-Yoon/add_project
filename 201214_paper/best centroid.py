"""
  # 'F:/data/KDD99/NSL-KDD/Train_data.csv'

#data = data.drop(['dst_host_srv_rerror_rate','rerror_rate','duration','srv_rerror_rate','hot','is_guest_login',
#                  'wrong_fragment','num_compromised','urgent','num_root','num_shells','num_access_files',
#                  'num_failed_logins','root_shell','num_file_creations','su_attempted','num_outbound_cmds',
#                  'land','is_host_login','dst_host_srv_diff_host_rate','dst_host_same_src_port_rate','dst_host_count',
#                  'srv_count','srv_diff_host_rate','dst_host_rerror_rate'], axis=1)
data = data.drop(['rerror_rate','duration','logged_in','dst_host_srv_rerror_rate','dst_bytes','srv_rerror_rate',
                  'hot','is_guest_login','num_compromised','num_file_creations','num_access_files','wrong_fragment',
                  'root_shell','num_failed_logins','num_shells','num_outbound_cmds','urgent','su_attempted',
                  'num_root','land','is_host_login'], axis=1)
"""

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Some variables
NUM_CLUSTERS = 4
NUM_ITER = 500

print("\n데이터 호출")
data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
label = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_label.csv")
train_total = pd.concat([data, label], axis=1)
normal_index = train_total[(train_total['Label'] == 1) == False].index
train_total = train_total.loc[normal_index]
print(list(set(train_total['Label'])))

X = train_total.drop(['Label'],axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)
#X = X.to_numpy()

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
  #print('Iteration: ', iter)
  #print('Inertia:', km.inertia_)
  cc = km.cluster_centers_.tolist()
  #print('Centroids:', cc)
  inertia = km.inertia_
  cents = km.cluster_centers_

  cents_list.append(cents)
  inert_list.append(inertia)

# Get best centroids to use for full clustering
best_cents = cents_list[inert_list.index(min(inert_list))]
print("\nbest centroids to use for full clustering")
print(best_cents.tolist())