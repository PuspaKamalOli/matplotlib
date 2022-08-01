import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

fig=plt.figure(figsize=(4,3),dpi=300)
axes=fig.add_axes([0.1,0.1,0.60,0.40])
x=np.random.randint(0,10,10)
y=np.sqrt(x**5)
axes.plot(x,y,color='r')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title("using figure object to plot in line graph")
axes.text(1,200,'x-y plot',color='blue')
plt.show()

