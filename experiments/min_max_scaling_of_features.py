# Min-Max Scaling of Feature Values
# Easy
# Data Preprocessing

# Breakdown

# Implement a function that performs Min-Max Normalization on a list of integers, scaling all values according to the formula. Min-Max normalization helps ensure that all features contribute equally to a model by scaling them to a common range.

# Example:
# Input:
# min_max([1, 2, 3, 4, 5])
# Output:
# [0.0, 0.25, 0.5, 0.75, 1.0]
# Reasoning:
# The minimum value (1) becomes 0.0, the maximum value (5) becomes 1.0, and the values in between are scaled proportionally. For instance, 3 is exactly halfway between 1 and 5, so it becomes 0.5.

import numpy as np

def min_max(x: list[float]) -> list[float]:
    mini = np.min(x)
    maxi = np.max(x)

    min_max_sca = (x - mini) / (maxi - mini)

    return min_max_sca