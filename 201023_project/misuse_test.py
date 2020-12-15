"""
    data_set : 전체 데이터 셋(label 특징 포함)
    feature_names : 특징 이름
    feature_type : 특징 유형('categorical', 'numerical', 'numerical', 'label')
    -> 여기서는 discretization을 수행한 특징 셋이기 때문에 클래스를 제외한 나머지는 카테고리로 분류함

    데이터 업로드 -> 전처리 -> CBA 룰 추출 -> 룰 출력
"""
import cba.cba_rg as cba_rg
import pandas as pd

print("\nData set Upload")
TD_misuse_data = pd.read_csv('F:/data/ADD/201023_data/disc_data.csv')
TD_misuse_data = TD_misuse_data.to_numpy()

print("\nCBA - Make Rule")
minsup = 0.1
minconf = 0.1
cars = cba_rg.rule_generator(TD_misuse_data, minsup, minconf)

print("\nCARs:")
cars.print_rule()