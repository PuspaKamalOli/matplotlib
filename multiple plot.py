import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0, 5, 10)
y_1 = x_1 ** 2
plt.subplot(1,2,1)
plt.plot(x_1, y_1, 'cyan')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("simple plot_1")
plt.subplot(1,2,2)
plt.plot(y_1, x_1, 'orange')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("simple plot_2")

plt.show()
