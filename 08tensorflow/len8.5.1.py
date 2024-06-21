import tensorflow as tf
import numpy as np
import pandas as pd

# t1 的 2次方，表示t1的每个元素2次方
t1 = tf.range(3)
t2 = tf.pow(t1, 2)
print(t2)

# t3 的 t4 次方，对t3 的 每个元素做 t4 对应位置元素次方
# 1的2次方，2的1次方，3的4次方，4的3次方
t3 = tf.constant([[1,2],[3,4]])
t4 = tf.constant([[2,1],[4,3]])
print(tf.pow(t3, t4))
print("-"*20)

t5 = tf.constant([[1.,9.],[16.,100.]])
t6 = tf.constant([[2.,3.],[2.,10.]])
print(tf.math.log(t5)/tf.math.log(t6))
print("-"*20)

# 张量广播，不同维度张量相加,最后一维长度先等就可以加
t7 = tf.constant([1,2,3])
t8 = tf.constant(np.arange(12).reshape([4,3]))
t9 = tf.constant(np.arange(12).reshape([2,2,3]))
print(t7,"\n",t8, "\n",t7+t8,"\n",t9,"\n", t7+t9)