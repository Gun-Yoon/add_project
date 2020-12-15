import pandas as pd
import numpy as np

def attack_type_trans(df, attack_type_df):
    for df_num in range(len(df)):
        for attack_type_num in range(len(attack_type_df)):
            if df['Label'][df_num] == 'normal':
                pass
            elif df['Label'][df_num] == attack_type_df['detail'][attack_type_num]:
                df['Label'][df_num] = attack_type_df['type'][attack_type_num]

    #df = df[(df['Label'] == 'normal') == False]
    return df

#Call Train data
dataset_path = 'F:/data/KDD99/NSL-KDD/KDDTrain+.csv'
idsTrain = pd.read_csv(dataset_path, header=None)

#Call Test data
dataset_path = 'F:/data/KDD99/NSL-KDD/KDDTest+.csv'
idsTest = pd.read_csv(dataset_path, header=None)

#Call Field name
dataset_columns = 'F:/data/KDD99/NSL-KDD/Field Names.csv'
idsDF_columns = pd.read_csv(dataset_columns, header=None)
idsTrain.columns = idsDF_columns.iloc[:, 0]
idsTest.columns = idsDF_columns.iloc[:, 0]

#Call Attack type
dataset_label = 'F:/data/KDD99/NSL-KDD/Attack Types.csv'
ids_label = pd.read_csv(dataset_label)
idsTrain = attack_type_trans(idsTrain, ids_label)
idsTest = attack_type_trans(idsTest, ids_label)

train_Label = idsTrain['Label']
test_Label = idsTest['Label']

idsTrain = idsTrain.select_dtypes(include=[np.float64, np.int64, np.int32])
idsTest = idsTest.select_dtypes(include=[np.float64, np.int64, np.int32])

del idsTrain['level']
del idsTest['level']

print(idsTrain.head())
print(idsTrain.shape)
print(list(set(train_Label)))

print(idsTest.head())
print(idsTest.shape)
print(list(set(test_Label)))

idsTrain.to_csv('F:/data/KDD99/NSL-KDD/Train_data.csv', index=False)
idsTest.to_csv('F:/data/KDD99/NSL-KDD/Test_data.csv', index=False)
train_Label.to_csv('F:/data/KDD99/NSL-KDD/Train_label.csv', index=False)
test_Label.to_csv('F:/data/KDD99/NSL-KDD/Test_label.csv', index=False)