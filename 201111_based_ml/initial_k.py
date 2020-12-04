import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn import datasets
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# Initial K calculate
data = pd.read_csv("dataset/Unknown_data.csv")
data = data.sample(n=10000, random_state=43)
y = data['Label']
X = data.drop(['Label'], axis=1)
#iris = datasets.load_iris()
#samples = iris.data
samples = X
num_clusters = list(range(1,16))	# K는 1 ~ 8사이의 정수입니다
inertias = []
#sil_coeff = []
# 각 K별로 모델을 생성하여 inertia를 측정합니다
for i in num_clusters:
    model = KMeans(n_clusters=i)
    model.fit(samples)
    label = model.labels_
    if i >= 2:
      #sil_coeff.append(silhouette_score(samples, label, metric='euclidean'))
      sil_coeff = silhouette_score(samples, label, metric='euclidean')
      print("For n_clusters={}, The Silhouette Coefficient is {}".format(i, sil_coeff))
    inertias.append(model.inertia_)
# K에 따른 inertia의 변화를 시각화합니다
plt.plot(num_clusters, inertias, '-o')
plt.xticks(np.arange(0, 15, step=1))
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()