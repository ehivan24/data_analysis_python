import pandas as pd
import datetime
from pandas_datareader import data, wb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sn
import quandl as qdl
import pickle
style.use('ggplot')


df = pd.read_csv('gdp_per_capita.csv')
#df.set_index('Country', inplace=True)

#print df.keys()

#print df['Country'].fillna(0)
plot_data = df['1960'].dropna()
plot_data_1 = df['2011'].dropna()

#plt.show()

#df2 = qdl.get('FMAC/HPI_AK')

#plt.plot(df2['Value'])

#my_data = qdl.get('FRED/GDP')
#print my_data

#nse_oil = qdl.get(["NSE/OIL.1", "WIKI/SCTY"])

#print nse_oil
elements_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_chemical_elements")
df = pd.DataFrame(elements_list[0][2], elements_list[0][3])
df2 = pd.DataFrame(elements_list[0][4], elements_list[0][1])
frames = [df.fillna(0), df2.fillna(0)]


pickle_out = open('elements.pickle', 'wb')
pickle.dump(frames, pickle_out)
pickle_out.close()


"""
Serializable data
"""

pickle_in = open('elements.pickle', 'rb')
data_pickle = pickle.load(pickle_in)
print data_pickle


print plot_data.describe()

plt.xlabel('Years')
plt.ylabel('Percent')
plt.plot(plot_data, color='b', label='1960')
plt.plot(plot_data_1, color='r', label='2011')
plt.legend()
plt.show()




