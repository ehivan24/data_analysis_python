import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Data_Analysis_Util(object):

    def __init__(self):
        pass

    @staticmethod
    def read_file(file_to_read):
        with open(file_to_read, 'rb') as f:
            read = csv.DictReader(f)
            return list(read)

    @staticmethod
    def parse_date(date):
        if date == '':
            return None
        else:
            return dt.strptime(date, '%Y-%m-%d')

    @staticmethod
    def parse_int(number):
        if number == '':
            return None
        else:
            return int(number)

    @staticmethod
    def parse_int_from_float(number):
        if number == '':
            return None
        else:
            return int(float(number))

    @staticmethod
    def round_data(number):
        if number == '':
            return None
        else:
            return round(float(number))

    """
        Plot Data
    """

    @staticmethod
    def run_plot(data):
        plt.hist(data, bins=8)
        plt.xlabel("XLabel")
        plt.ylabel("YLabel")
        plt.show()

    @staticmethod
    def describe_data(data):
        print("Mean: ", np.mean(data))
        print("Min: ", np.max(data))
        print("Max: ", np.min(data))
        print("Standard Deviation: ", np.std(data))
        print("Median: ", np.median(data))
        print("Sum: ", np.sum(data))

    """
    Numpy
    """
    @staticmethod
    def max_employment(countries, employment):
        i = employment.argmax()
        return (countries[i], employment[i])

    @staticmethod
    def min_employment(countries, employment):
        i = employment.argmin()
        return (countries[i], employment[i])

    @staticmethod
    def over_all_data(array1, array2):
        return (array1 + array2) /2

    @staticmethod
    def standardized_data(values):
        standarized_value = (values - values.mean()) / values.mean()
        return standarized_value

    @staticmethod
    def mean_time_for_paid_students(time_spent, days_to_cancel):
        return time_spent[days_to_cancel >= 7].mean()

    @staticmethod
    def variable_correlation(series1, series2):
        both_above = (series1 > series1.mean()) & (series2 > series2.mean())
        both_below = (series1 < series1.mean()) & (series2 < series2.mean())

        is_same_direction = both_above | both_below
        num_same_direction = is_same_direction.sum()
        num_different_direction = len(series1) - num_same_direction

        return (num_same_direction, num_different_direction)


    """
    Pandas
    """
    @staticmethod
    def max_gdp(data):
        max_country = data.argmax()
        max_value = data.loc[max_country]

        return (max_country, max_value)

    @staticmethod
    def min_gdp(data):
        min_country = data.argmin()
        min_value = data.loc[min_country]

        return (min_country, min_value)
