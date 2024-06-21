from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("lena.tiff")
img_data = np.array(img.convert("F"))
print(img_data.shape)
print(img_data)

# 缩放图像 resize 不对原图进行缩放，thumbnail直接对原图进行缩放
arr_img_new = img.resize((64,64))
plt.figure(figsize=(10,10))
plt.subplot(221)
plt.axis("off")
plt.imshow(img_data, cmap="gray")

plt.subplot(222)
plt.axis("off")
plt.imshow(arr_img_new, cmap="gray")

plt.subplot(223)
plt.axis("off")
# 旋转
plt.imshow(img.transpose(Image.FLIP_LEFT_RIGHT), cmap="gray")

plt.subplot(224)
plt.axis("off")
# 裁剪
plt.imshow(img.crop((100,100,400,400)), cmap="gray")
plt.show() 