"""
src_bytes 0.7154062463580262
diff_srv_rate 0.5092118943594457
same_srv_rate 0.4629653777002307
dst_bytes 0.4607568136503941
dst_host_diff_srv_rate 0.452063904351953
dst_host_srv_count 0.4171018316754942
count 0.41339259924703264
dst_host_serror_rate 0.40611225469023315
dst_host_same_srv_rate 0.4044796333502303
serror_rate 0.391945727459577
dst_host_srv_serror_rate 0.3814220795270753
srv_serror_rate 0.3672446840681307
logged_in 0.3129872107573246
dst_host_srv_diff_host_rate 0.26263327576811624
dst_host_same_src_port_rate 0.23753065935008344
dst_host_count 0.20870385874928488
srv_count 0.16181530943344646
srv_diff_host_rate 0.147913902099583
dst_host_rerror_rate 0.10108101475234532
dst_host_srv_rerror_rate 0.08581332488368298
rerror_rate 0.08186725542757833
duration 0.05983619909761484
srv_rerror_rate 0.05660175476541229
hot 0.023304719946443786
is_guest_login 0.012583516833621022
wrong_fragment 0.008849132966176398
num_compromised 0.008017138814303104
urgent 0.0033740869479612634
num_root 0.003284205434557874
num_shells 0.003255084562280075
num_access_files 0.002788120858283394
num_failed_logins 0.0026373817895517515
root_shell 0.0018953609253318238
num_file_creations 0.00040213989310022846
su_attempted 0.0
num_outbound_cmds 0.0
land 0.0
is_host_login 0.0

공격 기준 selection
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