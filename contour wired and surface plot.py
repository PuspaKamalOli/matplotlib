import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_z(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x_1 = np.linspace(-6, 6, 30)
y_1 = np.linspace(-6, 6, 30)
x_1, y_1 = np.meshgrid(x_1, y_1)
z = get_z(x_1, y_1)
fig = plt.figure(figsize=(6, 6), dpi=300)
axes = fig.add_axes([0, 0, 0.8, 0.8], projection='3d')
axes.view_init(45, 55)
# axes.contour3D(x_1,y_1,z,90,cmap='Blues')
# axes.plot_wireframe(x_1,y_1,z,cmap='Reds')
axes.plot_surface(x_1, y_1, z, cmap='Greys', edgecolor='k', rstride=1, cstride=1)
axes.set_xlabel('X', color='blue')
axes.set_ylabel('Y', color='blue')
axes.set_zlabel('Z', color='blue')
axes.set_facecolor('green')
axes.set_title('SURFACE-PLOT', color='#001e2b')
