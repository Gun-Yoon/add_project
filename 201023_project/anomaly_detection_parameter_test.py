import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

anomaly_data = pd.read_csv('F:/data/ADD/201023_data/anomaly_data.csv')  #레코드 수 : 2,856,000
anomaly_data = anomaly_data.drop(['Unnamed: 0'], axis=1)
unknown_data = pd.read_csv('F:/data/ADD/201023_data/Unknown_data.csv')

temp_adata = unknown_data[unknown_data['Label']=='Benign']
anomaly_data = pd.concat([temp_adata, anomaly_data], axis=0)    #3,286,000

unknown_label = pd.read_csv('F:/data/ADD/201023_data/unknown_label.csv')    # Benign은 '1', Attack은 '-1' 설정
unknown_data = unknown_data.drop(['Label'],axis=1)
n_list = [5000, 10000, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000]

for num in n_list:
    temp_data = anomaly_data.sample(n=num, random_state=42)

    print("\nData Construction")
    train_data = temp_data.drop(['Label'], axis=1)
    print("Data Shape : %s"%str(train_data.shape))

    # 데이터 분할
    train, test = train_test_split(train_data, test_size=0.25, random_state=42, shuffle=True)

    print("\nIsolation Forest")
    iforset = IsolationForest(max_samples=100, contamination=0.1, random_state=42)
    iforset.fit(train)
    iforset_pred_test = iforset.predict(test)
    iforse_pred = iforset.predict(unknown_data)

    for num in range(len(iforse_pred)):
        if iforse_pred[num] == unknown_label['Label'][num]:
            iforse_pred[num] = 1
        else:
            iforse_pred[num] = 0

    print("테스트 정확도:", list(iforset_pred_test).count(1) / iforset_pred_test.shape[0])
    print("예측 정확도:", list(iforse_pred).count(1) / iforse_pred.shape[0])
