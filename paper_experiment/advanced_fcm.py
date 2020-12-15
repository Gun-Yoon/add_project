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

def check_different(df):
  dif_indexes = df[(df['predict'] != df['actual']) == True]
  return dif_indexes

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
best_cent = [[-0.17577644245927798, -0.003820964125900931, -0.013536714330214545, 0.0, 0.0, 0.17031899518090288, 1.8639817784163883, -0.0092000922884453, 3.3486410427097963, 0.3115489290842178, 0.5906848384403881, 0.10429181503334062, 0.2341501069323052, 0.33128646869059497, 0.27830631421639884, 0.31828289930380993, 0.0, 0.0, 1.8712550159665058, -0.4573527570393958, -0.49550312229779214, -0.23269779060142284, -0.1783679371394946, -0.8456692382244435, -0.8331912297403684, 0.6205666986159264, -0.535224896782363, -0.5884565747479275, -0.3902110724557219, 0.026670477273263316, 0.5694201553893814, -0.8084703697788395, -0.13190008955347848, -0.32682168605975964, -0.21710167327233407, -0.18280078439462602, -0.8161492882104584, -0.8267345271039639], [-0.26320342356727255, -0.020478152372221788, -0.012315005284794593, 0.0, 0.0, -0.014490280960124727, -0.15982123305074378, -0.044009817607192914, -0.29754107713495487, -0.026505743005713067, -0.050253873672727864, -0.0088728664707618, -0.019920859870554017, -0.028184959666510235, -0.023677550948964888, -0.027078651038404074, 0.0, 0.0, -0.1592013321860959, -0.42485554072738907, 0.7723181953226834, -0.25578353013144894, -0.19748713543640073, -0.8555772265247162, -0.8371911948850915, 0.6156502453428548, -0.5794354244404715, 1.008676141926125, -0.9425197500267007, 0.8819292937137131, 1.0885472768488993, -0.891091041967137, 0.7602061519378381, 0.7810731033610439, -0.2908257453871856, -0.19870558978146424, -0.8673932847893018, -0.8357147858178295], [0.20805501585262806, 0.014766914211135443, 0.01050038318727254, 0.0, 0.0, -0.014490280960124766, -0.15772263333694375, 0.031878203615194306, -0.27611315940992515, -0.026505743005713032, -0.05025387367272783, -0.008872866470761838, -0.01992085987055378, -0.028184959666510356, -0.023677550948964652, -0.027078651038404043, 0.0, 0.0, -0.15920133218609722, 0.3608618487526107, -0.4647307197039515, 0.21110862423727467, 0.16280756209541952, 0.7158452267598511, 0.701282869274274, -0.5168391691362041, 0.4793973557505345, -0.6154148631505985, 0.7105524557227202, -0.6160895249361604, -0.8377574184966627, 0.7351375132584768, -0.5087317542185964, -0.49512203726591214, 0.23318731797418066, 0.16429237271182487, 0.7197930938048974, 0.6993272672306335]]
best_cents = np.array(best_cent)

train_y = train['actual']
le = LabelEncoder().fit(train_y)
print("Train Class : ", le.classes_)
train_y = le.transform(train_y)

X = train.drop(['actual'],axis=1)
col = X.columns
print(X.shape)
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)

x_train, x_test, y_train, y_test =train_test_split(X, train_y, test_size=0.2, random_state=42)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=NUM_CLUSTERS, first_center=best_cents, max_iter=1000, random_state=42)
fcm.fit(x_train)
probability = fcm.predict(x_test)
df_fcm = pd.DataFrame(data=probability, columns=['0','1','2','predict'])
df_fcm['actual'] = y_test
#df_fcm.to_csv('F:/data/KDD99/NSL-KDD/train_test/test.csv', index=False)
fcm_result = scoring(df_fcm, NUM_CLUSTERS)
print(fcm_result)

print(probability)

print(color.BOLD+"\nValidate records in cluster(find invalid record)"+color.END)
dif_data = check_different(df_fcm)
print(df_fcm.shape)
print(dif_data.shape)

print("\nCheck probability threshold : Threshold<0.5")
dif_df = dif_data
for i in dif_df.index:
    if dif_df.loc[i][0] >= 0.5 or dif_df.loc[i][1] >= 0.5 or dif_df.loc[i][2] >= 0.5:
        dif_df = dif_df.drop([i])
print(dif_df.shape)

print("\nSave invalid cluster")
test_data = pd.DataFrame(data=x_test, columns=col)
invalid_data = test_data.loc[dif_df.index.values]
test_data_label = pd.DataFrame(data=y_test, columns=['actual'])
invalid_data_label = test_data_label.loc[dif_df.index.values]
print(invalid_data.shape)

