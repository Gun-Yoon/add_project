"""
dst_host_diff_srv_rate 0.35773331218376425
count 0.32080484217787353
src_bytes 0.32022856655210563
diff_srv_rate 0.31574464652782597
dst_host_serror_rate 0.25496534667834303
serror_rate 0.23897764551416012
dst_host_same_src_port_rate 0.22689721991274747
same_srv_rate 0.22273946577541182
srv_count 0.21210721242401642
dst_host_srv_serror_rate 0.21194188519114232
srv_serror_rate 0.20829331364936277
dst_host_same_srv_rate 0.20683304812974002
dst_host_srv_count 0.17871979932447757
dst_host_srv_diff_host_rate 0.1599762905942761
dst_host_count 0.1513562490919791
dst_host_rerror_rate 0.13508540669997982
srv_diff_host_rate 0.10642712208732008
rerror_rate 0.08447584163246269
duration 0.06959653175468938
logged_in 0.060303044024323516
dst_host_srv_rerror_rate 0.05118405369885881
dst_bytes 0.0445103707482557
srv_rerror_rate 0.04395371624711153
hot 0.03570581771682391
is_guest_login 0.021079527768367523
num_compromised 0.00812863437340372
num_file_creations 0.005710837563356108
num_access_files 0.004982912329812628
wrong_fragment 0.004108714632090393
root_shell 0.0036234365601142127
num_failed_logins 0.0035836498637824565
num_shells 0.0030453158938958946
num_outbound_cmds 0.002035519123620544
urgent 0.0010061002471364322
su_attempted 0.0009107829293286684
num_root 0.0005619596603940735
land 0.00035158338907015363
is_host_login 0.0
"""

from sklearn.feature_selection import mutual_info_classif
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

print("\n데이터 호출")
data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
label = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_label.csv")

# Class :  ['dos' 'probe' 'r2l' 'u2r']
train_total = pd.concat([data, label], axis=1)
normal_index = train_total[(train_total['Label'] == 1) == False].index
train_total = train_total.loc[normal_index]

y = train_total['Label']
le = LabelEncoder().fit(y)
print("Class to number : ",le.classes_)
y = le.transform(y)

X = train_total.drop(['Label'], axis=1).to_numpy()
std_scaler = StandardScaler()
fitted = std_scaler.fit(X)
X = std_scaler.transform(X)

#Mutual Information 수행
mic = mutual_info_classif(X,y)

high_score_features = []
for score, f_name in sorted(zip(mic, data.columns), reverse=True)[:len(data.columns)]:
    print(f_name, score)
    high_score_features.append(f_name)