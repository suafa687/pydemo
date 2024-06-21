import tensorflow as tf
import numpy as np
import pandas as pd

t1 = tf.range(10)
print(t1[::], t1[::2], t1[4::-1])

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_file_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)
Names = ["h1","h2","h3","h4","h5"]
df_data = pd.read_csv(train_file_path,header=0,names=Names)
np_data = np.array(df_data)
tf_data = tf.convert_to_tensor(np_data)
print(type(df_data), type(np_data), type(tf_data), tf_data.shape)
# 二维张量：前5个样本中割2个取值，前4个属性隔2个取值
print(tf_data[0:5:2,0:4:2])
print("-"*20)

# 手写数字，三维张量
mnist = tf.keras.datasets.mnist
(tran_x,tran_y),(test_x, test_y) = mnist.load_data()
print(tran_x.shape)
# 第一张图片
print(tran_x[0,::,::])
print("-"*20)

t2 = tf.range(5)
# 对一维数组索引采样
t3 = tf.gather(t2, indices=[0,2,3])
print(t3)

t4 = tf.range(24)
t5 = tf.reshape(t4, [4,6])
# 对多维数组按着轴索引采样
t6 = tf.gather(t5, axis=0, indices=[0,2,3])
print(t6)

# 对多维数组按着坐标索引采样
t7 = tf.gather_nd(t5,[[0,0],[1,1],[2,3]])
print(t7)