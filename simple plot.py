import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 5, 10)
y_1 = x_1 ** 2
plt.plot(x_1, y_1, 'cyan')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("simple plot")
plt.show()
