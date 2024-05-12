import numpy as np

# 矩阵

ar1 = np.arange(6).reshape(2,3)
ma1 = np.mat(ar1, dtype=np.int32)
print(type(ar1),"\n"*2, ar1,"\n"*2, type(ma1),"\n"*2, ma1)
# 矩阵维数， 形状， 元素个数， 数据类型
print(ma1.ndim, ma1.shape, ma1.size, ma1.dtype)
print("-"*20)

# 矩阵乘法
ar2 = np.arange(6).reshape(3,2)
ma2 = np.mat(ar2, dtype=np.int32)
print(ma1,"\n"*2, ma2,"\n"*2, ma1*ma2)
print("-"*20)

# 矩阵转置
print(ma1, "\n"*2, ma1.T)
print("-"*20)

# 矩阵逆
print(ma1, "\n"*2, ma1.I, "\n"*2)
print(ma1*ma1.I)
print("-"*20)
print("-"*20)

# 随机数
# 创建(2,3)形状的随机数，数值在[0,1)之间
print(np.random.rand(2,3))
print(np.random.rand(2))
print(np.random.rand())

# 创建(3,2)形状的随机数，数值在[1,5)之间
print(np.random.uniform(1,5,(3,2)))

# 创建(3,2)形状的随机数，数值在[1,5)之间
print(np.random.randint(1,5,(3,2)))

# 创建(3,2)形状的随机数，符合标准正态分布
print(np.random.randn(3,2))

# 创建(3,2)形状的随机数，符合正态分布,均值100，方差5
print(np.random.normal(100,5,(3,2)))

# 随机种子，经一次有效，默认系统时钟为随机种子
np.random.seed(100)

# 打乱函数，针对高维数组只打乱第一层
ar1 = np.arange(10)
np.random.shuffle(ar1)
print(ar1)