"""
    - 0 : known / 1 : normal / 2 : unknown
"""

import pandas as pd
from paper_experiment import anomaly_detection, best_centroid, fuzzy_c_mean, advanced_fcm
print("\n데이터 호출")
train_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_data.csv")
train_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Train_label.csv")
test_data = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_data.csv")
test_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_label.csv")

anomaly = anomaly_detection.anomaly_test(train_data,train_label,test_data,test_label,0.2)
test_label = pd.read_csv("F:/data/KDD99/NSL-KDD/Test_label.csv")
process_one_df = anomaly_detection.data_extraction(test_data, test_label, anomaly)
process_one_df.to_csv('F:/data/KDD99/NSL-KDD/test.csv', index=False)

best_cent = best_centroid.best_cent(2,100,train_data,train_label,process_one_df)

# fit the fuzzy-c-means
fuzzy_c_mean.fuzzycmean(2,train_data,train_label,process_one_df,best_cent)

print("\n제안하는 방법 테스트")
#proposed method
#advanced_fcm.ad_fcm(2,train_data,train_label,process_one_df,best_cent)
