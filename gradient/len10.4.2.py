import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 房屋面积
area = np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 
                 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
# 房间数
room = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
# 房屋总价
price = np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

x0 = np.ones(len(area))
x1 = (area - area.min())/(area.max()-area.min())
x2 = (room - room.min())/(room.max()-room.min())

X = np.stack((x0, x1, x2), axis = 1)
Y = price.reshape(-1, 1)

learn_rate = 0.2
iter = 50
display_step = 5

np.random.seed(612)
W = tf.Variable(np.random.randn(3,1))

mse=[]
for i in range(0, iter+1):
    with tf.GradientTape() as tape:
        pred = tf.matmul(X,W)
        Loss = 0.5*tf.reduce_mean(tf.square(Y-pred))
    mse.append(Loss)
    dL_dw = tape.gradient(Loss, W)
    W.assign_sub(learn_rate*dL_dw)

    if i%display_step == 0:
        print("i:%i, Loss:%f" %(i, Loss))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure()
plt.plot(mse, color="green", label="损失变化曲线", linewidth=2)

plt.xlabel("Iteration", fontsize=14)
plt.ylabel("Loss", fontsize=14)
plt.show()