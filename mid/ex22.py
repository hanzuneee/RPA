import pandas as pd

data = {'열1': [1, 2, 2, 3, 4],
    '열2': ['A', 'B', 'B', 'C', 'D'],
    '열3': [-10, 20, 30, 40, 150],
    '열4': ['X', 'Y', 'X', 'Z', 'Z']}

df = pd.DataFrame(data)

#위 데이터프레임에서 ‘열3’에 대한 평균을 출력하는 코드를 쓰시오.
data_mean = df['열3'].mean()
print(data_mean)

# 위 데이터프레임에서 ‘열3’에 대한 사분위수를 출력하는 코드를 쓰시오. 
data_quantile = df['열3'].quantile([0.25, 0.5, 0.75])
print(data_quantile)

#위 데이터프레임에서 ‘열2’의 중복데이터를 처리하는 코드를 쓰시오. 
df.drop_duplicates(subset=['열2'])

#위 데이터프레임에서 ‘열4’의 ’Z’값을 ‘F’로 수정하는 코드를 쓰시오. 
df.loc[df['열4'] == 'Z', '열4'] = 'F'