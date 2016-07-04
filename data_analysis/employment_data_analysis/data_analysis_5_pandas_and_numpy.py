import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as utils

df_subway = pd.read_csv('nyc_subway_weather.csv')
ridership_per_day = df_subway.groupby('day_week').mean()['ENTRIESn_hourly']


"""
    In this graph we can observe that the days Saturday and Sunday the rides per day drop
"""
#plt.plot(ridership_per_day)
#plt.show()


def hourly_rate(entries_and_exits):
    return entries_and_exits -  entries_and_exits.shift(1)

ridership_hourly = df_subway.groupby('UNIT')[['ENTRIESn', 'EXITSn']].apply(hourly_rate)

"""
    Groups the DataFrame by latitude and longitude
"""
data_by_location = df_subway.groupby(['latitude', 'longitude'], as_index=False).mean()


"""
    Properly scales the scatter plot
"""
MAX_SCALE = 2
scaled_entries = (data_by_location['ENTRIESn_hourly'] /
                  data_by_location['ENTRIESn_hourly'].std() * MAX_SCALE)

"""
    Scales by latitude and longitude
"""
plt.scatter(data_by_location['latitude'], data_by_location['longitude'],
            s=scaled_entries)

"""
    This method gets the place with the max number of rides.
"""
max_riders_per_hour = df_subway['ENTRIESn_hourly'].argmax()
max_number = df_subway.iloc[max_riders_per_hour]
print max_number['latitude']
print max_number['longitude']
print utils.get_place_name(max_number['latitude'], max_number['longitude'])

"""
    how the plot
"""
plt.show()