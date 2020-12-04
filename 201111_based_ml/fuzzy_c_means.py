from fcmeans import FCM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import homogeneity_score, adjusted_mutual_info_score, accuracy_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def check_different(df):
  dif_indexes = df[(df['pre_class'] != df['class']) == True]
  return dif_indexes

def check_match(df):
  dif_indexes = df[(df['pre_class'] == df['class']) == True]
  return dif_indexes

data = pd.read_csv("dataset/Unknown_data.csv")
X = data.drop(['Label'], axis=1)
col = X.columns
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)

y = data['Label']
le = LabelEncoder().fit(y)
print("Class to number : ",le.classes_)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

centers = [[0.8780548390411661, 0.9434844754118773, 0.08570221749085585, 0.9441549808772682, 0.9508694103254853,
            0.8535406951590411, 0.8905401456770801, 0.39582444741022377, 0.3667930775720254, 0.3952155401243918,
            0.0032622049637311616, 0.9069492338739097, 0.7504700387230853, -0.13242523171180198, 0.9508694103254853,
            0.8905401456770801, 0.9434844754118773, 0.08570221749085585, 0.11618334316338697],
           [-0.9412667613865507, -1.0119779944751732, -0.09306364705246235, -1.0126546024310055, -1.019845635380197,
            -0.9157598569900075, -0.9550845402220292, -0.426040107421912, -0.3949314190439888, -0.4252499970085256,
            -0.004498061858428147, -0.9732354941599739, -0.8057760992662832, 0.14348119625617362, -1.019845635380197,
            -0.9550845402220292, -1.0119779944751732, -0.09306364705246235, -0.12494198981745376]]

# fit the fuzzy-c-means
fcm = FCM(n_clusters=2, first_center=centers, max_iter=100)
fcm.fit(X_train)

# outputs
fcm_centers = fcm.centers   # 첫번째는 'Bengin' cetroid, 두번쨰는 'attack' centroid
fcm_labels  = fcm.u.argmax(axis=1)
probability = fcm.predict(X_test)

result_df = pd.DataFrame(data=probability, columns=[0,1,'pre_class'])
result_df['class'] = y_test
print(color.BOLD+"Result"+color.END)
print(result_df.head())

print(color.BOLD+"\nScoring"+color.END)
h_score = homogeneity_score(result_df['class'], result_df['pre_class'])
ar_score = adjusted_rand_score(result_df['class'], result_df['pre_class'])
ami_socre = adjusted_mutual_info_score(result_df['class'], result_df['pre_class'])
print("Homogeneity_score : %.4f" %h_score)
print("Adjusted_rand_score : %.4f" %ar_score)
print("Adjusted_mutual_info_score : %.4f" %ami_socre)
print('Accuracy : %0.4f'%accuracy_score(result_df['class'], result_df['pre_class']))
Precision = precision_score(result_df['class'], result_df['pre_class'], average=None)
Precision = sum(Precision)/2
print('Precision : %0.4f'%Precision)
Recall = recall_score(result_df['class'], result_df['pre_class'], average=None)
Recall = sum(Recall)/2
print('Recall : %0.4f'%Recall)
F1 = f1_score(result_df['class'], result_df['pre_class'], average=None)
F1 = sum(F1)/2
print('F1-score : %0.4f'%F1)

print(color.BOLD+"\nValidate records in cluster(find invalid record)"+color.END)
dif_df = check_different(result_df)
#dif_df.to_csv('probability_data.csv', index=False)
print(dif_df.head())

#probability threshold(pt)를 기준으로 부합한 데이터 추출
# 0.4 <= pt <= 0.6
print(color.BOLD+"\nCheck probability threshold"+color.END)
for i in dif_df.index:
    if dif_df.loc[i][0] <= 0.4 or dif_df.loc[i][0] >= 0.6:
        dif_df = dif_df.drop([i])
print(dif_df.head(10))

print(color.BOLD+"\nSave invalid cluster"+color.END)
test_data = pd.DataFrame(data=X_test, columns=col)
invalid_data = test_data.loc[dif_df.index.values]
invalid_data.to_csv('dataset/different_data.csv', index=False)
test_data_label = pd.DataFrame(data=y_test, columns=['class'])
invalid_data_label = test_data_label.loc[dif_df.index.values]
invalid_data_label.to_csv('dataset/different_data_label.csv', index=False)
print(invalid_data.head(10))

print(color.BOLD+"\nCheck correct record"+color.END)
corr_df = check_match(result_df)
df_benign = corr_df[(corr_df['class'] == 0) == True]
df_attack = corr_df[(corr_df['class'] == 1) == True]

benign_data = test_data.loc[df_benign.index.values]
attack_data = test_data.loc[df_attack.index.values]
benign_data.to_csv('dataset/df_benign.csv', index=False)
attack_data.to_csv('dataset/df_attack.csv', index=False)
print("Benign data set")
print(benign_data.head(10))
print("\nAttack data set")
print(attack_data.head(10))

print(color.BOLD+"\nCheck centroid vector"+color.END)
print(fcm_centers.tolist())