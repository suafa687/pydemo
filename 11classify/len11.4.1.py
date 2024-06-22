import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10,3))

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_file_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)

df_iris = pd.read_csv(train_file_path,header=0)
# shape = (120, 5), 120条样本，每个样本有5列，前4列是属性，第5列是标签（分类）
iris = np.array(df_iris)

# 取所有样本的前2列属性，花萼的长度和宽度
train_x =  iris[:,0:2]
# 取所有样本的最后一列标签
train_y = iris[:,4]

# 只取标签为0和1的数据，山鸢尾和变色鸢尾
x_train = train_x[train_y < 2]
y_train = train_y[train_y < 2]

num = len(x_train)
print(num)

# 属性中心化
x_train = x_train - np.mean(x_train, axis=0)
x0_train = np.ones(num).reshape(-1,1)
X = tf.cast(tf.concat((x0_train, x_train), axis = 1), tf.float32)
Y = tf.cast(y_train.reshape(-1,1), tf.float32)

# 超参数
learn_rate = 0.2
iter = 120
display_step = 30

np.random.seed(612)
W=tf.Variable(np.random.randn(3,1), dtype=tf.float32)

ce = []
acc = []

for i in range(0, iter+1):
    with tf.GradientTape() as tape:
        PRED = 1/(1+tf.exp(-tf.matmul(X,W)))
        Loss = -tf.reduce_mean(Y*tf.math.log(PRED) + (1-Y)*tf.math.log(1-PRED))
    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.where(PRED.numpy()<0.5, 0. ,1.), Y), tf.float32))
    ce.append(Loss)
    acc.append(accuracy)
    dL_dw= tape.gradient(Loss, W)
    W.assign_sub(learn_rate*dL_dw)

    if i%display_step == 0:
        print("i:%i, Loss:%f, Accuracy:%f" %(i, Loss, accuracy))


plt.subplot(121)
cm_pt = mpl.colors.ListedColormap(["blue","red"])
plt.scatter(x_train[:,0], x_train[:,1], c=y_train, cmap=cm_pt)
x_ = [-1.5, 1.5]
y_ = -(W[0] + W[1]*x_)/W[2]
plt.plot(x_, y_, color = 'g')

plt.subplot(122)
plt.plot(ce, color="blue", label = "Loss")
plt.plot(acc, color="red", label = "acc")
plt.legend()
plt.show()