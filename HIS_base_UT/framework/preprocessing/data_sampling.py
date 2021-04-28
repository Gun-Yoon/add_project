"""
    전체 데이터에서 샘플링 수행하며, 각 데이터별로 가지고 있는 Label 비율을 적용하여 데이터 추출
    알려지지않은 위협은 위협 클래스를 번갈아가면서 수행
    각 데이터 셋별 5만개(5%) 추출하여 데이터 셋 구축

    *금요일
    csv_list = ['Friday-16-02-2018_TrafficForML_CICFlowMeter.csv','Friday-02-03-2018_TrafficForML_CICFlowMeter.csv']
    percent_num = [(['Benign','DoS attacks-SlowHTTPTest','DoS attacks-Hulk'],[43,13,44]),(['Bot'],[27])]

    *목요일
    csv_list = ['Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv','Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv']
    percent_num = [(['Benign','DDoS attacks-LOIC-HTTP'],[93,7]),(['Infilteration'],[28])]

    *수요일
    csv_list = ['Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv','Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv']
    percent_num = [(['Benign','FTP-BruteForce','SSH-Bruteforce'],[64,18,18]),(['DDOS attack-HOIC'],[65])]
        
    data_path_dir : 파일 디렉토리
    csv_list : CSV 파일명
    percent_num : 데이터별 Label, 데이터 비율 저장
"""

import pandas as pd
import numpy as np

def sampling(day, data_size):
    pd.set_option('display.max_row', 500)
    pd.set_option('display.max_columns', 10)

    # CSV 파일 호출
    data_path_dir = "F:/data/Processed Traffic Data for ML Algorithms/"

    if day == 'A':
        print("Friday data set sampling...\n")
        csv_list = ['A(1).csv','A(2).csv','A(3).csv']
        percent_num = [(['Benign', 'DoS attacks-SlowHTTPTest', 'DoS attacks-Hulk'], [43, 13, 44]), (['Bot'], [27]),
                       (['Infilteration'],[10])]
    elif day == 'B':
        print("Wednesday data set sampling...\n")
        csv_list = ['B(1).csv','B(2).csv','B(3).csv']
        percent_num = [(['Benign','FTP-BruteForce','SSH-Bruteforce'],[64,18,18]),(['DDOS attack-HOIC'],[65]),
                       (['Infilteration'],[10])]

    d_list = []
    for num in range(len(csv_list)):
        data_list = []
        print("Data Name : {}".format(csv_list[num]))
        temp_data = pd.read_csv(data_path_dir + csv_list[num])

        # 불필요한 특징 제거(대부분의 값이 Nan으로 되어있는 특징 제거 / 날짜 제거)
        temp_data = temp_data.drop(['Timestamp'], axis=1)

        if 'Flow ID' in temp_data.columns:
            temp_data = temp_data.drop(['Flow ID', 'Src IP', 'Src Port', 'Dst IP'], axis=1)

        class_num = len(percent_num[num][0])
        for i in range(class_num):
            temp_percent = int(data_size/100*percent_num[num][1][i])
            data = temp_data[temp_data['Label'] == percent_num[num][0][i]].sample(n=temp_percent, random_state=150)
            data_list.append(data)

        sample_data = pd.concat([data_list[i] for i in range(len(data_list))], axis=0)

        # 샘플링 데이터 확인
        #print("데이터 구성 : %s"%str(sample_data.shape))
        d_list.append(sample_data)

    # 샘플링 데이터 통합
    data = pd.concat([d_list[i] for i in range(len(d_list))], axis=0)
    #print("\ndata 데이터 구성 : %s"%str(data.shape))

    # Nan과 Finite 값 제거
    data = data[~data.isin([np.inf, -np.inf]).any(1)]
    #print("\ndata 데이터 구성 : %s"%str(data.shape))

    #데이터 저장
    #data.to_csv('dataset/data.csv', index=False)

    #데이터 반환
    return data