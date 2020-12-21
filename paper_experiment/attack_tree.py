"""
    알려진 공격에 대한 attack tree 생성
    CART를 이용 1)C4.5로 하고 차후 C5를 사용하여 생성 및 예정
    라이브러리 링크 : https://github.com/serengil/chefboost (['ID3', 'C4.5', 'CART', 'CHAID', 'Regression'])
"""

import pandas as pd
from chefboost import Chefboost as chef

train_data = pd.read_csv('dataset/pre_train.csv')

train_data.rename(columns = {'Label' : 'Decision'}, inplace = True)
#train_data = train_data[(train_data['Decision'] != 'dos') == True]

# model 생성
config = {'algorithm':'C4.5'}
model = chef.fit(train_data, config)

#모델 저장
chef.save_model(model, "dataset/c45_model.pkl")