import pandas as pd

data = {
'과목번호' : ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
'과목명' : ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의 세계'],
'강의실' : ['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
'시간수' : [3, 2, 3, 4, 2, 1]
}
df = pd.DataFrame(data)

# ‘경영학’ 과목의 강의실만 출력하는(셀 추출) 코드를 작성하시오.
cell_name = df.loc[2]['강의실']
print(cell_name)

# 데이터프레임을 CSV파일로 저장하는 코드를 작성하시오.
#  * 'lecture.csv'이름으로 저장
df.to_csv("lecture.csv", header=True, index=False)

# 다음 출력 결과를 쓰시오. 
print(df.iloc[0:3, 1:3], end='\n\n')
#     과목명       강의실
# 0  인공지능개론   R1
# 1  웃음치료       R2
# 2  경영학         R3

