import pandas as pd

data = {
    '과목번호': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명': ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의 세계'],
    '강의실': ['R1', 'R2', 'R3', 'R4', 'R2', 'R3'],  # R5, R6 대신 기존에 맞는 값 사용
    '시간수': [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df, end='\n\n')

sr_name = df['과목명']
print(sr_name, end='\n\n')

sr_no = df.loc[2]
print(sr_no, end='\n\n')

cell_name = df.loc[2]['강의실']
print(cell_name)

df.to_csv('file.csv', index=False)

print("###################################################")

df['담당교수'] = ['홍길동', '김철수', '이영희', '박영수', '최영희', '김영수']
print(df, end='\n\n')

df.loc[6] = ['C7', '통계학', 'R7', 3, '이철수']  # 새 행 추가
print(df, end='\n\n')

df1 = df.drop(['강의실'], axis=1)  # '강의실' 열 삭제
print(df1, end='\n\n')

df2 = df.drop([5], axis=0)  # 5번째 행 삭제
print(df2, end='\n\n')

print("###################################################")
# 범위 찾기
# 행 찾기
print(df.loc[0:2], end='\n\n')
print(df.iloc[0:2], end='\n\n')
# 열 찾기
print(df.loc[:, '강의실':'담당교수'], end='\n\n')

print("###################################################")

# 조건 찾기
# 행 찾기
print(df['과목명'] == '경영학', end='\n\n')
print(df.loc[df['과목명'] == '경영학'], end='\n\n')
print(df.loc[df['시간수'] > 2], end='\n\n')

# 셀 찾기 
print(df.loc[df['과목명'] == '경영학']['담당교수'], end='\n\n')
print(df.loc[df['과목명'] == '경영학']['담당교수'].values[0], end='\n\n')

# df.loc[3]['담당교수'] = '이경영'
df.loc[3, '담당교수'] = '이경영'
print(df, end='\n\n')

#df.loc[df['과목명'] == '경영학','담당교수'] = '이경영'
df.loc[df['과목명'] == '경영학'] ['담당교수'] = '이경영'
print(df, end='\n\n')

print(df.loc[df['과목명'] == '경영학', '담당교수'].values[0], end='\n\n')
