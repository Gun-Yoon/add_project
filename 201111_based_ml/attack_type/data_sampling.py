"""
    Mutual information과 Pearson correlation을 활용하여 특징 선택 수행
    -Feature Selection and Discretization based on Mutual Information
    -Mutual Information between Discrete and Continuous Data set
    -Estimating mutual information

    전체 데이터에서 샘플링 수행하며, 각 데이터별로 가지고 있는 Label 비율을 적용하여 데이터 추출
    Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv : Benign(93%), DDoS attacks-LOIC-HTTP(7%)
    Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv : Benign(34%), DDOS attack-HOIC(65%)
    Friday-02-03-2018_TrafficForML_CICFlowMeter.csv : Benign(73%), Bot(27%)
    Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv : Benign(72%), Infilteration(28%)
    Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv : Benign(64%), FTP-BruteForce(18%)

    알려지지않은 공격은 Bot으로 지정
    Friday-16-02-2018_TrafficForML_CICFlowMeter.csv : Benign(43%), DoS attacks-Hulk(44%)

    *각 데이터별 10만개(10%) 추출하여 데이터 셋 구축*

    구축된 데이터 셋 정보:
        - Label 수 : 정상 + 공격(3) + 알려지지않은 공격(1) -> 5개
        - Record 수 : 40만개

        Data Name : Friday-16-02-2018_TrafficForML_CICFlowMeter.csv
        정상 : 43000, 공격 : 44000 / 데이터 구성 : (87000, 80)

        Data Name : Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv
        정상 : 93000, 공격 : 7000 / 데이터 구성 : (100000, 80)

        Data Name : Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv
        정상 : 34000, 공격 : 65000 / 데이터 구성 : (99000, 80)

        Data Name : Friday-02-03-2018_TrafficForML_CICFlowMeter.csv
        정상 : 73000, 공격 : 27000 / 데이터 구성 : (100000, 80)

        Known 데이터 구성 : (286000, 80)
        Unknown 데이터 구성 : (100000, 80)

    data_path_dir : 파일 디렉토리
    csv_list : CSV 파일명
    percent_num : 데이터별 Label, 데이터 비율 저장
"""

from sklearn.feature_selection import mutual_info_classif
import pandas as pd
import numpy as np

# CSV 파일 호출
data_path_dir = "F:/data/Processed Traffic Data for ML Algorithms/"
csv_list = ['Friday-02-03-2018_TrafficForML_CICFlowMeter.csv',
            'Friday-16-02-2018_TrafficForML_CICFlowMeter.csv','Friday-16-02-2018_TrafficForML_CICFlowMeter.csv',
            'Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv',
            'Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv',
            'Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv','Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv',
            'Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv','Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv',
            'Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv','Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv']
percent_num = [(['Benign', 'Bot'], 73, 27),
               (['Benign', 'DoS attacks-Hulk'], 43, 44),(['Benign', 'DoS attacks-SlowHTTPTest'], 43, 13),
               (['Benign', 'DDoS attacks-LOIC-HTTP'], 93, 7),
               (['Benign', 'Infilteration'], 72, 28),
               (['Benign', 'DoS attacks-Slowloris'], 95, 1),(['Benign', 'DoS attacks-GoldenEye'], 95, 4),
               (['Benign', 'FTP-BruteForce'], 64, 18),(['Benign', 'SSH-Bruteforce'], 64, 18),
               (['Benign', 'DDOS attack-LOIC-UDP'], 34, 1),(['Benign', 'DDOS attack-HOIC'], 34, 65)]
mal_list = ['Bot','DoS attacks-Hulk','DoS attacks-SlowHTTPTest','DDoS attacks-LOIC-HTTP','Infilteration',
            'DoS attacks-Slowloris','DoS attacks-GoldenEye','FTP-BruteForce','SSH-Bruteforce','DDOS attack-LOIC-UDP',
            'DDOS attack-HOIC']

