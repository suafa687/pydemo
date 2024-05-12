import matplotlib.pyplot as plt

# num：编号或名称，figsize:绘图对象宽高，单位英寸，dpi:分辨率，默认=80,
# facecolor:背景颜色，edgecolor：边框颜色，frameon:是否显示边框
plt.figure(num="名称", figsize=(9,6), dpi=100, facecolor="green", edgecolor="red", frameon=True)
# plt.plot()
# 设置中文字体
plt.rcParams["font.sans-serif"]="SimHei"
# 恢复RC默认设置
#plt.rcdefaults()
plt.suptitle("全局标题",fontsize=20, color="r", backgroundcolor="y")

plt.subplot(221)
plt.title("子标题1")

plt.subplot(222)
plt.title("子标题2", loc="left", color="b")

plt.subplot(223)
myfontdict={"fontsize":12,"color":"w","backgroundcolor":"y", "rotation":30}
plt.title("子标题3", fontdict=myfontdict)

# 自动调整子图布局，避免子图覆盖[left, bottom,right,top]
plt.tight_layout(rect=[0,0,1,0.9])

plt.show()