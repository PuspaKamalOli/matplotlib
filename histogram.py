import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

arr = np.array(
    [10, 13, 60, 3, 65, 12, 14, 14, 17, 34, 25, 22, 36, 44, 35, 78, 54, 86, 90, 71, 90, 99, 12, 45, 56, 77, 84, 84,
     100])
fig = plt.figure(figsize=(6, 4), dpi=300)
axes = fig.add_axes([0, 0, 0.8, 0.6])
axes.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], color='green',
          edgecolor='blue', stacked=True, density=True)
plt.show()
