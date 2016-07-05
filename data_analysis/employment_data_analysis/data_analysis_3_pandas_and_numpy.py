import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as utils

ny_weather_subway = pd.read_csv('nyc_subway_weather.csv')
print ny_weather_subway[:5]

ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

max_per_row = ridership[0, :].max()
print max_per_row

max_per_col = ridership[:, :].max()
print max_per_col

min_per_col = ridership[:, :].min()
print min_per_col

print ny_weather_subway.keys()
print ny_weather_subway.head()
print ny_weather_subway.tail()
print "Ending ", len(ny_weather_subway[[station_name.endsWith('CYPRESS HILLS') for station_name in ny_weather_subway.station]])



