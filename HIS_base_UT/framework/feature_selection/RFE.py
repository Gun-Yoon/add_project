import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier

def rfe_fs(df):
    print("")
    #데이터 호출
    train_data = df.copy()
    label = train_data['Label']
    data = train_data.drop(['Label'], axis=1)
    feature_name = data.columns

    feature_importance_erf = pd.DataFrame(index=range(0,len(feature_name)), columns=['name','DT','RF','ERF','rank'])

    # DT 기반 특징 평가
    print("DT")
    dt_model =DecisionTreeClassifier(random_state=42)
    dt_selector = RFE(dt_model)
    dt_selector = dt_selector.fit(data,label)

    rfe_dt = zip(feature_name, dt_selector.ranking_)
    rfe_dt_dc = {x : y for x, y in rfe_dt}

    feature_importance_erf['DT'] = rfe_dt_dc.values()

    # RF 기반 특징 평가
    print("RF")
    rf_model =RandomForestClassifier(random_state=42)
    rf_selector = RFE(rf_model)
    rf_selector = rf_selector.fit(data,label)

    rfe_rf = zip(feature_name, rf_selector.ranking_)
    rfe_rf_dc = {x : y for x, y in rfe_rf}

    feature_importance_erf['RF'] = rfe_rf_dc.values()

    # ERF 기반 특징 평가
    print("ERF")
    erf_model =ExtraTreesClassifier(random_state=42)
    erf_selector = RFE(erf_model)
    erf_selector = erf_selector.fit(data,label)

    rfe_erf = zip(feature_name, erf_selector.ranking_)
    rfe_erf_dc = {x : y for x, y in rfe_erf}

    feature_importance_erf['ERF'] = rfe_erf_dc.values()

    feature_importance_erf['name'] = feature_name
    feature_importance_erf['rank'] = feature_importance_erf.mean(axis=1)

    #print(feature_importance_erf)

    #feature_importance_erf.to_csv('../dataset/feature_importance_erf.csv', index=False)

    temp_data = df.copy()
    feature_first = feature_importance_erf[feature_importance_erf['rank'] <= 1]
    pre_df = temp_data[feature_first['name'].tolist()]

    pre_df['Label'] = temp_data['Label'].tolist()
    print(pre_df.shape)

    return pre_df