"""
  - sample size as a ratio of our full dataset
  - random state for reproducibility
  - number of clusters (k) for our dataset
  - number of iterations (n) for our k-means algorithm
  - number of attempts at finding our best chance initial centroids while clustering on our sample dataset

"""

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# target은 x_train의 예측 label / labels는 x_train의 실제 label
def matrics_function(target, labels):
  species = np.chararray(target.shape, itemsize=150)
  for i in range(len(target)):
    if target[i] == 0:
      species[i] = 'setosa'
    elif target[i] == 1:
      species[i] = 'versicolor'
    elif target[i] == 2:
      species[i] = 'virginica'

  df = pd.DataFrame({'labels': labels, 'species': species})
  ct = pd.crosstab(df['labels'], df['species'])

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
RANDOM_STATE = 42
NUM_CLUSTERS = 2
NUM_ITER = 100

print(color.BOLD+"\n데이터 호출"+color.END)
data = pd.read_csv("dataset/Unknown_data.csv")
#data = data.sample(frac=0.1, random_state=43)
y = data['Label']
X = data.drop(['Label'], axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#k-means 학습 수행
cents_list = []
inert_list = []

km = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1, n_init=1)
km.fit(X_train)
inertia = km.inertia_
cents = km.cluster_centers_
cents_list.append(cents)
inert_list.append(inertia)

print(color.BOLD+"\nInitial centroid 찾기"+color.END)
for iter in range(NUM_ITER):
  km = KMeans(n_clusters=NUM_CLUSTERS, init=cents, max_iter=1, n_init=1)
  km.fit(X_train)
  #print('Iteration: ', iter)
  #print('Inertia:', km.inertia_)
  cc = km.cluster_centers_.tolist()
  print('Centroids:', cc)
  inertia = km.inertia_
  cents = km.cluster_centers_

  cents_list.append(cents)
  inert_list.append(inertia)

# Get best centroids to use for full clustering
best_cents = cents_list[inert_list.index(min(inert_list))]
print("\nbest centroids to use for full clustering")
print(best_cents.tolist())