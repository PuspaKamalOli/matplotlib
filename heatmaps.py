import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

diseases = ["Coronavirus", "Influenza", "Pneumonia", "Dyspnea"]
dates = ["Jun28", "Jul05", "Jul12", "Jul19", "Jul26", "Aug02", "Aug09", "Aug16", "Aug21"]
symp_per = np.array([[5.2, 5.5, 5.7, 5.6, 5.3, 5.1, 5.0, 4.9, 5.3],
                     [3.5, 4.0, 4.3, 3.9, 3.5, 3.2, 2.7, 2.2, 2.0],
                     [1.8, 2.2, 2.3, 2.2, 2.1, 1.9, 1.7, 1.4, 1.3],
                     [1.0, 1.1, 1.1, 1.0, 0.9, 0.8, 0.8, 0.8, 0.7]])

fig_10, axes_10 = plt.subplots()

im = axes_10.imshow(symp_per, cmap="Blues")
axes_10.set_xticks(np.arange(len(dates)))
axes_10.set_yticks(np.arange(len(diseases)))
axes_10.set_xticklabels(dates)
axes_10.set_yticklabels(diseases)

plt.setp(axes_10.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(diseases)):
    for j in range(len(dates)):
        text = axes_10.text(j, i, symp_per[i, j],
                            ha="center", va="center", color="k", fontweight="bold")
