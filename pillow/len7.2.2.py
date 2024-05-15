from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("lena.tiff")
# 图像转数组 灰度图像转二维数组，RGB图像转三维数组
img_data = np.array(img.convert("F"))
print(img_data.shape)
print(img_data)

# 图像颜色反向
arr_img_new = 255 - img_data
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.axis("off")
plt.imshow(img_data, cmap="gray")

plt.subplot(122)
plt.axis("off")
plt.imshow(arr_img_new, cmap="gray")

plt.show() 