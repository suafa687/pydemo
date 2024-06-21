import tensorflow as tf
import numpy as np

t1 = tf.constant(np.arange(24).reshape((2,3,4)))
t2 = tf.reshape(t1, shape=(3,8))
print(t1, t2)
print("-"*20)

t3 = tf.constant([[1,2],[3,4]])
# 增加维度，增加的维度长度为1
t4 = tf.expand_dims(t3, 1)
# 删除维度
t5 = tf.squeeze(t4, 1)
print(t3, t4, t5)
print("-"*20)

t6 = tf.range(24)
t7 = tf.reshape(t6,[2,3,4])
# 交换维度，改变张量的视图，同时改变张量的存储顺序
t8 = tf.transpose(t7, [2,0,1])
print(t6,t7,t8)
print("-"*20)

t9 = tf.constant([[1,2,3],[4,5,6]])
t10 = tf.constant([[11,12,13],[14,15,16]])
# 拼接张量
t11 = tf.concat([t9, t10],0)
t12 = tf.concat([t9, t10],1)
print(t11, t12)
print("-"*20)

# 张量分割
t13 = tf.reshape(tf.range(24), shape=(4,6))
t14, t15, t16 = tf.split(t13, [1,2,1], 0)
print(t13, t14, t15, t16)
print("-"*20)

# 张量堆叠
t17 = tf.stack((t9, t10),axis=0)
t18 = tf.stack((t9, t10),axis=1)
t19 = tf.stack((t9, t10),axis=2)
print(t17, t18, t19)
print("-"*20)

# 张量分解
t20, t21 = tf.unstack(t19, axis=2)
print(t20, t21)

