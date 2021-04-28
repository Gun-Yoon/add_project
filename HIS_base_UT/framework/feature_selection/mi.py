from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import numpy as np

def mi_fs(df):
    #데이터 호출
    train_data = df.copy()
    X = train_data.drop(['Label'], axis=1).to_numpy()
    train_data['Label'] = pd.factorize(train_data['Label'])[0].astype(np.uint16)
    y = train_data['Label'].to_numpy()

    #Mutual Information 수행
    corr_data = train_data.drop(['Label'], axis=1)
    mic = mutual_info_classif(X,y)

    high_score_features = []
    for score, f_name in sorted(zip(mic, train_data.columns), reverse=True)[:len(corr_data.columns)]:
        if score >= 0.9:
            high_score_features.append(f_name)

    #print(high_score_features)

    #데이터 호출
    data = df.copy()

    pre_df = data[high_score_features]
    pre_df['Label'] = data['Label']
    #print(pre_df.shape)

    return pre_df