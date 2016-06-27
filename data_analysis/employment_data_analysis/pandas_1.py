import pandas as pd
import datetime
import pandas.io.data as web
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sn

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader('XOM', 'google', start, end)

print df.head(3)
print df.tail(3)
#df['Adj Close'].plot()
#df['Open'].plot()
#df['High'].plot()

print df[['Low', 'Close']].head(5)
print (np.array(df[['High', 'Low']]))
"""
Convert to DataFrame
"""

df2 = pd.DataFrame(np.array(df[['High', 'Open']]))


plt.plot(df['High'], df['Low'], 'b')
print df2.head(4)
plt.show()