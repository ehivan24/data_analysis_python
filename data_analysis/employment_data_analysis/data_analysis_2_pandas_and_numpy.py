import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as util

#life_expectancy.csv
#employment_above_15.csv
#female_completion_rate.csv
#gdp_per_capita.csv
#male_completion_rate_rate.csv


countries = pd.read_csv('male_completion_rate.csv')
#enrollments = enrollments.values
print countries[0]

for country in countries:
    if country == 'Abkhazia':
        print "Found"
        break

