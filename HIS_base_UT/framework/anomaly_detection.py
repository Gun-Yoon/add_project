import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

def anomaly(train_df, test_df, threat):
    print("")
    print("Anomaly Detection")
    train = train_df.copy()
    test = test_df.copy()

    #학습 데이터 standardscaler
    train_label = train['Label'].tolist()
    train = train.drop(['Label'], axis=1)
    train_columns = train.columns

    std_scaler = StandardScaler()
    train = std_scaler.fit_transform(train)

    train = pd.DataFrame(data=train, columns=train_columns)
    train['Label'] = train_label
    #----------------------------

    #학습 데이터 standardscaler
    test_label = test['Label'].tolist()
    pre_label = test['predict'].tolist()
    test = test.drop(['Label','predict'], axis=1)
    test_columns = test.columns

    test = std_scaler.transform(test)

    test = pd.DataFrame(data=test, columns=test_columns)
    test['Label'] = test_label
    test['predict'] = pre_label
    #----------------------------

    train = train[(train['Label'] == 'Benign') == True]
    train = train.drop(['Label'], axis=1)

    clf = OneClassSVM(kernel='linear',gamma='auto',nu=0.1)
    clf.fit(train)

    temp_test = test[(test['predict'] == 'None') == True]
    temp_test = temp_test.drop(['Label','predict'], axis=1)

    predict = clf.predict(temp_test)

    temp_index = temp_test.index
    for id, pred in zip(temp_index, predict):
        test.predict[id] = pred

    test.loc[(test.predict == 1) == True, 'predict'] = 'Benign'
    test.loc[(test.predict == -1) == True, 'predict'] = threat

    return test