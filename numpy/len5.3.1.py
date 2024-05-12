import numpy as np

arr = np.arange(12)
print(arr)
# reshape 不改变源数组
arr1 = arr.reshape(3,4)
print(arr1)
print(arr)
print("-"*20)

# resize 改变源数组
arr.resize(3,4)
print(arr)
# -1 自动计算维度
arr2 = arr.reshape(-1,2)
print(arr2)
print(arr2.reshape(-1))
print("-"*20)

ar1 = np.arange(4)
ar2 = np.arange(12).reshape(3,4);
print(ar1, "\n"*2, ar2, "\n"*2, ar2*2, "\n"*2,ar2**2, "\n"*2, ar1+ar2)
print("-"*20)

a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
print(a*b)
# 矩阵乘法
print(np.matmul(a,b))
print("-"*20)

# 矩阵转置
print(np.transpose(a), "\n"*2, np.transpose(b), "\n"*2)
print(np.linalg.inv(a), "\n"*2,np.linalg.inv(a))
