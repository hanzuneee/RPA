import pandas as pd 
#빈칸1
import matplotlib.pyplot as plt 
import matplotlib.font_manager as font_manager

def addtext(x, y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,y[i], ha = 'center')
    
hat = pd.read_csv('ch4-1.csv') # hat 변수에 데이터셋 입력 
print(hat.head(), end="\n\n") # 위에서 부터 5개 데이터 확인

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))

plt.title('hatchery statistics')

#빈칸2
plt.bar(hat['hatchery'], hat['chick'], color = ('red','orange','yellow','green','blue','navy', 'purple'))

plt.xlabel('hatchery')
plt.ylabel('chick count')

addtext(hat['hatchery'], hat['chick'])

#빈칸3
plt.show()