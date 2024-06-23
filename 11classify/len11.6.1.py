import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_file_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)

df_iris_train = pd.read_csv(train_file_path,header=0)
iris_train = np.array(df_iris_train)
# 取所有样本的第2，3列属性，花萼的长度和宽度
x_train =  iris_train[:,2:4]
# 取所有样本的最后一列标签
y_train = iris_train[:,4]

num_train = len(x_train)
x0_train = np.ones(num_train).reshape(-1,1)
X_train = tf.cast(tf.concat((x0_train, x_train), axis = 1), tf.float32)
# 独热编码 one_hot(indices, depth) 
# indices:输入值，一维数组或张量
# depth:编码深度，编码位数
Y_train = tf.one_hot(tf.constant(y_train, dtype=tf.int32), 3)
print(Y_train)

# 超参数
learn_rate = 0.2
iter = 500
display_step = 100

np.random.seed(612)
W=tf.Variable(np.random.randn(3,3), dtype=tf.float32)

acc = []
cce = []

for i in range(0, iter+1):
    with tf.GradientTape() as tape:
        # softmax()根据输入数据得到各个数据的概率占比
        # 得到预测值的分类概率
        PRED_train = tf.nn.softmax(tf.matmul(X_train,W))
        Loss_train = -tf.reduce_sum(Y_train*tf.math.log(PRED_train))/num_train
    # tf.argmax() 计算最大元素，axis=1 取每行中的最大元素，PRED_train是预测出来的分类概率，找到预测值中概率最大的：转换为自然顺序码
    # 计算准确率
    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(PRED_train.numpy(),axis=1), y_train), tf.float32))
    acc.append(accuracy)
    cce.append(Loss_train)
    dL_dw= tape.gradient(Loss_train, W)
    W.assign_sub(learn_rate*dL_dw)

    if i%display_step == 0:
        print("i:%i, Loss:%f, Accuracy:%f" %(i, Loss_train, accuracy))

M = 500
x1_min, x2_min = x_train.min(axis = 0)
x1_max, x2_max = x_train.max(axis = 0)
t1 = np.linspace(x1_min, x1_max, M)
t2 = np.linspace(x2_min, x2_min, M)
m1,m2 = np.meshgrid(t1, t2)
m0 = np.ones(M*M)
X_ = tf.cast(np.stack((m0,m1.reshape(-1), m2.reshape(-1)), axis=1),tf.float32)
Y_ = tf.nn.softmax(tf.matmul(X_,W))
Y_ = tf.argmax(Y_.numpy(), axis=1)
n = tf.reshape(Y_,m1.shape)

plt.figure(figsize=(8,6))
cm_bg = mpl.colors.ListedColormap(["#A0FFA0","#FFA0A0","#A0A0FF"])
plt.pcolormesh(m1, m2, n, cmap=cm_bg)
plt.scatter(x_train[:,0], x_train[:,1], c=y_train, cmap="brg")

plt.show()

