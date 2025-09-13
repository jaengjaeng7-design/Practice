#코드 3-14 데이터 탐색의 예

import pandas as pd

df_duplicates = pd.DataFrame({
    '이름': ['김철수', '이영희', '김철수'],
    '나이': [25, 30, 25],
    '점수': [90 ,85, 90]
})

#데이터 기본 정보 확인
print(df.info()) #데이터 타입, 결측치 여부 확인

#데이터 요약 통계 확인
print(df.info()) #숫자형 데이터의 기초 통계 정보 확인

#데이터 크기 및 형태 확인
print(df.shape) # (행 개수, 열 개수)
print(df.columns) # 열 이름 리스트
print(df.index) # 인덱스 정보