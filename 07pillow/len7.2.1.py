from PIL import Image
import matplotlib.pyplot as plt

# img = Image.open("lena.png")
img = Image.open("lena.tiff")
# img.save("lena.bmp")
# img.save("lena.jpeg")

# 格式，图像大小，颜色模式
print(img.format, img.size, img.mode)

# 分离三个通道
img_r, img_g, img_b = img.split()

plt.figure(figsize=(15,15))
plt.subplot(331)
# 关闭坐标轴
plt.axis("off")
# 合并三个通道
plt.imshow(Image.merge("RGB",[img_r,img_g,img_b]))
plt.title(img.format)

plt.subplot(332)
# 关闭坐标轴
plt.axis("off")
plt.imshow(Image.merge("RGB",[img_r,img_g,img_b]))
plt.title(img.format)

img_gray = img.convert("F")
plt.subplot(333)
plt.axis("off")
plt.imshow(img_gray)
plt.title("gray")


plt.subplot(334)
plt.axis("off")
# , cmap="gray" 采用灰度图表示颜色的亮度
plt.imshow(img_r, cmap="gray")
plt.title("R")

plt.subplot(335)
plt.axis("off")
plt.imshow(img_g, cmap="gray")
plt.title("G")

plt.subplot(336)
plt.axis("off")
plt.imshow(img_b, cmap="gray")
plt.title("B")

plt.show()