import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# where GOOG.csv is a file you can get from https://finance.yahoo.com/quote/GOOG/history?period1=1566345600&period2=1597968000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
dt_frame = pd.read_csv('GOOG.csv')
np_arr = dt_frame.values
open = np_arr[:, 1]
volume = np_arr[:, 2] * 2
plt.plot(open, volume)
plt.xlabel('open')
plt.ylabel('volume')
plt.show()
