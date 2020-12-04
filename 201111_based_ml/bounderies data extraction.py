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

benign_data = pd.read_csv("dataset/df_benign.csv")
attack_data = pd.read_csv("dataset/df_attack.csv")
centroid = [[0.938805887305535, 0.9810643328255747, 0.07532707510788424, 0.9832582374136084, 0.97639971807557,
             0.7644889545720601, 0.8412442248395775, 0.2948681215639623, 0.26714266736526215, 0.2941154022780497,
             -0.015326195389452317, 0.9342591683014572, 0.7218558391174821, -0.12278416871385163, 0.97639971807557,
             0.8412442248395775, 0.9810643328255747, 0.07532707510788424, -0.04235995283569242],
            [-0.9383893225594496, -0.9976158145483698, -0.08836943762501397, -0.998563612533996, -1.0023682656258093,
             -0.8709686348059381, -0.920066230246388, -0.3863745535796511, -0.35639708585938906, -0.38557230344189963,
             0.0022184005898271187, -0.9564343386668844, -0.7825304543717697, 0.09573598577920255, -1.0023682656258093,
             -0.920066230246388, -0.9976158145483698, -0.08836943762501397, -0.07639214458746109]]

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
benign_bounderies = benign_data.loc[benign_bounderies_index.index.values]
benign_bounderies.to_csv('dataset/benign_bounderies.csv', index=False)
print(benign_bounderies.shape)

print("\n위협 클러스터 결정 경계 데이터 셋")
attack_bounderies_index = attack_distance[(attack_distance['distance'] >= (attack_mean+attack_std)) == True]
attack_bounderies = attack_data.loc[attack_bounderies_index.index.values]
attack_bounderies.to_csv('dataset/attack_bounderies.csv', index=False)
print(attack_bounderies.shape)