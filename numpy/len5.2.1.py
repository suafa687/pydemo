import numpy as np
list1 = np.array([[[0,1,2,3], [0,1,2,3.1]], [[0,1,2,3.1], [0,1,2,"hello"]]], dtype=np.unicode_)
print(type(list1))
a = np.array(list1)
# 如果数据源本身已经是ndarray时，asarray不是复制，而array则是复制
b = np.asarray(list1)
list1[0][0][0] = "python"
# 维度， 形状， 元素总个数，元素数据类型，每个元素字节数
print(a, type(a), a.ndim, a.shape, a.size,a.dtype,a.itemsize)
print(a[0],a[1])
print(b[0],b[1])
print("-"*20)

print(np.arange(1,4,0.3))
# 创建元素为0的矩阵
print(np.zeros((3,2),dtype=np.int32))
# 创建元素为1的矩阵
print(np.ones((3,2),dtype=np.int32))
# 创建单位矩阵
print(np.eye(3,dtype=np.int32))
# 创建等差数列：起始1，结束24，合计12个元素
print(np.linspace(1,24,12,dtype=np.int32))
# 创建等比数列：3的1次方开始，3的6次方结束，合计6个
print(np.logspace(1,6,6,base=3,dtype=np.int32))