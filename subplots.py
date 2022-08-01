import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(figsize=(4, 3), nrows=2, ncols=1, dpi=200)
plt.tight_layout()
x = np.random.randint(0, 15, 10)
y = np.sqrt(x ** 2)

axes[1].plot(x, y, color='green', label='x/x squared')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_title('plot-2')

axes[0].plot(y / 2, x / 10, color='red')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('plot-1')
