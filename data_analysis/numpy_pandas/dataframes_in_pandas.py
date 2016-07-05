import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Analysis_Utils import Data_Analysis_Util as utils


def create_data_frame():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    df_medals = ({'country_name': pd.Series(countries),
                  'gold': pd.Series(gold),
                  'silver': pd.Series(silver),
                  'bronze': pd.Series(bronze)})
    olympic_medals = pd.DataFrame(df_medals)
    return olympic_medals


df_olympics = create_data_frame()

print df_olympics[['country_name', 'gold']].max()
#print df_olympics['gold'].map(lambda x: x >= 5)
print df_olympics['gold'].filter(lambda x: x >= 5)


