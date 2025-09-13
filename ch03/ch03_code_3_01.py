import pandas as pd

# 리스트를 사용하여 Series 생성
data = [10, 20, 30, 40]
series1 = pd.Series(data)
print(series1)

# 인덱스를 지정하여 Series 생성
index_labels = ['A', 'B', 'C', 'D']
series2 = pd.Series(data, index=index_labels)
print(series2)

# 딕셔너리를 사용하여 Series 생성
data_dict = {'A': 100, 'B': 200, 'C': 300}
series3 = pd.Series(data_dict)
print(series3)