import pandas as pd
from sklearn.model_selection import train_test_split

def df_sep(df, t_name):
    # CSV 파일 호출
    data = df.copy()
    threat_name = t_name

    unknown_data = data[(data['Label'] == threat_name) == True]
    known_data = data[(data['Label'] != threat_name) == True]

    # 데이터 분할
    train, test = train_test_split(known_data, test_size=0.2, random_state=123)

    test = pd.concat([test, unknown_data], axis=0)

    #print(train.shape)
    #print(set(train.Label))
    #train.to_csv('dataset/train.csv', index=False)

    #print("")
    #print(test.shape)
    #print(set(test.Label))
    #test.to_csv('dataset/test.csv', index=False)

    return train, test