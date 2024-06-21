import tensorflow as tf
import numpy as np

# 全零张量
t1 = tf.zeros(shape=(3,2))
# 全一张量
t2 = tf.ones(shape=(3,4))
t3 = tf.fill([3,4], 6)
t4 = tf.constant(6,shape=[3,4])
# 正态分布, 均值为0，标准差为2
t5 = tf.random.normal(shape=[2,2], mean=0.0, stddev=2.0)
# 阶段正态分布，2倍的标准差
t6 = tf.random.truncated_normal(shape=[2,2], mean=0.0, stddev=2.0)
# 设置随机种子
tf.random.set_seed(1000)
# 均匀分布张量,前闭后开
t7 = tf.random.uniform(shape=[2,2],minval=3,maxval=9, dtype=tf.int32)

t8 = tf.constant([[1,2],[3,4],[5,6]])
# 随机打乱，只打乱第一维度
t9 = tf.random.shuffle(t8)
t10 = tf.random.shuffle([1,2,3,4,5,6])
# 创建序列
t11 = tf.range(start=10, limit=100, delta=7)
print(t1,t2,t3, t4, t5, t6, t7, t8,t9, t10, t11)