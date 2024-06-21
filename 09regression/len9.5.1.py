import numpy as np

# 房屋面积
x1 = np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 
                 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
# 房间数
x2 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
# 房屋总价
y = np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

# 生成一维数组
x0 = np.ones(len(x1))

# np.stack() 数组堆叠，现在axis轴上给被堆叠数组加上一维，再在axis轴上将多个数组该维堆放一起
X = np.stack(( x1, x2, x0), axis=1)
# np.reshape() 改变数组形状，-1 表示未知的维数，np根据数据和另外一个维度维数自动推导 -1 的真实维数
Y = np.array(y).reshape(-1, 1)
# np.transpose() 矩阵转置
Xt = np.transpose(X)
# np.linalg.inv() 矩阵求逆
XtX_1 = np.linalg.inv(np.matmul(Xt, X))
# np.matmul() 矩阵相乘
XtX_1_Xt = np.matmul(XtX_1, Xt)
# W = [(X(T)*X)(-1)]*X(T)*Y
W = np.matmul(XtX_1_Xt, Y)
print(W)

x1_test = float(input("商品房面积："))
x2_test = int(input("房间数："))
y_pred = W[0]*x1_test + W[1]*x2_test+W[2]
print("预测价格：",np.round(y_pred, 2), "万元")

