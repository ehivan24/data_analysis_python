import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as utils

#life_expectancy.csv
#employment_above_15.csv
#female_completion_rate.csv
#gdp_per_capita.csv
#male_completion_rate_rate.csv


countries = pd.read_csv('gdp_per_capita.csv')

print("", len(countries['Country'].unique()))


countries_array = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])

print "Maximum: ", utils.max_employment(countries_array, employment)
print "Minimum: ", utils.min_employment(countries_array, employment)

life_expectancy_values = [74.7, 75., 83.4, 57.6, 74.6, 75.4, 72.3, 81.5, 80.2,
                          70.3, 72.1, 76.4, 68.1, 75.2, 69.8, 79.4, 70.8, 62.7,
                          67.3, 70.6]

gdp_values = [1681.61390973, 2155.48523109, 21495.80508273, 562.98768478,
              13495.1274663, 9388.68852258, 1424.19056199, 24765.54890176,
              27036.48733192, 1945.63754911, 21721.61840978, 13373.21993972,
              483.97086804, 9783.98417323, 2253.46411147, 25034.66692293,
              3680.91642923, 366.04496652, 1175.92638695, 1132.21387981]

life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

print "Life Expectancy \n", life_expectancy.describe()
print "GDP \n", gdp.describe()
print utils.variable_correlation(life_expectancy, gdp)

