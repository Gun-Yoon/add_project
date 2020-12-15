import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
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

def anomaly_test(train_data, train_label, test_data, test_label):
    train_data = train_data
    train_label = train_label
    train_total = pd.concat([train_data, train_label], axis=1)
    normal_index = train_total[(train_total['Label'] == 1) == True].index
    train_total = train_total.loc[normal_index]
    test_data = test_data
    test_label = test_label
    test_label = labeling(test_label)

    train_total = train_total.drop(['Label'], axis=1)
    train_total = train_total.sample(frac=0.2, random_state=42)

    print("\nOne-class SVM")
    ocs = OneClassSVM(kernel="linear", gamma='auto')
    ocs.fit(train_total)
    ocs_pred = ocs.predict(test_data)
    df_ocs = pd.DataFrame(data=(test_label['Label']).to_numpy(), columns=['actual'])
    df_ocs['predict'] = ocs_pred
    ocs_result = scoring(df_ocs)
    print(ocs_result)

    print("\nIsolation Forest")
    iforset = IsolationForest(max_samples=100, contamination = 0.1, random_state=42)
    iforset.fit(train_total)
    iforse_pred = iforset.predict(test_data)
    df_iforse = pd.DataFrame(data=(test_label['Label']).to_numpy(), columns=['actual'])
    df_iforse['predict'] = iforse_pred
    iforse_result = scoring(df_iforse)
    print(iforse_result)

    print("\nLocal Outlier Factor")
    lof = LocalOutlierFactor(n_neighbors=15)
    lof.fit(train_total)
    lof_pred = lof.fit_predict(test_data)
    df_lof = pd.DataFrame(data=(test_label['Label']).to_numpy(), columns=['actual'])
    df_lof['predict'] = lof_pred
    lof_result = scoring(df_lof)
    print(lof_result)