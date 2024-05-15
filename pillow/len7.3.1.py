import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(tran_x,tran_y),(test_x, test_y) = mnist.load_data()
print(len(tran_x), len(test_x))
print(tran_y.shape, test_x.shape)
print(tran_x[0])

for i in range(4):
    num = np.random.randint(1, 50000)
    plt.subplot(1,4,i+1)
    plt.axis("off")
    plt.imshow(tran_x[num], cmap="gray")
    plt.title(tran_y[num])

plt.show()