for num in range(len(csv_list)):
    print("\nData Name : {}".format(csv_list[num]))
    temp_data = pd.read_csv(data_path_dir + csv_list[num])

    # 불필요한 특징 제거(대부분의 값이 Nan으로 되어있는 특징 제거 / 날짜 제거)
    temp_data = temp_data.drop(['Timestamp'], axis=1)
    temp_data = temp_data.drop(['Flow Pkts/s', 'Tot Bwd Pkts', 'Bwd Pkts/s', 'Subflow Bwd Pkts',
                                'Flow IAT Max', 'Flow IAT Mean', 'Flow IAT Min', 'Pkt Size Avg', 'Pkt Len Mean',
                                'Pkt Len Var',
                                'Pkt Len Std', 'Subflow Fwd Pkts', 'Tot Fwd Pkts', 'Flow Duration', 'Fwd Pkt Len Std',
                                'Pkt Len Max', 'Flow Byts/s', 'Bwd Pkt Len Std', 'Init Bwd Win Byts',
                                'Fwd Seg Size Min',
                                'Flow IAT Std', 'Bwd IAT Min', 'Bwd IAT Mean', 'Fwd IAT Std', 'Bwd IAT Max',
                                'Bwd IAT Tot',
                                'Bwd IAT Std', 'Fwd Act Data Pkts', 'ACK Flag Cnt', 'Protocol', 'Idle Max', 'Idle Min',
                                'Idle Mean', 'Fwd Pkt Len Min', 'Pkt Len Min', 'Bwd Pkt Len Min', 'PSH Flag Cnt',
                                'ECE Flag Cnt',
                                'RST Flag Cnt', 'Down/Up Ratio', 'Active Min', 'Active Mean', 'Active Max', 'Idle Std',
                                'Active Std', 'Fwd PSH Flags', 'SYN Flag Cnt', 'URG Flag Cnt', 'Fwd Blk Rate Avg',
                                'Bwd Blk Rate Avg', 'Bwd Pkts/b Avg', 'Bwd Byts/b Avg', 'Fwd URG Flags',
                                'Fwd Pkts/b Avg',
                                'Fwd Byts/b Avg', 'FIN Flag Cnt', 'CWE Flag Count', 'Bwd URG Flags', 'Bwd PSH Flags'],axis=1)  # Mutual Information 기반 삭제할 특징 삭제
    if 'Flow ID' in temp_data.columns:
        temp_data = temp_data.drop(['Flow ID', 'Src IP', 'Src Port', 'Dst IP'], axis=1)

    if 'Infilteration' in percent_num[num][0]:
        temp_benign = int(300000 / 100 * int(percent_num[num][1]))
        temp_mal = int(300000 / 100 * int(percent_num[num][2]))
        print("정상 : {0}, 공격 : {1}".format(temp_benign, temp_mal))
    elif 'DoS attacks-Slowloris' in percent_num[num][0]:
        temp_benign = int(1000000 / 100 * int(percent_num[num][1]))
        temp_mal = int(100000 / 100 * int(percent_num[num][2]))
        print("정상 : {0}, 공격 : {1}".format(temp_benign, temp_mal))
    elif 'DoS attacks-GoldenEye' in percent_num[num][0]:
        temp_benign = int(1000000 / 100 * int(percent_num[num][1]))
        temp_mal = int(100000 / 100 * int(percent_num[num][2]))
        print("정상 : {0}, 공격 : {1}".format(temp_benign, temp_mal))
    elif 'DDOS attack-LOIC-UDP' in percent_num[num][0]:
        temp_benign = int(1000000 / 100 * int(percent_num[num][1]))
        temp_mal = int(10000 / 100 * int(percent_num[num][2]))
        print("정상 : {0}, 공격 : {1}".format(temp_benign, temp_mal))
    else:
        temp_benign = int(1000000 / 100 * int(percent_num[num][1]))
        temp_mal = int(1000000 / 100 * int(percent_num[num][2]))
        print("정상 : {0}, 공격 : {1}".format(temp_benign, temp_mal))
        # 샘플링 데이터 비율 설정

    # 고정개수의 레코드만큼 데이터 추출
    temp_label = percent_num[num][0]
    temp_benign_data = temp_data[temp_data['Label'] == temp_label[0]].sample(n=temp_benign, random_state=150)
    temp_mal_data = temp_data[temp_data['Label'] == temp_label[1]].sample(n=temp_mal, random_state=150)
    sampling_data = pd.concat([temp_benign_data, temp_mal_data], axis=0)

    # 샘플링 데이터 확인
    print("데이터 구성 : %s" % str(sampling_data.shape))

    # Nan과 Finite 값 제거
    sampling_data = sampling_data[~sampling_data.isin([np.nan, np.inf, -np.inf]).any(1)]
    sampling_data.to_csv('F:/data/ADD/201210/'+mal_list[num]+'.csv', index=False)