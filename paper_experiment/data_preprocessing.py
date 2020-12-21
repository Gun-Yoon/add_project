"""
    ===============특징 선택(3)===============
    특징 평가를 기반으로 특징 선택 및 최종 전처리 수행
"""
import pandas as pd

temp_data = pd.read_csv('dataset/train_data.csv')
feature_rank = pd.read_csv('dataset/feature_importance_erf.csv')
feature_first = feature_rank[feature_rank['rank'] <= 1]
pre_train_df = temp_data[feature_first['name'].tolist()]

test_data = pd.read_csv('dataset/test_data.csv')
pre_test_df = test_data[feature_first['name'].tolist()]

pre_train_df['Label'] = temp_data['Label']
pre_test_df['Label'] = test_data['Label']

pre_test_df = pre_test_df

print(pre_train_df.shape)
print(pre_test_df.shape)

pre_train_df.to_csv('dataset/pre_train.csv', index=False)
pre_test_df.to_csv('dataset/pre_test.csv', index=False)