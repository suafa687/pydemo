import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax3d = Axes3D(fig)
fig.add_axes(ax3d)


# 散点图
x = np.random.uniform(10, 40, 30)
y = np.random.uniform(100, 200, 30)
z = 2*x + y
# ax3d.scatter(x,y,z,c='b', marker="*")

# 平面图
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
# np.meshgrid() 网格坐标((4,4),(4,4))
X,Y = np.meshgrid(x,y)
Z = 2*X+Y
# ax3d.plot_surface(X,Y,Z,cmap="rainbow")

# 线框图
#ax3d.plot_wireframe(X,Y,Z,color="m", linewidth=0.5)

# 曲面
Z = np.sin(np.sqrt(X**2+Y**2))
ax3d.plot_surface(X,Y,Z,cmap="rainbow")

ax3d.set_xlabel("X")
ax3d.set_xlabel("Y")
ax3d.set_xlabel("Z=2X+y")
plt.show()
