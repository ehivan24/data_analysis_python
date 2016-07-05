import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as utils


"""
    Here we load the file.
"""

df_weather = pd.read_csv('nyc_subway_weather.csv')

max_station = df_weather['ENTRIESn'].argmax()
row_number = df_weather.iloc[max_station]
"""
    Print out the row with the highest number of entries.
"""
print row_number
"""
    prints out the approximate location of the station.
"""
print utils.get_place_name(40.7526, -73.9792)

print df_weather['ENTRIESn'].describe()

"""
    Pearson's R
    Correlation between two arrays

    expected output: (-1, 1, 0)
    -1: Negative Correlation
     1: Positive Correlation
     0: No Correlation

"""

print "Correlation: ", utils.correlation(df_weather['ENTRIESn_hourly'], df_weather['meanprecipi'])
print "Correlation: ", utils.correlation(df_weather['ENTRIESn_hourly'], df_weather['ENTRIESn'])



"""
    Example with Pandas applymap()
"""

df_grades = pd.DataFrame(
    data={'exams_1': [98, 90, 87, 90, 89, 45],
          'exams_2': [78, 90, 67, 80, 89, 23]},
    index=['Joe', 'Marie', 'Foo', 'Abs', 'Me', 'Smith'])


def convert_grades(grades):
    if grades >= 90:
        return 'A'
    elif grades >= 80:
        return 'B'
    elif grades >= 70:
        return 'C'
    elif grades >= 60:
        return 'D'
    else:
        return 'F'

#print convert_grade(0)


def convert_grade(grades):
    return grades.applymap(convert_grades)

print convert_grade(df_grades)

"""
    Standardizing a func
"""


def std_col(col):
    return (col - col.mean()) / col.std()

print std_col(df_grades['exams_1'])
print std_col(df_grades['exams_2'])

print "Largest Number of Entries: \n", utils.sorting_data_frame_first_largest(df_weather['ENTRIESn'])
print "Second Largest Number of Entries: \n", utils.sorting_data_frame_second_largest(df_weather['ENTRIESn'])


df = pd.DataFrame({
    'a': [3, 4, 7, 9, 2],
    'b': [1, 2, 4, 5, 89],
    'c': [6, 34, 65, 2, 00]
})


"""
    Apply pandas
"""

print utils.second_largest_data_frame(df)

"""
    Group by function in Pandas
"""
# mean of the col b.
print "Mean: ", df.groupby('a').sum()['b'].mean()

print "Group: ", df.groupby('a').groups

print "", df.describe()

plt.plot(df)
plt.legend()
#plt.show()