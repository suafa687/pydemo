import tensorflow as tf
import numpy as np

x=np.array([1.,2.,3.,4.])
w = tf.Variable(1.)
b = tf.Variable(1.)
pred = 1/(1/tf.exp(-(w*x+b)))
print(pred)

y= np.array([0,0,1,1])
# 交叉熵损失
Loss = -tf.reduce_sum(y*tf.math.log(pred) + (1-y)*tf.math.log(1-pred))
print("交叉熵损失", Loss)
# 平均交叉熵损失
AVG_Loss = -tf.reduce_mean(y*tf.math.log(pred) + (1-y)*tf.math.log(1-pred))
print("平均交叉熵损失", Loss)

pred = np.array([0.1,0.2,0.8,0.49])
# 四舍五入
classfy = tf.round(pred)
print("二分类", classfy)

# 预测值和标签值比较
res = tf.equal(classfy, y)
print("检验", res)

resi = tf.cast(res, tf.int8)
print("检验int", resi)

avg = tf.reduce_mean(tf.cast(res, tf.float32))
print("准确率", avg)

# tf.where(condition,a,b) ,condition为true则返回a, 为false则返回b
classfy = tf.where(pred < 0.5, 0, 1)
print("二分类", classfy)

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
res = tf.where(pred < 0.5, a, b)
print("检验", res)



