# StandardScaler Fit and Transform
# Medium
# Machine Learning

# Implement a function standard_scaler(X_train, X_test) that standardizes features by removing the mean and scaling to unit variance.

# Given:

# X_train: numpy array of shape (n_train, n_features) used to fit the scaler (compute per-feature mean and standard deviation).
# X_test: numpy array of shape (n_test, n_features) to transform using the statistics learned from X_train.
# For each feature column 
# j
# j, compute the mean 
# μ
# j
# μ 
# j
# ​
#   and the population standard deviation 
# σ
# j
# σ 
# j
# ​
#   (i.e., dividing by 
# N
# N, not 
# N
# −
# 1
# N−1) from X_train. Then transform X_test as:

# z
# i
# j
# =
# x
# i
# j
# −
# μ
# j
# σ
# j
# z 
# ij
# ​
#  = 
# σ 
# j
# ​
 
# x 
# ij
# ​
#  −μ 
# j
# ​
 
# ​
 

# Edge case: If a feature has zero standard deviation in X_train (constant column), treat its standard deviation as 1.0 to avoid division by zero (the resulting transformed values become x_{ij} - \mu_j).

# Return the transformed X_test as a numpy array. Do NOT round inside the function.

# Example:
# Input:
# X_train = [[1, 2], [3, 4], [5, 6]]
# X_test = [[2, 3], [4, 5]]
# Output:
# [[-0.6124, -0.6124], [0.6124, 0.6124]]
# Reasoning:
# Per-feature means from X_train are [3, 4] and population standard deviations are [sqrt(8/3), sqrt(8/3)] ≈ [1.6330, 1.6330]. Subtracting the means and dividing by the standard deviations yields the standardized X_test.

import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)

    std[std == 0.0] = 1.0

    return (X_test - mean)/std