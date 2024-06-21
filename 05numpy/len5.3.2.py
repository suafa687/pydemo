import numpy as np

# 多维数组

# 元素求和
a=np.arange(4)
print(a.sum())
print("-"*20)

# 轴上的元素求和
b=np.arange(12).reshape(3,4)
print(b.sum(axis=0), "\n", b.sum(axis=1))
print("-"*20)

t=np.arange(24).reshape(2,3,4)
print(t.sum(axis=0), "\n"*2, t.sum(axis=1), "\n"*2, t.sum(axis=2))
print("-"*20)

# 数组堆叠
x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.stack((x,y),axis=0), "\n"*2, np.stack((x,y),axis=1))
print("-"*20)
z = np.array([7,8,9])
print(np.stack((x,y,z),axis=0), "\n"*2, np.stack((x,y,z),axis=1))
print("-"*20)

i = np.arange(0,9).reshape(3,3)
j = np.arange(10,19).reshape(3,3)
print(np.stack((i,j),axis=0), "\n---\n", np.stack((i,j),axis=1), "\n---\n", np.stack((i,j),axis=2))
print("-"*20)