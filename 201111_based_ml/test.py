'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

labels = pd.DataFrame(iris.target)
labels.columns=['labels']
data = pd.DataFrame(iris.data)
data.columns=['Sepal length','Sepal width','Petal length','Petal width']
data = pd.concat([data,labels],axis=1)

feature = data[['Sepal length','Sepal width','Petal length','Petal width']]

model = TSNE(learning_rate=100, n_components=3)
transformed = model.fit_transform(feature)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = transformed[:,0]
y = transformed[:,1]
z = transformed[:,2]

img = ax.scatter(x, y, x, c=labels)
plt.show()
'''

'''
from pandas.plotting import scatter_matrix
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

labels = pd.DataFrame(iris.target)
labels.columns=['labels']
data = pd.DataFrame(iris.data)
data.columns=['Sepal length','Sepal width','Petal length','Petal width']
data = pd.concat([data,labels],axis=1)

feature = data[['Sepal length','Sepal width','Petal length','Petal width']]

model = TSNE(learning_rate=100, n_components=3)
transformed = model.fit_transform(data)
t_data = pd.DataFrame(transformed, columns=['x1', 'x2', 'x3'])
scatter_matrix(t_data, alpha=0.2, figsize=(10, 10), diagonal='kde', c=data['labels'])

plt.show()
'''

'''
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10)
y = np.random.rand(10)

fig, ax = plt.subplots(nrows=4, ncols=3, figsize=(8, 6))

# ax is a 2d array with shape (4, 3), it can be sliced just like a numpy array
for row in range(4):
    for col in range(3):
        ax[row][col].scatter(x, y, c=y)
plt.show()
'''

from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from yellowbrick.contrib.classifier import DecisionViz

iris = datasets.load_iris()

labels = pd.DataFrame(iris.target)
labels.columns=['labels']
data = pd.DataFrame(iris.data)
data.columns=['Sepal length','Sepal width','Petal length','Petal width']
data = pd.concat([data,labels],axis=1)
data_sp = data[['Sepal length','Sepal width','labels']]

X = StandardScaler().fit_transform(data_sp.drop(['labels'],axis=1))
X_train, X_test, y_train, y_test = tts(X, data_sp['labels'], test_size=.4, random_state=42)

viz = DecisionViz(KNeighborsClassifier(3), title="Nearest Neighbors",
                  features=['Feature One', 'Feature Two'],
                  classes=["0","1","2"])

viz.fit(X_train, y_train)
viz.draw(X_test, y_test)
viz.show()