import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score,f1_score

def scoring(df):
   tn, fp, fn, tp = confusion_matrix(df['actual'], df['predict']).ravel()
   accuracy = accuracy_score(df['actual'], df['predict'])
   Precision = precision_score(df['actual'], df['predict'], average=None)
   Precision = sum(Precision) / 2
   Recall = recall_score(df['actual'], df['predict'], average=None)
   Recall = sum(Recall) / 2
   F1 = f1_score(df['actual'], df['predict'], average=None)
   F1 = sum(F1) / 2
   score_list = [accuracy,Precision,Recall,F1,tn,fp,fn,tp]
   return score_list

def labeling(df):
    for i in range(len(df)):
        if df['Label'][i] == 1:
            pass
        else:
            df['Label'][i] = -1
    return df

print("\n데이터 호출")
train_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
train_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_label.csv")
train_anomaly = pd.concat([train_data, train_label], axis=1)
normal_index = train_anomaly[(train_anomaly['Label'] == 1) == True].index
train_anomaly = train_anomaly.loc[normal_index]
test_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_data.csv")
test_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_label.csv")
test_label_anomaly = labeling(test_label)

train_anomaly = train_anomaly.drop(['Label'], axis=1)
train_anomaly = train_anomaly.sample(frac=0.2, random_state=42)

print("\nIsolation Forest")
iforset = IsolationForest(max_samples=100, contamination = 0.1, random_state=42)
iforset.fit(train_anomaly)
iforse_pred = iforset.predict(test_data)
df_iforse = pd.DataFrame(data=(test_label_anomaly['Label']).to_numpy(), columns=['actual'])
df_iforse['predict'] = iforse_pred
iforse_result = scoring(df_iforse)
print(iforse_result)

test_data['predict'] = iforse_pred
test_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_label.csv")
test_data['actual'] = test_label['Label']
train_clustering = test_data.loc[test_data[(test_data['predict'] == 1) == False].index]
train_clustering = train_clustering.drop(['predict'],axis=1)
print(train_clustering.shape)
print(train_clustering.head())
#train_clustering.to_csv('F:/data/KDD99/NSL-KDD/anomaly_after_data.csv', index=False)