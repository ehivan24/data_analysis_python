import pandas as pd
import datetime
from pandas_datareader import data, wb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sn
import pickle
from sklearn import svm, preprocessing, cross_validation

style.use('ggplot')


def check_price(current_price, future_price):
    if future_price > current_price:
        return 1
    else:
        return 0


def moving_average(values):
    return np.mean(values)

df_googl = pd.read_csv('NASDAQ_GOOGL.csv')
"""
here it shifts the price to minus one.
"""
df_googl['Future'] = df_googl['Close'].shift(-1)
df_googl.dropna(inplace=True)
#print df_googl[['Future', 'Close']].head()

df_googl['Predicted'] = list(map(check_price, df_googl['Close'], df_googl['Future']))

#print df_googl['Price'].head()

#df_googl['Mean'] = moving_average(df_googl['Close'])

#print df_googl[['Open', 'High', 'Low', 'Close', 'Future', 'Predicted', 'Mean']].head()

X = np.array(df_googl['Close'])
X = preprocessing.scale(X)

print X
y = np.array(df_googl['Predicted'])
print y

x_train, x_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

classifier = svm.SVC(kernel='linear')
classifier.fit(x_train, y_train)
print classifier.score(x_test, y_test)



#plt.plot(df_googl['Future'], '-', color='b')
#plt.show()
#print df_googl.head()






