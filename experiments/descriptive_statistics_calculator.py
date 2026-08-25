# Descriptive Statistics Calculator

# Write a Python function to calculate various descriptive statistics metrics for a given dataset. The function should take a list or NumPy array of numerical values and return a dictionary containing:

# mean: Average of all values
# median: Middle value when sorted
# mode: Most frequently occurring value
# variance: Population variance (divide by N)
# standard_deviation: Square root of variance
# 25th_percentile, 50th_percentile, 75th_percentile: Quartile values
# interquartile_range: Difference between 75th and 25th percentiles (IQR)

# Example:
# Input:
# [1, 2, 2, 3, 4, 4, 4, 5]
# Output:
# {'mean': 3.125, 'median': 3.5, 'mode': 4, 'variance': 1.6094, 'standard_deviation': 1.2686, ...}

# Reasoning:
# Mean = (1+2+2+3+4+4+4+5)/8 = 3.125. Median = average of 4th and 5th values = (3+4)/2 = 3.5. Mode = 4 (appears 3 times, most frequent). Variance and standard deviation measure spread around the mean. Percentiles divide the sorted data into quarters.

import numpy as np
from collections import Counter
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    mean = sum(x for x in data) / len(data)
    data.sort()
    median = data[len(data)//2]
    if len(data) % 2 == 0:
        median = (data[len(data)//2] + data[len(data)//2-1]) / 2
    counter = Counter(data)
    mode = counter.most_common(1)[0][0]
    
    variance = sum((x-mean) ** 2 for x in data) / len(data)
    sd = math.sqrt(variance)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        "standard_deviation": sd,
        '25th_percentile': np.percentile(data, 25),
        '50th_percentile': np.percentile(data, 50),
        '75th_percentile': np.percentile(data, 75),
        'interquartile_range': np.percentile(data, 75) - np.percentile(data, 25)
    }