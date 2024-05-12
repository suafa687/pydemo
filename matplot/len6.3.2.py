import matplotlib.pyplot as plt
import numpy as np

# 支持中文字体
plt.rcParams["font.sans-serif"]="SimHei"
# 正常显示负号
plt.rcParams["axes.unicode_minus"]=False

n = 24
y1 = np.random.randint(5,30,n)
y2 = np.random.randint(-30,-5,n)

# 绘制柱状图
plt.bar(range(len(y1)), y1,label="统计量1")
plt.bar(range(len(y1)), y2,label="统计量2")
# 显示图例 loc:1=右上，2=左上，3=左下，4=右下
plt.legend(loc=2)

# 设置标题
plt.title("柱状图",fontsize=20)

plt.show()
