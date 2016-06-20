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
