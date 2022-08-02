import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(10, 50, 23)
y = x ** 3
fig = plt.figure(figsize=(6, 5), dpi=300)
axes = fig.add_axes([0, 0, 0.6, 0.6])
axes.plot(x, y, color='#081c0e', ls='-.',
          marker='*', markersize=8, markeredgewidth=0.7,
          markeredgecolor='blue', markerfacecolor='red')
axes.grid(True, color='#9c9b9a')
axes.set_facecolor('#21edd9')
plt.show()
# to save
fig.savefig('plot.png')
