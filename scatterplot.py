import numpy as np
import matplotlib.pyplot as plt

cnt_arr = np.array(['australia', 'brazil', 'candada', 'chile',
                    'france', 'germany', 'greece', 'india'])
dr_arr = np.array([1.8, 53, 24.5, 56.5,
                   45, 11, 2.2, 24])
test_arr = np.array([110, 7197, 600, 1862,
                     1636, 1103, 35, 10243])
cc_arr = np.array([24236, 3456652, 125408, 390037,
                   256534, 229706, 7684, 50488])
cc_arr_sm = cc_arr / 1000
color_arr = ['red', 'orange', 'yellow', 'blue', 'cyan', 'green', '#e809c3', '#a3a0a3']
fig = plt.figure(figsize=(6, 5), dpi=300)
axes = fig.add_axes([0, 0, 0.6, 0.5])
axes.scatter(dr_arr, test_arr, s=cc_arr_sm, c=color_arr, alpha=1)
