from scipy.spatial import distance
import pandas as pd
import numpy as np

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

benign_bounderies = pd.read_csv("dataset/benign_bounderies.csv")
attack_bounderies = pd.read_csv("dataset/attack_bounderies.csv")
diff_data = pd.read_csv("dataset/different_data.csv")
dif_label = pd.read_csv("dataset/different_data_label.csv")

benign_distance = pd.DataFrame(index=range(0,len(benign_bounderies)), columns=['distance'])
attack_distance = pd.DataFrame(index=range(0,len(attack_bounderies)), columns=['distance'])
dif_prelist = []
print("\n")
print(diff_data.shape)

print(color.RED+"\nEuclidean distance measure between benign/attack boundaries and invalid data"+color.END)
for j in range(len(diff_data)):
    for i in range(len(benign_bounderies)):
        benign_distance.loc[i] = distance.euclidean(benign_bounderies.loc[i],diff_data.loc[j])

    for i in range(len(attack_bounderies)):
        attack_distance.loc[i] = distance.euclidean(attack_bounderies.loc[i],diff_data.loc[j])

    if benign_distance['distance'].min() > attack_distance['distance'].min():
        print("{0}번째 Invalid Data => Attack / {1} : {2}".format(j,benign_distance['distance'].min(),attack_distance['distance'].min()))
        dif_prelist.append(1)
    else:
        print("{0}번째 Invalid Data => Benign / {1} : {2}".format(j,benign_distance['distance'].min(),attack_distance['distance'].min()))
        dif_prelist.append(0)

dif_predict = pd.DataFrame(data=dif_prelist, columns=['predict'])
print("\n")

from sklearn.metrics import accuracy_score
print(accuracy_score(dif_label, dif_predict))