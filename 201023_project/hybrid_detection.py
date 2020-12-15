def rule_set(record):
    define_rule = [0,0,0,0,0]
    define_name = ['DDOS attack-HOIC','DDoS attacks-LOIC-HTTP','FTP-BruteForce','Bot','Infilteration']

    if record['Init Fwd Win Byts'] >= 32719.5 and record['Init Fwd Win Byts'] <= 32753:
        define_rule[0] = define_rule[0] + 1
    elif record['Subflow Bwd Byts'] >= 933 and record['Subflow Bwd Byts'] <= 936.5:
        define_rule[0] = define_rule[0] + 1
    elif record['Init Fwd Win Byts']>=8191 and record['Init Fwd Win Byts']<=8283:
        define_rule[1] = define_rule[1] + 1
    #elif record['Dst Port']>=20.5 and record['Dst Port']<=21.5 and\
    #        record['Init Fwd Win Byts']>=26558 and record['Init Fwd Win Byts']<=27433.5:
    #    define_rule[2] = define_rule[2] + 1
    elif record['Fwd Pkts/s']>=464286 and record['Fwd Pkts/s']<=550000:
        define_rule[2] = define_rule[2] + 1
    elif record['Bwd Header Len']<= 4 and record['Dst Port']>=8074 and record['Dst Port']<=8080.5:
        define_rule[3] = define_rule[3] + 1
    #elif record['Fwd Header Len']>=70 and record['Fwd Header Len']<=76 and\
    #        record['Dst Port']>=8074 and record['Dst Port']<=8080.5:
    #    define_rule[3] = define_rule[3] + 1
    #elif record['Bwd Pkt Len Max']>=111.5 and record['Bwd Pkt Len Max']<=112.5 and\
    #        record['TotLen Bwd Pkts']>=128.5 and record['TotLen Bwd Pkts']<=129.5:
    #    define_rule[3] = define_rule[3] + 1
    #elif record['Init Fwd Win Byts']>=8191 and record['Init Fwd Win Byts']<=8283 and\
    #        record['Dst Port']>=8074 and record['Dst Port']<=8080.5:
    #    define_rule[3] = define_rule[3] + 1
    elif record['Dst Port']>=8074 and record['Dst Port']<=8080.5:
        define_rule[3] = define_rule[3] + 1
    elif record['Fwd Header Len']>=4 and record['Fwd Header Len']<=38:
        define_rule[4] = define_rule[4] + 1

    index_num = define_rule.index(max(define_rule))

    if define_rule[0] == define_rule[1] == define_rule[2] == define_rule[3] == define_rule[4] == 0:
        return 'unknown'
    else:
        return define_name[index_num]

import pandas as pd

unknown_data = pd.read_csv('F:/data/ADD/201023_data/Unknown_data.csv')
label_list = []

print("\n규칙 기반 탐지 수행")
for record in range(len(unknown_data)):
    temp_label = rule_set(unknown_data.loc[record])
    label_list.append(temp_label)

#misuse_result = pd.DataFrame(data=label_list, columns=['Label'])
#misuse_result.to_csv('F:/data/ADD/201023_data/misuse_result.csv', index=False)

print("\n이상 탐지 수행")
from sklearn.model_selection import train_test_split
from sklearn import svm

unknown_data_no = unknown_data.drop(['Label'], axis=1)

anomaly_data = pd.read_csv('F:/data/ADD/201023_data/Unknown_data.csv')
unknown_label = pd.read_csv('F:/data/ADD/201023_data/unknown_label.csv')    # Benign은 '1', Attack은 '-1' 설정

anomaly_data = anomaly_data[anomaly_data['Label']=='Benign']
anomaly_data = anomaly_data.sample(n=50000, random_state=150)

print("\nData Construction")
anomaly_data = anomaly_data.drop(['Label'], axis=1)
print("Data Shape : %s"%str(anomaly_data.shape))

# 데이터 분할
train, test = train_test_split(anomaly_data, test_size=0.2, random_state=150)

print("\nOne-class SVM")
ocs = svm.OneClassSVM(kernel="linear")
ocs.fit(train)
ocs_pred_test = ocs.predict(test)
ocs_pred = ocs.predict(unknown_data_no)

for num in range(len(ocs_pred)):
    if ocs_pred[num] == unknown_label['Label'][num]:
        ocs_pred[num] = 1
    else:
        ocs_pred[num] = 0

print("테스트 정확도:", list(ocs_pred_test).count(1)/ocs_pred_test.shape[0])
print("예측 정확도:", list(ocs_pred).count(1)/ocs_pred.shape[0])