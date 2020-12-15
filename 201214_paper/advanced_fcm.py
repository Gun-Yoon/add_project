from fcmeans import FCM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import numpy as np
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

# Some variables
NUM_CLUSTERS = 4

print(color.BOLD+"\n데이터 호출"+color.END)
train_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
train_data = train_data.drop(['num_compromised','num_file_creations','num_access_files','wrong_fragment',
                  'root_shell','num_failed_logins','num_shells','num_outbound_cmds','urgent','su_attempted',
                  'num_root','land','is_host_login'], axis=1)
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

best_cents = [[-0.10212415043810268, -0.00568773341595566, -0.004946050537159135, 0.40089082442727453, 0.8203335459558522, 0.3321067726203586, -0.4256617178032613, 0.9632999044426577, -1.20971107308101, -1.198533111743241, -0.49733328844171854, -0.4840379268682684, 1.6938446386806927, -0.4562873487677785, 1.179126551213772, -1.331198868418921, 1.5032987037839038, 1.8501800709586045, -0.4058258866930234, 1.5143277524148633, 1.0269502808792215, -1.205295943220701, -1.201214326342044, -0.45052161704009897, -0.4977509851997306], [0.5410023805835588, 0.0332454508839395, 0.028338535041039885, -0.08650018147773814, -0.1785969417589995, -0.07337886000629187, -0.23124142782770146, -0.231563771461018, -1.2130917393734126, -1.2092562130340636, 1.8086840146034115, 1.778389228582484, 0.0532591670050126, -0.19956415885086423, -0.26323016639766383, 0.1849320311227303, -0.40650932506339194, -0.44699776562346344, 0.5140613458391957, 0.0040794646102261505, -0.08107361234692183, -1.2172850086891744, -1.2056337915762436, 1.8716001962642783, 1.7803598250302022], [-0.11932238385086659, -0.007329004934973599, -0.006363447217590727, -0.08916355450402513, -0.18768475491829784, -0.07337886000629387, 0.10871706268619148, -0.19928567585432805, 0.8108769651426274, 0.8098382913512028, -0.5146553945624234, -0.5135874391280748, -0.48392452964477156, -0.1285360079639055, -0.2598113018527628, 0.3207493196460369, -0.2930825493608728, -0.38437181222127287, -0.25590599580556217, -0.45646326015984295, -0.26660665938543915, 0.8109838044467286, 0.8093991124537558, -0.526311840298027, -0.5105459483674691], [-0.11926169810400752, -0.009638103526193072, -0.00636516095863553, -0.08890890578366609, -0.10960310250168505, -0.07337886000629022, 1.1262739341286674, -0.3146644203704947, -1.0838483660959362, -1.1280859695714163, 1.6698245377357763, 1.7185345113494013, -0.5842138526548748, 4.1351214634351745, -0.25949121075791753, 0.36539558008372486, -0.5492850013173127, -0.5755520455430633, 2.883802006120292, -0.05701917102130869, -0.26944538017809383, -1.0865024815873356, -1.1257558326496786, 1.4017725642956809, 1.7253845865356212]]
best_cents = np.array(best_cents)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=NUM_CLUSTERS, first_center=best_cents, max_iter=1000, random_state=42)
fcm.fit(x_train)
probability = fcm.predict(x_test)
df_fcm = pd.DataFrame(data=y_test, columns=['actual'])
df_fcm['predict'] = probability[:,4]