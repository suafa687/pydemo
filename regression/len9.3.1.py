

xarr = [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 
                 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21]
yarr = [145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30]
x_testarr = [128.15, 45.00, 141.43, 106.27, 99.00, 53.84, 85.36, 70.00]

arrMeanX = sum(xarr)/len(xarr)
arrMeanY = sum(yarr)/len(yarr)
sumXY = 0.0
sumX = 0.0
for i in range(len(xarr)):
    sumXY += (xarr[i]-arrMeanX)*(yarr[i]-arrMeanY)
    sumX += (xarr[i]-arrMeanX)*(xarr[i]-arrMeanX)

w = sumXY/sumX
b = arrMeanY - w* arrMeanX
print(w, b)

for i in range(len(x_testarr)) :
    print(x_testarr[i], "\t", round( w*x_testarr[i] + b, 2))
