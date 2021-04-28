"""
    ioc_matching.py에서는 수집된 네트워크 데이터와 ioc 정보와의 매칭을 통해,
    ioc에 존재하는 위협들이 수집된 네트워크 데이터에 포함되어 있는 지 확인
"""
import pandas as pd
import numpy as np

def matching(data):
    # ioc 파일 호출
    ioc_data = pd.read_csv('F:/data/ioc/ioc_data.csv', encoding='cp949')

    print("\nioc matching...")
    #print(data.shape)

    if 'Link' in data.columns:
        print("Link matching")
        index_list = []

        temp_ioc = ioc_data.copy()
        temp_ioc['Link'].replace('', np.nan, inplace=True)
        temp_ioc.dropna(subset=['Link'], inplace=True)

        temp_data = data.copy()
        temp_data['Link'].replace('', np.nan, inplace=True)
        temp_data.dropna(subset=['Link'], inplace=True)

        for i in temp_data.index:
            if temp_data.loc[i, 'Link'] in temp_ioc['Link'].tolist():
                index_list.append(i)

        print("Detection Data : {}".format(len(index_list)))
        data = data.drop(index_list)
        data = data.drop(['Link'], axis=1)

    elif 'SHA-1' in data.columns:
        print("SHA-1 matching")
        index_list = []

        temp_ioc = ioc_data.copy()
        temp_ioc['SHA-1'].replace('', np.nan, inplace=True)
        temp_ioc.dropna(subset=['SHA-1'], inplace=True)

        temp_data = data.copy()
        temp_data['SHA-1'].replace('', np.nan, inplace=True)
        temp_data.dropna(subset=['SHA-1'], inplace=True)

        for i in temp_data.index:
            if temp_data.loc[i, 'SHA-1'] in temp_ioc['SHA-1'].tolist():
                index_list.append(i)

        print("Detection Data : {}".format(len(index_list)))
        data = data.drop(index_list)
        data = data.drop(['SHA-1'], axis=1)

    elif 'SHA-256' in data.columns:
        print("SHA-256 matching")
        index_list = []

        temp_ioc = ioc_data.copy()
        temp_ioc['SHA-256'].replace('', np.nan, inplace=True)
        temp_ioc.dropna(subset=['SHA-256'], inplace=True)

        temp_data = data.copy()
        temp_data['SHA-256'].replace('', np.nan, inplace=True)
        temp_data.dropna(subset=['SHA-256'], inplace=True)

        for i in temp_data.index:
            if temp_data.loc[i, 'SHA-256'] in temp_ioc['SHA-256'].tolist():
                index_list.append(i)

        print("Detection Data : {}".format(len(index_list)))
        data = data.drop(index_list)
        data = data.drop(['SHA-256'], axis=1)

    elif 'MD5' in data.columns:
        print("MD5 matching")
        index_list = []

        temp_ioc = ioc_data.copy()
        temp_ioc['MD5'].replace('', np.nan, inplace=True)
        temp_ioc.dropna(subset=['MD5'], inplace=True)

        temp_data = data.copy()
        temp_data['MD5'].replace('', np.nan, inplace=True)
        temp_data.dropna(subset=['MD5'], inplace=True)

        for i in temp_data.index:
            if temp_data.loc[i, 'MD5'] in temp_ioc['MD5'].tolist():
                index_list.append(i)

        print("Detection Data : {}".format(len(index_list)))
        data = data.drop(index_list)
        data = data.drop(['MD5'], axis=1)

    elif 'IP' in data.columns:
        print("IP matching")
        index_list=[]

        temp_ioc = ioc_data.copy()
        temp_ioc['IP'].replace('', np.nan, inplace=True)
        temp_ioc.dropna(subset=['IP'], inplace=True)

        temp_data = data.copy()
        temp_data['IP'].replace('', np.nan, inplace=True)
        temp_data.dropna(subset=['IP'], inplace=True)

        for i in temp_data.index:
            if temp_data.loc[i,'IP'] in temp_ioc['IP'].tolist():
                index_list.append(i)

        print("Detection Data : {}".format(len(index_list)))
        data = data.drop(index_list)
        data = data.drop(['IP'], axis=1)

    data = data[~data.isin([np.nan]).any(1)]
    #print(data.shape)

    return data