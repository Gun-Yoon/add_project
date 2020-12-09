"""
    fuzzy c-mean에서 test에 사용된 데이터 셋에서 각 클러스터의 결정 경계에 분포되어 있는 데이터들을 추출
    benign_data는 test에서 정상으로 군집화된 데이터 셋
    attack_data는 test에서 위협으로 군집화된 데이터 셋
    centroid는 fuzzy c-mean에서 최종적으로 산출된 중심 벡터(첫번째는 정상 / 두번째는 위협)

    정상/위협의 평균 거리와 표준편차를 구하고, 표준편차보다 먼 거리에 있는 데이터들을 결정 경계에 분포되어 있는 데이터로 정의
"""

from scipy.spatial import distance
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

benign_raw = pd.read_csv("dataset/df_benign.csv")
attack_raw = pd.read_csv("dataset/df_attack.csv")
standard_data = pd.concat([benign_raw, attack_raw], axis=0)
centroid = [[45848.247303895856, 922.4596065577446, 407.1701727877382, 921.2567857963534, 186.47624411743897, 359.5369967117907, 119.48956722210153, 4810168.213311829, 1225757.1736451185, 4680330.184515111, 7642.554275982365, 166.3395995391915, 115.93853496622576, 1.146745429159639, 186.47624411743897, 119.48956722210153, 922.4596065577446, 407.1701727877382, 228.03583818404033], [901.4383214885949, 18.938521656572696, 36.07221827473216, 18.647858973421794, 5.190672412919071, 32.333730375893985, 8.233846150083142, 303954.56412531785, 90709.11172267026, 295205.78344028664, 19399.22321726312, 70.36320483630978, 5.830471136532167, 1223.977788196416, 5.190672412919071, 8.233846150083142, 18.938521656572696, 36.07221827473216, 1047.4925292635908]]

std_scaler = StandardScaler()
std_scaler.fit(standard_data)
benign_data = pd.DataFrame(data=std_scaler.transform(benign_raw), columns=benign_raw.columns)
attack_data = pd.DataFrame(data=std_scaler.transform(attack_raw), columns=attack_raw.columns)
centroid = list(std_scaler.transform(centroid))

benign_distance = pd.DataFrame(index=range(0,len(benign_data)), columns=['distance'])
attack_distance = pd.DataFrame(index=range(0,len(attack_data)), columns=['distance'])

print(color.RED+"\n정상/악성 각각의 벡터에 대한 유클리드 거리 측정"+color.END)
for i in range(len(benign_data)):
    benign_distance.loc[i] = distance.euclidean(benign_data.loc[i],centroid[0])

for i in range(len(attack_data)):
    attack_distance.loc[i] = distance.euclidean(attack_data.loc[i],centroid[0])
print(benign_distance.head())
print(attack_distance.head())

print(color.RED+"\n유클리드 거리 기반 평균 및 표준편차 계산"+color.END)
benign_arr = benign_distance.to_numpy()
attack_arr = attack_distance.to_numpy()

benign_mean = np.mean(benign_arr)   #평균
benign_std = np.std(benign_arr)     #표준편차
attack_mean = np.mean(attack_arr)   #평균
attack_std = np.std(attack_arr)     #표준편차

print('정상 평균 : {0}\n정상 표준편차 : {1}\n위협 평균 : {2}\n위협 표준편차 : {3}'.format(benign_mean,benign_std,attack_mean,attack_std))

print(color.RED+"\n클러스터 결정경계에 위치되어 있는 데이터 추출"+color.END)

print("정상 클러스터 결정 경계 데이터 셋")
benign_bounderies_index = benign_distance[(benign_distance['distance'] >= (benign_mean+benign_std)) == True]
benign_bounderies = benign_raw.loc[benign_bounderies_index.index.values]
#benign_bounderies.to_csv('dataset/benign_bounderies.csv', index=False)
print(benign_bounderies.shape)

print("\n위협 클러스터 결정 경계 데이터 셋")
attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean+attack_std)) == True]
attack_bounderies = attack_raw.loc[attack_bounderies_index.index.values]
#attack_bounderies.to_csv('dataset/attack_bounderies.csv', index=False)
print(attack_bounderies.shape)