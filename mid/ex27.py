import matplotlib.pyplot as plt
from matplotlib.font_manager import font_manager
import pandas as pd

hat = pd.read_csv('ch4-2.csv') 
print(hat.describe(), end="\n\n")

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

#빈칸1
plt.subplot(1, 2, 1)

plt.figure(figsize=(10, 17)) 

#빈칸2
plt.hist(hat.weight, bins=7)

plt.title('B 부화장 병아리 무게 분포 현황', fontsize= 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

plt.show()