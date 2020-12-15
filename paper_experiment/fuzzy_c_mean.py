from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from fcmeans import FCM
import numpy as np
import pandas as pd

def scoring(df, NUM_CLUSTERS):
    accuracy = accuracy_score(df['actual'], df['predict'])
    Precision = precision_score(df['actual'], df['predict'], average=None)
    Precision = sum(Precision) / NUM_CLUSTERS
    Recall = recall_score(df['actual'], df['predict'], average=None)
    Recall = sum(Recall) / NUM_CLUSTERS
    F1 = f1_score(df['actual'], df['predict'], average=None)
    F1 = sum(F1) / NUM_CLUSTERS
    score_list = [accuracy,F1,Precision,Recall]
    return score_list

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

# 1차 실험은 dos를 unknown으로 정의하고 실험 수행
train = pd.read_csv("F:/data/KDD99/NSL-KDD/train_test/Train_data.csv")
train = train.loc[train[(train['actual'] == 'normal') == False].index]
train = train.loc[train[(train['actual'] == 'dos') == False].index]
#data = pd.read_csv("F:/data/KDD99/NSL-KDD/train_test/anomaly.csv")
#test_data = data.drop(['actual'],axis=1)
#print(test_data.shape)
#label = data['actual']
#le_test = LabelEncoder().fit(label)
#print("Test Class : ", le_test.classes_)
#test_label = le_test.transform(label)

NUM_CLUSTERS = 3
best_cent = [[30266.000000000004, 5.820766091346741e-11, 703506507.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.734723475976807e-18, 0.0, 0.0, 0.0, 8.673617379884035e-19, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3333333333333428, 1.333333333333334, 0.0, 6.938893903907228e-18, 0.9999999999999999, 1.0, 1.0, 0.0, 0.0, 255.0, 1.3333333333333357, 0.003333333333333355, 0.55, 1.0, 0.0, 6.938893903907228e-18, 0.0, 0.9999999999999999, 1.0], [1939.1381537492114, 73983.32514177694, 6440.607199117774, 0.0, 0.0, 0.0003150598613736575, 0.6603654694391943, 0.004804662885948329, 0.0817580340264651, 0.011578449905482227, 0.0025204788909892525, 7.876496534341364e-05, 0.012523629489603014, 0.0075614366729679135, 0.0008664146187775735, 0.0008664146187775662, 0.0, 0.0, 0.02473219911783241, 70.8609010712035, 10.237240075614368, 0.04374054820415873, 0.03768352236925019, 0.40510318210459995, 0.4117186515437933, 0.7215327662255828, 0.23630513547574042, 0.27668084436042845, 140.3846880907372, 42.26244486452424, 0.4190114996849401, 0.37006458727158165, 0.6472841839949589, 0.17904851921865142, 0.04294580970384372, 0.037756773787019485, 0.3617060491493383, 0.4081947069943288], [27227.500000000004, 965606922.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15.0, 1.5, 0.1975, 0.1675, 0.8025, 0.8325, 0.7625, 0.0975, 0.0, 121.5, 1.5, 0.010000000000000009, 0.10249999999999998, 0.10250000000000004, 0.0, 0.045, 0.16749999999999998, 0.06, 0.8325]]
best_cents = np.array(best_cent)

train_y = train['actual']
le = LabelEncoder().fit(train_y)
print("Train Class : ", le.classes_)
train_y = le.transform(train_y)

X = train.drop(['actual'],axis=1)
print(X.shape)
#std_scaler = StandardScaler()
#fitted = std_scaler.fit(X)
#X = std_scaler.transform(X)
X = X.to_numpy()

x_train, x_test, y_train, y_test =train_test_split(X, train_y, test_size=0.2, random_state=42)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=NUM_CLUSTERS, first_center=best_cents, max_iter=1000, random_state=42)
fcm.fit(x_train)
probability = fcm.predict(x_test)
df_fcm = pd.DataFrame(data=y_test, columns=['actual'])
df_fcm['predict'] = probability[:,3]
df_fcm.to_csv('F:/data/KDD99/NSL-KDD/train_test/test.csv', index=False)
fcm_result = scoring(df_fcm, NUM_CLUSTERS)
print(fcm_result)