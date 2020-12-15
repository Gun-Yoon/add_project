import pandas as pd
from pyarc import CBA,TransactionDB
from sklearn.model_selection import train_test_split

print("")
print("Misuse Data 적용")
Misuse_data = pd.read_csv('F:/data/KDD99/NSL-KDD/train_test/Train_data.csv')
Misuse_data = Misuse_data.loc[Misuse_data[(Misuse_data['actual'] == 'normal') == False].index]
Misuse_data = Misuse_data.loc[Misuse_data[(Misuse_data['actual'] == 'dos') == False].index]
Misuse_data = Misuse_data.drop(['rerror_rate','duration','logged_in','dst_host_srv_rerror_rate','dst_bytes',
                                'srv_rerror_rate','hot','is_guest_login','num_compromised','num_file_creations',
                                'num_access_files','wrong_fragment','root_shell','num_failed_logins','num_shells',
                                'num_outbound_cmds','urgent','su_attempted','num_root','land','is_host_login'], axis=1)

test_data = pd.read_csv('F:/data/KDD99/NSL-KDD/train_test/Test_data.csv')
test_data = test_data.drop(['rerror_rate','duration','logged_in','dst_host_srv_rerror_rate','dst_bytes',
                                'srv_rerror_rate','hot','is_guest_login','num_compromised','num_file_creations',
                                'num_access_files','wrong_fragment','root_shell','num_failed_logins','num_shells',
                                'num_outbound_cmds','urgent','su_attempted','num_root','land','is_host_login'], axis=1)

print("Misuse Data Size : %s"%str(Misuse_data.shape))

rules = []
def rule_mining(Misuse_data):
    txns_train = TransactionDB.from_DataFrame(Misuse_data, target="actual")
    #print(len(test_data))

    print("\nAssociation Rule Generation")
    cba = CBA(support=0.3)
    cba.fit(txns_train)

    print("\nRULES : ({})".format(len(cba.clf.rules)))
    for i in cba.clf.rules:
        print(i)
        rules.append(i)

def r2l_u2r_data(Misuse_data):
    Misuse_data = Misuse_data.loc[Misuse_data[(Misuse_data['actual'] == 'probe') == False].index]
    return Misuse_data

data_r2l_u2r = r2l_u2r_data(Misuse_data)

rule_mining(data_r2l_u2r)

txns_train = TransactionDB.from_DataFrame(Misuse_data, target="actual")
txns_test = TransactionDB.from_DataFrame(test_data)
# print(len(test_data))

print("\nAssociation Rule Generation")
cba = CBA(support=0.1, algorithm='m2')
cba.fit(txns_train)

for i in range(len(rules)-2):
    print(type(cba.clf.rules))
    cba.clf.rules.insert(0,rules[i])

print("\nRULES : ({})".format(len(cba.clf.rules)))
for i in cba.clf.rules:
    print(i)
#print("\nPredict Rules")
#print(cba.predict_matched_rules(txns_test))

print("\nTarget_class")
print(cba.target_class)

predict, actual = cba.predict_actual(txns_test)
df = pd.DataFrame(data=predict, columns=['predict'])
df['actual'] = actual
df.to_csv('F:/data/KDD99/NSL-KDD/train_test/misuse_test.csv', index=False)

df = df.loc[df[(df['actual'] == 'normal') == False].index]
df = df.loc[df[(df['actual'] == 'dos') == False].index]
print(list(set(df['actual'])))

accuracy = cba.rule_model_accuracy(txns_test)
print("")
print(accuracy)