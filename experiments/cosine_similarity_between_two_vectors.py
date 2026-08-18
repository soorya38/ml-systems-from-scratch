# Calculate Cosine Similarity Between Vectors

# Task: Implement Cosine Similarity
# In this task, you need to implement a function cosine_similarity(v1, v2) that 
# calculates the cosine similarity between two vectors. Cosine similarity measures 
# the cosine of the angle between two vectors, indicating their directional similarity.

# Input:

# v1 and v2: Numpy arrays representing the input vectors.
# Output:

# A float representing the cosine similarity.
# Constraints:

# Both input vectors must have the same shape.
# Input vectors cannot be empty or have zero magnitude.

# Example:
# Input:
# import numpy as np

# v1 = np.array([1, 2, 3])
# v2 = np.array([2, 4, 6])
# print(round(cosine_similarity(v1, v2), 3))

# Output:
# 1.0

# Reasoning:
# The cosine similarity between v1 and v2 is 1.0, indicating perfect similarity (vectors point in the same direction).

from math import sqrt

def dot_product(v1: list[int | float], v2: list[int | float]) -> float:
    return sum(x * y for x, y in zip(v1, v2))

def l2_norm(v1: list[int | float]) -> float:
    return sqrt(sum(x * x for x in v1))

def cosine_similarity(v1: list[int | float], v2: list[int | float]) -> float:
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1: 1D array representing the first vector.
        vec2: 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    denominator = l2_norm(v1) * l2_norm(v2)
    if denominator == 0:
        return 0.0

    return dot_product(v1, v2) / denominator