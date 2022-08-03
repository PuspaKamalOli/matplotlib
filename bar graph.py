import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(10, 50, 8)
y = np.array([30, 50, 45, 80, 90, 76, 23, 10])
fig = plt.figure(figsize=(6, 4), dpi=300)
axes = fig.add_axes([0, 0, 0.8, 0.6])
axes.bar(x, y, width=4, color='cyan', edgecolor='black')
axes.grid(True, color='#8e918f', dashes=(6, 1, 3, 1))
axes.set_xlabel("x-axis", color='#156e32')
axes.set_ylabel("y-axis", color='#156e32')
axes.set_xticks(x, ('x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8'), color='red')
axes.set_yticks(y, ('y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8'), color='red')
