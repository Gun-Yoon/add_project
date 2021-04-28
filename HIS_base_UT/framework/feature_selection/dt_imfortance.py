from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

def dt_fs(df):
    #데이터 호출
    train_data = df.copy()
    y = train_data['Label'].to_numpy()
    X = train_data.drop(['Label'], axis=1)

    std_scaler = StandardScaler()
    train = std_scaler.fit_transform(X)

    # define the model
    model = DecisionTreeClassifier()
    # fit the model
    model.fit(train, y)
    # get importance
    importance = model.feature_importances_

    high_score_features = []
    # summarize feature importance
    for i,v, in enumerate(importance):
        if v > 0:
            high_score_features.append(i)

    #데이터 호출
    data = df.copy()

    pre_df = data.iloc[:,high_score_features]
    pre_df['Label'] = data['Label']
    #print(pre_df.shape)

    return pre_df