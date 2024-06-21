import matplotlib.pyplot as plt
import numpy as np

# 支持中文字体
plt.rcParams["font.sans-serif"]="SimHei"
# 正常显示负号
plt.rcParams["axes.unicode_minus"]=False

n = 24
y1 = np.random.randint(27,37,n)
y2= np.random.randint(40,60,n)

# 绘制折线图
plt.plot(y1,label="温度")
plt.plot(y2,label="湿度")
# 显示图例 loc:1=右上，2=左上，3=左下，4=右下
plt.legend(loc=2)

# 设置标题
plt.title("24小时温度湿度统计",fontsize=20)

# x轴，y轴范围
plt.xlim(0,23)
plt.ylim(20,70)

# x轴，y轴标签文本
plt.xlabel("小时",fontsize=14)
plt.ylabel("测量值",fontsize=14)

plt.show()
