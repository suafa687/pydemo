import tensorflow as tf
import numpy as np
import pandas as pd

t1 = tf.constant(np.arange(6).reshape(2,3))
t2 = tf.constant(np.arange(6).reshape(3,2))

# 相同维数向量乘法
print(tf.matmul(t1, t2))
print(t1@t2)
print("-"*20)

# 不同维数向量乘法 最后两维矩阵乘法 (2,3,5) X (5,4) = (2,3,4)
t3 = tf.random.normal([2,3,5])
t4 = tf.random.normal([5,4])
print(t3,"\n",t4,"\n",t3@t4)
print("-"*20)

# 三维 X 三维 最后两维矩阵乘法
t5 = tf.constant(np.arange(12).reshape(2,2,3))
t6 = tf.constant(np.arange(12).reshape(2,3,2))
print(t5,"\n",t6,"\n",t5@t6)
print("-"*20)

# 四维 X 四维 最后两维矩阵乘法
t7 = tf.constant(np.arange(24).reshape(2,2,2,3))
t8 = tf.constant(np.arange(24).reshape(2,2,3,2))
print(t7,"\n",t8,"\n",t7@t8)
print("-"*20)

# 求和
print(tf.reduce_sum(t1,axis=0))