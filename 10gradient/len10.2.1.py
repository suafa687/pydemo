import numpy as np
import matplotlib.pyplot as plt

# 房屋面积
x = np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 
                 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
# 房间数
x2 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
# 房屋总价
y = np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])
# 学习率
learn_rate = 0.00001
# 迭代次数
inter = 100
display_step = 10

np.random.seed(612)
w = np.random.randn()
b = np.random.randn()
mse = []
for i in range(0, inter + 1):
    dL_dw = np.mean(x*(w*x+b-y))
    dL_db = np.mean(w*x+b-y)
    w=w-learn_rate*dL_dw
    b=b-learn_rate*dL_db
    pred = w*x+b
    Loss = np.mean(np.square(y-pred))/2
    mse.append(Loss)
    
    if i%display_step == 0:
        print("i:%i, Loss:%f, w:%f, b:%f" %(i, mse[i], w,b))


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure()
plt.plot(mse, color="green", label="损失变化曲线", linewidth=2)

plt.xlabel("Iteration", fontsize=14)
plt.ylabel("Loss", fontsize=14)
plt.show()