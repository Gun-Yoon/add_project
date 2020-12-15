"""
   dos : 0
   normal : 1
   probe : 2
   r2l : 3
   u2r : 4
   ohers : 5
"""

from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics import jaccard_score, adjusted_mutual_info_score, precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from fcmeans import FCM
import time
import numpy as np
import pandas as pd

def scoring(df, NUM_CLUSTERS):
   ars = adjusted_rand_score(df['actual'], df['predict'])
   mis = adjusted_mutual_info_score(df['actual'], df['predict'])
   jaccard = jaccard_score(df['actual'], df['predict'], average=None)
   jaccard = sum(jaccard) / NUM_CLUSTERS
   Precision = precision_score(df['actual'], df['predict'], average=None)
   Precision = sum(Precision) / NUM_CLUSTERS
   Recall = recall_score(df['actual'], df['predict'], average=None)
   Recall = sum(Recall) / NUM_CLUSTERS
   F1 = f1_score(df['actual'], df['predict'], average=None)
   F1 = sum(F1) / NUM_CLUSTERS
   score_list = [ars,jaccard,mis,F1,Precision,Recall]
   return score_list

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

# Some variables
NUM_CLUSTERS = 4

print(color.BOLD+"\n데이터 호출"+color.END)
train_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
train_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_label.csv")
train_total = pd.concat([train_data, train_label], axis=1)
normal_index = train_total[(train_total['Label'] == 1) == False].index
train_total = train_total.loc[normal_index]

y = train_total['Label']
le = LabelEncoder().fit(y)
print("Class to number : ",le.classes_)
y = le.transform(y)

X = train_total.drop(['Label'],axis=1)
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)
#X = X.to_numpy()

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

best_cents = [[-0.11931161083125921, -0.003468285624032891, -0.006358101166384696, -0.013160414170389578, -0.12330410267674015, -0.006744259863550918, -0.08892831276821966, -0.02229173026024981, -0.18599797571021862, -0.0741852622346487, -0.023368648299276613, -0.0041299401367450115, -0.009271153905966004, -0.013115218674899612, -0.01101880863088062, -0.012600725112407247, 0.0, 0.0, -0.07337886000629086, -0.6375102340635923, -0.2090323180146423, 0.7293390607275736, 0.7311093976483249, -0.508321769130241, -0.5094209598695919, -0.19697485097954143, 0.023469778877830468, -0.2547556963900531, 0.19830766834220795, -0.17623153468053876, -0.2826706269683591, -0.19532766780187574, -0.3515443481224053, -0.2563452292544116, 0.7238095434070183, 0.714753220911046, -0.5042113542238754, -0.5075007279643315], [-0.11932410993747923, -0.009638148529098223, -0.006366620269036628, -0.017524392920516076, -0.13177786439525555, -0.006744259863551143, -0.08928083744372672, -0.026132240809920142, -0.18768475491830183, -0.07418526223464819, -0.0233686482992767, -0.004129940136744979, -0.009271153905966065, -0.013115218674899766, -0.01101880863088082, -0.012600725112406848, 0.0, 0.0, -0.0733788600062899, 0.5288464934091278, -0.19453794032176597, 0.8289483110332465, 0.8265261493626211, -0.5186005997321961, -0.5167805969333562, -0.6401601341172284, -0.2065350337434794, -0.26192972634091216, 0.38985232310037465, -0.3603435025941647, -0.4432882883538646, -0.28079061730683713, -0.49745804548368144, -0.27208310943643754, 0.8329275434698432, 0.8341399835704456, -0.529170844766171, -0.513104271656942], [0.414350171122418, 0.025019382657634006, 0.021681584939091846, -0.017524392920516524, -0.10340415771762998, -0.006744259863550925, -0.08695331492625623, 0.0702670707548559, -0.16565106113486178, -0.0741852622346487, -0.02336864829927661, -0.004129940136745013, -0.009271153905966004, -0.013115218674899605, -0.011018808630880632, -0.01260072511240724, 0.0, 0.0, -0.07337886000629097, 0.08041513727013971, -0.25097580970022315, -1.1873553481242412, -1.1918076648648857, 1.8345631574018069, 1.8217476115671634, -0.09647952039038653, 0.7190829360081096, -0.2626933037648395, 0.2221854632196116, -0.44069541311147226, -0.4765416690818894, 1.0124588650827129, -0.01845601596742248, -0.1175007795555745, -1.1897138059508523, -1.1884417257401696, 1.7965851719103991, 1.8247284789058749], [-0.10206544878747482, -0.005672389558454066, -0.004940420361887496, 0.07429755209067011, 0.5545442659096838, 0.030672087203064826, 0.4027904150723208, -0.0023652659851225075, 0.8248616058202702, 0.33738569961408577, 0.10627781742617594, 0.01878247377481431, 0.04216409907537281, 0.0596464458698932, 0.05011222373366641, 0.057306590684379245, 0.0, 0.0, 0.33371827873034327, -0.4197909772009731, 0.9708564748601611, -1.2108133908420176, -1.2025341476155835, -0.49700101885635783, -0.4839841635985473, 1.7060316490396026, -0.46360151184010684, 1.1832682426770562, -1.3333720163243183, 1.507995621020523, 1.85739861995607, -0.3911253664071658, 1.5031092458096886, 1.0311747092509707, -1.2094850534984702, -1.2023615018934177, -0.43398827214715874, -0.49768996721797426]]
best_cents = np.array(best_cents)

# Optimized centroid
kmbest = KMeans(n_clusters=NUM_CLUSTERS, init=best_cents, max_iter=1000, n_init=1)
kmbest_start = time.time()
kmbest.fit(X)
kmbest_end = time.time()
predic_kmbest = kmbest.predict(x_test)
print(list(set(predic_kmbest)))
df_kmbest = pd.DataFrame(data=y_test, columns=['actual'])
df_kmbest['predict'] = predic_kmbest
kmbest_result = scoring(df_kmbest, NUM_CLUSTERS)
print(kmbest_result)

#Random centroid
kmrandom = KMeans(n_clusters=NUM_CLUSTERS, init='random', max_iter=1000, n_init=1)
kmrandom_start = time.time()
kmrandom.fit(X)
kmrandom_end = time.time()
predic_kmrandom = kmrandom.predict(x_test)
print(list(set(predic_kmrandom)))
df_kmrandom = pd.DataFrame(data=y_test, columns=['actual'])
df_kmrandom['predict'] = predic_kmrandom
kmrandom_result = scoring(df_kmrandom, NUM_CLUSTERS)
print(kmrandom_result)

# Random centroid
kmplus = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', max_iter=1000, n_init=1)
kmplus_start = time.time()
kmplus.fit(X)
kmplus_end = time.time()
predic_kmplus = kmplus.predict(x_test)
print(list(set(predic_kmplus)))
df_kmplus = pd.DataFrame(data=y_test, columns=['actual'])
df_kmplus['predict'] = predic_kmplus
kmplus_result = scoring(df_kmplus, NUM_CLUSTERS)
print(kmplus_result)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=NUM_CLUSTERS, first_center=best_cents, max_iter=1000, random_state=42)
fcm.fit(X)
probability = fcm.predict(x_test)
df_fcm = pd.DataFrame(data=y_test, columns=['actual'])
print(list(set(probability[:,4])))
df_fcm['predict'] = probability[:,4]
fcm_result = scoring(df_fcm, NUM_CLUSTERS)
print(fcm_result)