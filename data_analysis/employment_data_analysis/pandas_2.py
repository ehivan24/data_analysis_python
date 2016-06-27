import pandas as pd
import datetime
import pandas.io.data as web
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sn
import quandl as qdl


#df = pd.read_csv('gdp_per_capita.csv')
#df.set_index('Country', inplace=True)

#print df.keys()

#print df['Country'].fillna(0)
#print df[['Country', '1998', '2011']].fillna(0)

df2 = qdl.get('FMAC/HPI_AK')

plt.plot(df2['Value'])

my_data = qdl.get('FRED/GDP')
#print my_data

nse_oil = qdl.get(["NSE/OIL.1", "WIKI/APPL"])

print nse_oil
#plt.show()