import numpy as np

xarr = [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 
                 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21]
yarr = [145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30]
x_testarr = [128.15, 45.00, 141.43, 106.27, 99.00, 53.84, 85.36, 70.00]

x = np.array(xarr)
y = np.array(yarr)
x_test = np.array(x_testarr)

# np.mean 求数组均值
meanX = np.mean(x)
meanY = np.mean(y)

sumXY = np.sum((x-meanX)*(y-meanY))
sumX = np.sum((x-meanX)*(x-meanX))
w = sumXY/sumX
b = meanY - w*meanX
print(w, b)

y_pred = w*x_test+b
for i in range(y_pred.size) :
    print(x_testarr[i], "\t", np.round( y_pred[i], 2))