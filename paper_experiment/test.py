import os
import pandas as pd

path_dir = 'dataset/fcm_result/'

file_list = os.listdir(path_dir)

temp_list = []
for file_name in file_list:
    print("\n"+file_name)
    temp_data = pd.read_csv(path_dir+file_name)
    print(list(set(temp_data['actual'])))
    temp_data = temp_data.loc[:,['actual','predict']]
    print(temp_data)
    temp_list.append(temp_data)

predict_result = pd.concat([i for i in temp_list], axis=0)
print(len(predict_result))

predict_result.to_csv('dataset/fcm_result/result.csv',index=False)