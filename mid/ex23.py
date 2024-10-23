import pandas as pd

data = {'이름' : ['유정', '유나', '민영', '은지'],
    '나이' : [30, 28, 31, 29],
    '생일' : ['1991.5.2', '1993.4.6', '1990.9.12', '1992.7.19']}

df1 = pd.DataFrame(data)

# 위 데이터프레임에서 첫번째 행을 출력하시오. 
print(df1.loc[0])

# 위 데이터프레임에서 ‘이름’ 열을 출력하시오. 
col_name = df1['이름']
print(col_name)

# 위 데이터프레임에서 이름이 ‘유나’인 행을 출력하시오. 
row_yuna = df1.loc[df1['이름'] == '유나']
print(row_yuna)

# 위 데이터프레임에서 나이가 30이상인 행을 출력하시오
row_age30 = df1.loc[df1['나이'] >= 30]
print(row_age30)