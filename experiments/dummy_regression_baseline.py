# Implement a simple baseline regressor that ignores feature values and always predicts a summary statistic of the training targets. This is a useful sanity check: any real model should outperform it.

# Write dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None) that:

# Computes a single prediction value p from y_train according to strategy:
# 'mean': arithmetic mean of y_train.
# 'median': median of y_train (use numpy.median, which averages the two middle values for even-length inputs).
# 'quantile': the quantile-th quantile of y_train using linear interpolation (i.e. numpy.quantile(y_train, quantile)). Raise ValueError if quantile is None or not in [0, 1].
# 'constant': use the provided constant value. Raise ValueError if constant is None.
# For any other strategy string, raise ValueError.
# Returns a Python list of length n_test where every entry equals p (cast to float).
# Do not round the prediction inside the function.

# Example:
# Input:
# y_train = [1, 2, 3, 4, 5], n_test = 3, strategy = 'mean'
# Output:
# [3.0, 3.0, 3.0]
# Reasoning:
# The mean of [1,2,3,4,5] is 3.0. The dummy regressor ignores any test features and outputs this same value n_test=3 times, giving [3.0, 3.0, 3.0].

import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    match strategy:
        case "constant":
            if constant is None:
                raise ValueError('invalid constant')
            
            return [constant] * n_test
        
        case 'mean':
            m = np.array(y_train)
            me = m.mean(axis=0)
            return [me] * n_test

        case 'median':
            m = np.array(y_train)
            me = np.median(y_train)
            return [me] * n_test
        
        case 'quantile':
            if quantile is None or not (0 <= quantile <= 1):
                raise ValueError('invalid quantile')
            
            return [np.quantile(y_train, quantile)] * n_test
