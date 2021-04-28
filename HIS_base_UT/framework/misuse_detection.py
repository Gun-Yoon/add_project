import pandas as pd
from pyarc import CBA,TransactionDB
from sklearn.metrics import accuracy_score

def misuse(train_df, test_df):
    print("\nMisuse Data")
    train = train_df.copy()
    test = test_df.copy()

    train = train[(train['Label'] != 'Benign') == True]

    txns_train = TransactionDB.from_DataFrame(train, target="Label")
    txns_test = TransactionDB.from_DataFrame(test)

    print("Association Rule Generation")
    cba = CBA(support=0.01, confidence=0.01)
    cba.fit(txns_train)

    predict = cba.predict(txns_test)
    test['predict'] = predict

    return test