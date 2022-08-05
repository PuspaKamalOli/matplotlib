import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

goog_df = pd.read_csv('GOOG.csv', index_col=0, parse_dates=True)
goog_df.index.name = 'Date'
mpf.plot(goog_df, type='candle')
mpf.plot(goog_df, type='line')
mpf.plot(goog_df, type='ohlc', mav=(4, 5, 6), volume=True)
