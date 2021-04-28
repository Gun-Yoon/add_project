"""
    sampling():
        day는 공격이 수행된 날짜(A,B)
        data_size는 각 네트워크 데이터에서 추출하는 데이터 샘플 수
        A에는 'DoS attacks-SlowHTTPTest','DoS attacks-Hulk','Bot','Infilteration' 공격이 수행되었음
        B에는 'FTP-BruteForce','SSH-Bruteforce','DDOS attack-HOIC','Infilteration' 공격이 수행되었음
    matching():
        IoC 정보와 매칭을 통해 1차 탐지 수행
    feature selection:
        RFE, IM, DT 기반 중요도 3가지 방법을 적용하여 특징 선택 수행
        3가지 방식 중 한가지를 선택하고, 그에 따른 데이터 셋을 output으로 받음
    data separation:
        알려지지 않은 공격에 대해 정의하고, 이에 따라 학습 데이터화 훈련 데이터 분할
    misuse detection:
        CBA 알고리즘 기반 오용 탐지 수행
        알려진 공격에 대한 연관 규칙을 생성하고 이를 기반으로 Classification 수행
        알려진 공격에 대해서 탐지 가능
    anomaly detection:
        OCSVM 알고리즘 기반 이상 탐지 수행
        정상 데이터로 학습된 이상 탐지 모델을 기반으로 알려지지 않은 공격 탐지 수행
"""
from HIS_base_UT.framework.preprocessing.data_sampling import sampling
from HIS_base_UT.framework.ioc_matching import matching
from HIS_base_UT.framework.feature_selection import RFE, mi, dt_imfortance
from HIS_base_UT.framework.data_seperate import df_sep
from HIS_base_UT.framework.misuse_detection import misuse
from HIS_base_UT.framework.anomaly_detection import anomaly
from HIS_base_UT.performance import confusion_matrix
import time

# Data preprocessing
sampling_data = sampling(day='A', data_size=500000) #A & B 가능
print("\nSampling Data : {}".format(sampling_data.shape))

start_t = time.time() #프레임워크 시작 시간
# ioc matching
ioc_result_df = matching(data=sampling_data)
print("\nioc matching Data : {}".format(ioc_result_df.shape))

# feature selection
#fs_df = RFE.rfe_fs(ioc_result_df)
#fs_df = mi.mi_fs(ioc_result_df)
fs_df = dt_imfortance.dt_fs(ioc_result_df)
print("\nFeature selection Data : {}".format(fs_df.shape))

# data separation
unknown_threat = 'DoS attacks-SlowHTTPTest'  #Bot,DoS attacks-Hulk,DoS attacks-SlowHTTPTest,FTP-BruteForce,SSH-Bruteforce,DDOS attack-HOIC
train_df, test_df = df_sep(fs_df, unknown_threat)

# misuse detection
misuse_result_df = misuse(train_df, test_df)

# anomaly detection
anomaly_result_df = anomaly(train_df, misuse_result_df, unknown_threat)
end_t = time.time() #프레임워크 시작 시간

print("\n프레임워크 수행 시간 : {:.4F}".format(end_t-start_t))

# performance
confusion_matrix(anomaly_result_df)