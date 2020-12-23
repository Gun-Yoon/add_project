"""
    ===============특징 선택(2)===============
    42개 특징에 대한 평가 진행
    평가는 'Analysis of Feature Importance and Interpretation for Malware classification'을 참고하여 진행
    DT,RF, ERF의 특징 중요도 평가 수행

    'dataset/feature_importance_value.csv' : 특징에 따른 평가 value 저장
    'dataset/feature_importance_sort.csv' : 각 특징별 중요 특징 sorting 수행(내림차순)
    'dataset/feature_importance_erf.csv' : 특징에 ranking을 측정하고 이를 평균화하여 의견반영
"""

import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier

#데이터 호출
train_data = pd.read_csv('dataset/train_data.csv')
label = train_data['Label']
data = train_data.drop(['Label'], axis=1)
feature_name = data.columns

#feature_importance_val = pd.DataFrame(index=feature_name, columns=['DT','RF','ERF'])
#feature_importance_name = pd.DataFrame(index=range(0,len(feature_name)), columns=['DT_name','DT_val','RF_name','RF_val','ERF_name','ERF_val'])
feature_importance_erf = pd.DataFrame(index=range(0,len(feature_name)), columns=['name','DT','RF','ERF','rank'])

# DT 기반 특징 평가
print("DT")
dt_model =DecisionTreeClassifier(random_state=42)
#dt_model.fit(data,label)
dt_selector = RFE(dt_model)
dt_selector = dt_selector.fit(data,label)

rfe_dt = zip(feature_name, dt_selector.ranking_)
#rfe_dt = sorted(rfe_dt, key=lambda i: i[1])
rfe_dt_dc = {x : y for x, y in rfe_dt}

#sort_dt_zip = sorted(zip(feature_name, dt_model.feature_importances_), key=lambda i: i[1], reverse=True)
#dt_dc = {x : y for x, y in zip(feature_name, dt_model.feature_importances_)}
#dt_sort_dc = {x : y for x, y in sort_dt_zip}
#feature_importance_val['DT'] = dt_dc.values()
#feature_importance_name['DT_name'] = dt_sort_dc.keys()
#feature_importance_name['DT_val'] = dt_sort_dc.values()
feature_importance_erf['DT'] = rfe_dt_dc.values()

# RF 기반 특징 평가
print("RF")
rf_model =RandomForestClassifier(random_state=42)
#rf_model.fit(data,label)
rf_selector = RFE(rf_model)
rf_selector = rf_selector.fit(data,label)

rfe_rf = zip(feature_name, rf_selector.ranking_)
#rfe_rf = sorted(rfe_rf, key=lambda i: i[1])
rfe_rf_dc = {x : y for x, y in rfe_rf}

#sort_rf_zip = sorted(zip(feature_name, rf_model.feature_importances_), key=lambda i: i[1], reverse=True)
#rf_dc = {x : y for x, y in zip(feature_name, rf_model.feature_importances_)}
#rf_sort_dc = {x : y for x, y in sort_rf_zip}
#feature_importance_val['RF'] = rf_dc.values()
#feature_importance_name['RF_name'] = rf_sort_dc.keys()
#feature_importance_name['RF_val'] = rf_sort_dc.values()
feature_importance_erf['RF'] = rfe_rf_dc.values()

# ERF 기반 특징 평가
print("ERF")
erf_model =ExtraTreesClassifier(random_state=42)
#erf_model.fit(data,label)
erf_selector = RFE(erf_model)
erf_selector = erf_selector.fit(data,label)

rfe_erf = zip(feature_name, erf_selector.ranking_)
#rfe_erf = sorted(rfe_erf, key=lambda i: i[1])
rfe_erf_dc = {x : y for x, y in rfe_erf}

#sort_erf_zip = sorted(zip(feature_name, erf_model.feature_importances_), key=lambda i: i[1], reverse=True)
#erf_dc = {x : y for x, y in zip(feature_name, erf_model.feature_importances_)}
#erf_sort_dc = {x : y for x, y in sort_erf_zip}
#feature_importance_val['ERF'] = erf_dc.values()
#feature_importance_name['ERF_name'] = erf_sort_dc.keys()
#feature_importance_name['ERF_val'] = erf_sort_dc.values()
feature_importance_erf['ERF'] = rfe_erf_dc.values()

feature_importance_erf['name'] = feature_name
feature_importance_erf['rank'] = feature_importance_erf.mean(axis=1)

#print(feature_importance_val)
#print(feature_importance_name)
print(feature_importance_erf)

#feature_importance_val.to_csv('dataset/feature_importance_value.csv', index=False)
#feature_importance_name.to_csv('dataset/feature_importance_sort.csv', index=False)
feature_importance_erf.to_csv('dataset/feature_importance_erf.csv', index=False)