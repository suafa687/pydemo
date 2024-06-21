import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# 支持中文字体
plt.rcParams["font.sans-serif"]="SimHei"
# 正常显示负号
plt.rcParams["axes.unicode_minus"]=False

boston_housing = tf.keras.datasets.boston_housing

(train_x,train_y),(test_x,test_y) = boston_housing.load_data()

#print("training set:",len(train_x),type(train_x),train_x.ndim, train_x.shape)
#print("testing set:",len(test_x),type(test_x),test_x.ndim,test_x.shape)

plt.figure(figsize=(12,12))

for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel("参数")
    plt.ylabel("Price($1000's)")
    plt.title(str(i)+"."+" - Price")
plt.tight_layout()
plt.suptitle("各属性和房价的关系",x=0.5,y=1.02,fontsize=20)
plt.show()