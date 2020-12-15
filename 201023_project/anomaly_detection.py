import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

anomaly_data = pd.read_csv('F:/data/ADD/201023_data/anomaly_data.csv')  #레코드 수 : 285,6000
unknown_data = pd.read_csv('F:/data/ADD/201023_data/Unknown_data.csv')
unknown_label = pd.read_csv('F:/data/ADD/201023_data/unknown_label.csv')    # Benign은 '1', Attack은 '-1' 설정

temp_adata = unknown_data[unknown_data['Label']=='Benign']
temp_adata = temp_adata.sample(n=50000, random_state=150)
anomaly_data = anomaly_data.sample(n=50000, random_state=150)
anomaly_data = pd.concat([temp_adata, anomaly_data], axis=0)

unknown_data = unknown_data.drop(['Label'],axis=1)

print("Data Construction")
train_data = anomaly_data.drop(['Label','Unnamed: 0'], axis=1)
#train_data = anomaly_data.drop(['Label'], axis=1)
print("Data Shape : %s"%str(train_data.shape))
train_data_label = anomaly_data['Label']

# 데이터 분할
train, test = train_test_split(train_data, test_size=0.2, random_state=150)

# fit the model
print("\nOne-class SVM")
ocs = svm.OneClassSVM(kernel="linear", gamma='auto')
ocs.fit(train)
ocs_pred_test = ocs.predict(test)
ocs_pred = ocs.predict(unknown_data)

for num in range(len(ocs_pred)):
    if ocs_pred[num] == unknown_label['Label'][num]:
        ocs_pred[num] = 1
    else:
        ocs_pred[num] = 0

print("테스트 정확도:", list(ocs_pred_test).count(1)/ocs_pred_test.shape[0])
print("예측 정확도:", list(ocs_pred).count(1)/ocs_pred.shape[0])
#pred = clf.predict(unknown_data)

#df = pd.DataFrame(data=pred, columns=['Label'])
#df.to_csv('F:/data/ADD/201023_data/anomaly_result1.csv', index=False)

print("\nIsolation Forest")
iforset = IsolationForest(max_samples=100, contamination = 0.1, random_state=42)
iforset.fit(train)
iforset_pred_test = iforset.predict(test)
iforse_pred = iforset.predict(unknown_data)

for num in range(len(iforse_pred)):
    if iforse_pred[num] == unknown_label['Label'][num]:
        iforse_pred[num] = 1
    else:
        iforse_pred[num] = 0

print("테스트 정확도:", list(iforset_pred_test).count(1)/iforset_pred_test.shape[0])
print("예측 정확도:", list(iforse_pred).count(1)/iforse_pred.shape[0])

from sklearn.neighbors import LocalOutlierFactor

print("\nLocal Outlier Factor")
lof = LocalOutlierFactor(n_neighbors=15)
lof.fit(train)
lof_pred_test = lof.fit_predict(test)
lof_pred = lof.fit_predict(unknown_data)

for num in range(len(lof_pred)):
    if lof_pred[num] == unknown_label['Label'][num]:
        lof_pred[num] = 1
    else:
        lof_pred[num] = 0

print("테스트 정확도:", list(lof_pred_test).count(1)/lof_pred_test.shape[0])
print("예측 정확도:", list(lof_pred).count(1)/lof_pred.shape[0])