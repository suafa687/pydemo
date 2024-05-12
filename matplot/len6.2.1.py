import matplotlib.pyplot as plt
import numpy as np

# 支持中文字体
plt.rcParams["font.sans-serif"]="SimHei"
# 正常显示负号
plt.rcParams["axes.unicode_minus"]=False

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
m = np.random.uniform(-4,4,(1,n))
n = np.random.uniform(-4,4,(1,n))

# 绘制数据点
plt.scatter(x,y,color="b",marker=".",label="正态分布")
plt.scatter(m,n,color="y",marker=".",label="均匀分布")
# 显示图例 loc:1=右上，2=左上，3=左下，4=右下
plt.legend(loc=2)

# 设置标题
plt.title("标准正态分布",fontsize=20)

# 显示文本
plt.text(2.5,2.5,"均 值：0\n标准差：1")

# x轴，y轴范围
plt.xlim(-4,4)
plt.ylim(-4,4)

# x轴，y轴标签文本
plt.xlabel("横坐标x",fontsize=14)
plt.ylabel("横坐标y",fontsize=14)

plt.show()
