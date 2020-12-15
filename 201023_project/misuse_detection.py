import pandas as pd
from pyarc import CBA,TransactionDB
from sklearn.model_selection import train_test_split

print("")
print("Misuse Data 적용")
Misuse_data = pd.read_csv('F:/data/ADD/201023_data/disc_attack_data.csv')  #disc_data/Known_attack_data
print("Misuse Data Size : %s"%str(Misuse_data.shape))

# 데이터 분할
train, test = train_test_split(Misuse_data, test_size=0.2, random_state=123)

txns_train = TransactionDB.from_DataFrame(train, target="Label")
txns_test = TransactionDB.from_DataFrame(test)

print("Association Rule Generation")
cba = CBA(support=0.3)
cba.fit(txns_train)
print(cba.fit(txns_train))

print("\nRULES : ({})".format(len(cba.clf.rules)))
for i in cba.clf.rules:
    print(i)

#print("\nPredict Rules")
#print(cba.predict_matched_rules(txns_test))

#print("\nTarget_class")
#print(cba.target_class)

accuracy = cba.rule_model_accuracy(txns_test)
print("")
print(accuracy)