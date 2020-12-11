from sklearn.cluster import DBSCAN
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import pandas as pd

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

# Some variables
NUM_CLUSTERS = 2
k_num = 10
kf = KFold(n_splits=k_num, shuffle=True, random_state=42)

print("\n데이터 호출")
data = pd.read_csv("dataset/Unknown_data.csv")


y = data['Label']
le = LabelEncoder().fit(y)
y = le.transform(y)

X = data.drop(['Label'], axis=1)
col = X.columns
X = X.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#DBSCAN
print("\nDBSCAN")
ds = DBSCAN()
ds.fit(X_test)
predic_ds = ds.fit_predict(X_test)
ds_df = pd.DataFrame(data=predic_ds, columns=['predict'])
ds_df['actual'] = y_test

ds_result = scoring(ds_df)
print(ds_result)
#ds_df.to_csv("dataset/(1)ds_predict.csv", index=False)