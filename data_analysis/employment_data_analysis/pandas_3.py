import pandas as pd
import datetime
from pandas_datareader import data, wb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sn
import quandl as qdl
import pickle

#style.use('ggplot')
style.use('fivethirtyeight')


"""
Plotting two graphs


plt.figure(1)
plt.subplot(211)
plt.plot(np.array([23, 34, 53, 4]), '-')
plt.subplot(212)
plt.plot(np.array([0, 23, 34, 12]), 'o')
plt.show()
"""


"""
    Finding erroneous data with Pandas
    (1) get the standard deviation of the data
        and then plot it.

"""
bridge_height = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 6212.90, 10.28, 10.25, 10.31]}

df = pd.DataFrame(bridge_height)
df['STD'] = pd.Series(df['meters'])
print df
df_std = df.describe()['meters']['std']
print df_std

df = df[ (df['STD'] < df_std) ]
print df

max_number_registered = df['meters'].max()

plot_final_data = []
for mts in df['meters']:
    if not mts > max_number_registered:
        plot_final_data.append(mts)

print plot_final_data
plt.plot(plot_final_data)
plt.show()

