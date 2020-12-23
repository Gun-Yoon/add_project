"""
    ===============특징 선택(1)===============
    NTS-KDD 데이터 셋에 존재하는 symbolic 특징은 4개
    1) protocol_type , 2) service, 3) flag, 4) level
    level은 이미 binary화가 되어있으므로 나머지 3개 특징에 대한 symbolic 정보를 binary 정보로 변환

    protocol_type(3) : ['icmp' 'tcp' 'udp']
    service(70) : ['IRC' 'X11' 'Z39_50' 'aol' 'auth' 'bgp' 'courier' 'csnet_ns' 'ctf' 'daytime' 'discard' 'domain'
    'domain_u' 'echo' 'eco_i' 'ecr_i' 'efs' 'exec' 'finger' 'ftp' 'ftp_data' 'gopher' 'harvest' 'hostnames' 'http'
    'http_2784' 'http_443' 'http_8001' 'imap4' 'iso_tsap' 'klogin' 'kshell' 'ldap' 'link' 'login' 'mtp' 'name'
    'netbios_dgm' 'netbios_ns' 'netbios_ssn' 'netstat' 'nnsp' 'nntp' 'ntp_u' 'other' 'pm_dump' 'pop_2' 'pop_3'
    'printer' 'private' 'red_i' 'remote_job' 'rje' 'shell' 'smtp' 'sql_net' 'ssh' 'sunrpc' 'supdup' 'systat' 'telnet'
    'tftp_u' 'tim_i' 'time' 'urh_i' 'urp_i' 'uucp' 'uucp_path' 'vmnet' 'whois']
    flag(11) : ['OTH' 'REJ' 'RSTO' 'RSTOS0' 'RSTR' 'S0' 'S1' 'S2' 'S3' 'SF' 'SH']
"""

import pandas as pd

#데이터 호출
train_data = pd.read_csv('F:/data/KDD99/NSL-KDD/test/Train_data.csv')
train_data = train_data.drop(['level'], axis=1)
test_data = pd.read_csv('F:/data/KDD99/NSL-KDD/test/Test_data.csv')
test_data = test_data.drop(['level'], axis=1)

data_list = [train_data,test_data]

for data in data_list:
    #특징 유형 식별
    print(data.dtypes)

    #특징 데이터 추출
    df_protocol = data['protocol_type']
    df_service = data['service']
    df_flag = data['flag']

    #특징별 개수 파악
    print(str(list(set(df_protocol)))+" : "+str(len(list(set(df_protocol)))))
    print(str(list(set(df_service)))+" : "+str(len(list(set(df_service)))))
    print(str(list(set(df_flag)))+" : "+str(len(list(set(df_flag)))))

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(df_protocol)
    print("\nprotocol_type("+str(len(list(set(df_protocol))))+") : "+str(le.classes_))
    trans_protocol = le.transform(df_protocol)
    print(df_protocol.head(10))
    print(trans_protocol[:10])

    data['protocol_type'] = trans_protocol

    le = preprocessing.LabelEncoder()
    le.fit(df_service)
    print("\nservice("+str(len(list(set(df_service))))+") : "+str(le.classes_))
    trans_service = le.transform(df_service)
    print(df_service.head(10))
    print(trans_service[:10])

    data['service'] = trans_service

    le = preprocessing.LabelEncoder()
    le.fit(df_flag)
    print("\nflag("+str(len(list(set(df_flag))))+") : "+str(le.classes_))
    trans_flag = le.transform(df_flag)
    print(df_flag.head(10))
    print(trans_flag[:10])

    data['flag'] = trans_flag

    print("\n")
    print(data.head(10))

train_data.to_csv('dataset/train_data.csv', index=False)
test_data.to_csv('dataset/test_data.csv', index=False)

#특징 타입 변환 확인
print(train_data.dtypes)