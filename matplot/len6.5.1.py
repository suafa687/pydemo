import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_file_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)

Names = ["h1","h2","h3","h4","h5"]
df_data = pd.read_csv(train_file_path,header=0,names=Names)
# 读取前8行数据
print(df_data.head(8))
# 读取后8行数据
print(df_data.tail(8))

# pandas数据集转化为numpy格式
print(type(df_data))
print(type(df_data.values))
print(type(np.array(df_data)))

iris = np.array(df_data)
print(iris[:,2])
plt.scatter(iris[:,2], iris[:,3], c=iris[:,4], cmap='brg')
plt.title("Iris")
plt.show()