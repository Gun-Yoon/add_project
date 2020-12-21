"""
    알려진 공격에 대한 attack tree 생성
    CART를 이용 1)C4.5로 하고 차후 C5를 사용하여 생성 및 예정
    라이브러리 링크 : https://github.com/serengil/chefboost (['ID3', 'C4.5', 'CART', 'CHAID', 'Regression'])
"""

import pandas as pd
from chefboost import Chefboost as chef
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def make_df(name, df):
    print(name)
    result_df = df[(df['predict'] == name) == True]
    result_df.to_csv('dataset/misuse_result/' + name + '.csv', index=False)
    print(len(result_df))

test_data = pd.read_csv('dataset/pre_test.csv')
result_df = pd.DataFrame(data=test_data, columns=test_data.columns)
test_data.rename(columns = {'Label' : 'Decision'}, inplace = True)

#모델 호출
model = chef.load_model("dataset/c45_model.pkl")

test_label = test_data['Decision']
test_data = test_data.drop(['Decision'], axis=1)

predict_list = []
for index, instance in test_data.iterrows():
    prediction = chef.predict(model, instance)
    predict_list.append(prediction)

result_df.rename(columns = {'Decision' : 'actual'}, inplace = True)
result_df['predict'] = predict_list
print(len(result_df))
print(result_df.columns)

label_list = set(result_df['predict'])
for name in label_list:
    make_df(name, result_df)