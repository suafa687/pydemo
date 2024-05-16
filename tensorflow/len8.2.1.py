import tensorflow as tf
import numpy as np

print(tf.__version__)

print(tf.executing_eagerly())

tensor1 = tf.constant([[1,2],[3,4]])
print("-"*20)
print(tensor1)
print("-"*20)
print(tensor1.numpy())
print("-"*20)
t1 = tf.constant(1.0)
print(t1)
print("-"*20)
# np 浮点数默认64，TensorFlow默认32浮点数
t2 = tf.constant(np.array([1.,2.]))
print(t2)
print("-"*20)
# np 浮点数默认64，TensorFlow默认32浮点数
t3 = tf.constant(np.array([False,True]))
print(t3)
# 类型转换
t4 = tf.cast(t3, tf.int32)
print(t4)
print("-"*20)
na = np.arange(12).reshape((3,4))
ta = tf.convert_to_tensor(na)
print(type(na), type(ta))
print(tf.is_tensor(na), tf.is_tensor(ta))
