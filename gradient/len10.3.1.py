import numpy as np
import tensorflow as tf

# tf.Variable 可训练变量
x = tf.Variable(3.0)
# GradientTape梯度带
with tf.GradientTape() as tape:
    y = tf.square(x)

# tape.gradient(函数，自变量)
dy_dx = tape.gradient(y,x)
print(y)
print(dy_dx)

# persistent 默认为False, 只能求导一次。
# 通过设置为True，可以对多个公式求导，但是在求导结束时需要使用 del 删除 tape
with tf.GradientTape(persistent=True) as tape:
    y = tf.square(x)
    z = pow(x,3)

dy_dx = tape.gradient(y,x)
dz_dx = tape.gradient(z,x)
print(y,z)
print(dy_dx, dz_dx)

del tape

# watch_accessed_variables 默认 True,自动监视X变量
# 如果设置为False,需要通过tape.watch()手动添加对变量的监视,watch还可以监视非可训练变量
i = tf.constant(3.0)
with tf.GradientTape(persistent=True, watch_accessed_variables=False) as tape:
    tape.watch(x)
    tape.watch(i)
    y = tf.square(x)
    z = pow(i,3)

dy_dx = tape.gradient(y,x)
dz_dx = tape.gradient(z,i)
print(y,z)
print(dy_dx, dz_dx)

del tape