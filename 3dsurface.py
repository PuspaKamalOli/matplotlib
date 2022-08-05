import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = 15 * np.random.random(50)
y = np.sin(x) * np.random.randn(50)
z = np.cos(x) * np.random.randn(50)
fig = plt.figure(figsize=(5, 6), dpi=300)
axes = fig.add_axes([0, 0, 0.7, 0.6], projection='3d')
axes.scatter(x, y, z, c=z)
plt.show()
