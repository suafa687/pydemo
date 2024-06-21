import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y),(test_x, test_y) = boston_housing.load_data()
print(train_x.shape, train_y.shape)
print(test_x.shape, test_y.shape)

x_train = train_x[:,5]
y_train = train_y
x_test = test_x[:,5]
y_test = test_y

learn_rate = 0.04
iter = 2000
display_step = 200

np.random.seed(612)
w = tf.Variable(np.random.randn())
b = tf.Variable(np.random.randn())
mse_train = []
mse_test = []

for i in range(0, iter+1):
    with tf.GradientTape() as tape:
        pred_train = w*x_train+b
        Loss_train = 0.5*tf.reduce_mean(tf.square(y_train-pred_train))

        pred_test = w*x_test+b
        Loss_test = 0.5*tf.reduce_mean(tf.square(y_test-pred_test))
    mse_train.append(Loss_train)
    mse_test.append(Loss_test)

    dL_dw,dL_db= tape.gradient(Loss_train, [w,b])
    w.assign_sub(learn_rate*dL_dw)
    b.assign_sub(learn_rate*dL_db)

    if i%display_step == 0:
        print("i:%i, Train Loss:%f, Test Loss:%f" %(i, Loss_train, Loss_test))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(15,10))

plt.subplot(221)
plt.scatter(x_train, y_train,color="blue", label="data")
plt.plot(x_train,pred_train, color="red", label="model", linewidth=2)
plt.legend(loc="upper left")

plt.subplot(222)
plt.plot(mse_train,color="blue", label="train loss", linewidth=2)
plt.plot(mse_test, color="red", label="test loss", linewidth=2)
plt.legend(loc="upper right")

plt.subplot(223)
plt.plot(y_train,color="blue", label="train_price", marker="*")
plt.plot(pred_train,color="red", label="pridict", marker=".")
plt.legend()

plt.subplot(224)
plt.plot(y_test,color="blue", label="train_price", marker="*")
plt.plot(pred_test,color="red", label="pridict", marker=".")
plt.legend()

plt.show()