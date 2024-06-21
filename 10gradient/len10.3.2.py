import numpy as np
import tensorflow as tf

x = tf.Variable(3.0)
y = tf.Variable(4.0)
with tf.GradientTape() as tape:
    f = tf.square(x) + 2*tf.square(y) +1

# tape.gradient(函数，自变量) 多元函数求导
df_dx, df_dy = tape.gradient(f,[x,y])
print(f)
print(df_dx, df_dy)
print("---------------")

# 二阶导数
with tf.GradientTape() as tape2:
    with tf.GradientTape() as tape1:
        f = tf.square(x) + 2*tf.square(y) +1
    first_grads = tape1.gradient(f,[x,y])
second_grads = tape2.gradient(first_grads,[x,y])

print(f)
print(first_grads)
print(second_grads)