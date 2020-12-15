import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score,f1_score
from sklearn.model_selection import train_test_split

class color:
   BOLD = '\033[1m'
   END = '\033[0m'

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

def labeling(y):
    label = y.tolist()
    for i in range(len(label)):
        if label[i] == 'normal':
            label[i] = 1
        else:
            label[i] = -1
    return label

def data_extraction(test_data, test_label, df):
    test_data['predict'] = df['predict']
    test_data['actual'] = test_label['actual']
    anomaly_finish = test_data.loc[test_data[(test_data['predict'] == 1) == False].index]
    anomaly_finish = anomaly_finish.drop(['predict'], axis=1)
    return anomaly_finish

for i in range(1,11,1):
    print(color.BOLD+"\nfrac 값 : "+str(round((i*0.1),1))+color.END)
    # 1차 실험은 dos를 unknown으로 정의하고 실험 수행
    data = pd.read_csv("F:/data/KDD99/NSL-KDD/train_test/Train_data.csv")
    train_data = data.loc[data[(data['actual'] == 'normal') == True].index]
    train_data = train_data.sample(frac=round((i*0.1),1), random_state=42)
    y = train_data['actual']
    train_data = train_data.drop(['actual'], axis=1)

    std_scaler = StandardScaler()
    fitted_train = std_scaler.fit(train_data)
    x_train = std_scaler.transform(train_data)
    #x_train = train_data.to_numpy()

    y = labeling(y)
    y_train = np.array(y)

    test_data = pd.read_csv("F:/data/KDD99/NSL-KDD/train_test/Test_data.csv")
    test_label = test_data['actual']
    y_test = test_data['actual']
    y_test = labeling(y_test)
    y_test = np.array(y_test)

    test_data = test_data.drop(['actual'], axis=1)
    std_scaler = StandardScaler()
    fitted_test = std_scaler.fit(test_data)
    x_test = std_scaler.transform(test_data)
    #x_test = test_data.to_numpy()

    print("\nOne-class SVM")
    ocs = OneClassSVM(kernel="linear", gamma='auto')
    ocs.fit(x_train)
    ocs_pred = ocs.predict(x_test)
    df_ocs = pd.DataFrame(data=y_test, columns=['actual'])
    df_ocs['predict'] = ocs_pred
    ocs_result = scoring(df_ocs)
    print(ocs_result)

    print("\nIsolation Forest")
    iforset = IsolationForest(max_samples=100, contamination = 0.1, random_state=42)
    iforset.fit(x_train)
    iforse_pred = iforset.predict(x_test)
    df_iforse = pd.DataFrame(data=y_test, columns=['actual'])
    df_iforse['predict'] = iforse_pred
    iforse_result = scoring(df_iforse)
    print(iforse_result)

    print("\nLocal Outlier Factor")
    lof = LocalOutlierFactor(n_neighbors=15)
    lof.fit(x_train)
    lof_pred = lof.fit_predict(x_test)
    df_lof = pd.DataFrame(data=y_test, columns=['actual'])
    df_lof['predict'] = lof_pred
    lof_result = scoring(df_lof)
    print(lof_result)

#anomaly_finish = data_extraction(test_data=test_data,test_label=test_label,df=df_iforse)