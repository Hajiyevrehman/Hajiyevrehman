import pandas as pd
import numpy as np

class DataAnalyticsTool:
    def __init__(self, data):
        if not data:
            raise ValueError("The data list cannot be empty.")
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        mean = total / len(self.data)
        return mean

    def calculate_median(self):
        median = np.median(self.data)
        return median

    def calculate_mode(self):
        mode = pd.Series(self.data).mode()[0]
        return mode

    def calculate_standard_deviation(self):
        std = np.std(self.data)
        return std

    def calculate_variance(self):
        var = np.var(self.data)
        return var

    def calculate_skewness(self):
        skew = pd.Series(self.data).skew()
        return skew

    def calculate_kurtosis(self):
        kurtosis = pd.Series(self.data).kurtosis()
        return kurtosis

    def calculate_range(self):
        data_range = max(self.data) - min(self.data)
        return data_range

    def calculate_interquartile_range(self):
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        return iqr

    def calculate_z_scores(self):
        z_scores = (self.data - np.mean(self.data)) / np.std(self.data)
        return z_scores
