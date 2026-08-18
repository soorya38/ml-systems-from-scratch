# Vector Norms (L1/L2/Frobenius)

# Implement a function that computes different types of norms for vectors and matrices.

# Vector norms are fundamental concepts in linear algebra that measure the "size" or "length" of vectors. 
# Different norms have different properties and applications in machine learning, particularly in regularization and distance calculations.

# Your Task: Write a function compute_norm(arr, norm_type) that takes:

# arr: A numpy array (can be 1D or 2D)
# norm_type: A string specifying which norm to compute ('l1', 'l2', or 'frobenius')
# The function should return the computed norm as a float.

# Constraints:

# For 'l1' and 'l2' norms, the input can be any array (1D or 2D)
# For 'frobenius' norm, the input is typically a 2D matrix
# All norms should treat the input as a flattened collection of elements when computing

# Example:
# Input:
# arr = [3, -4], norm_type = 'l2'
# Output:
# 5.0

# Reasoning:
# For the L2 norm, we compute the square root of the sum of squared elements: sqrt(3^2 + (-4)^2) = sqrt(9 + 16) = sqrt(25) = 5.0

import math


def compute_norm(array: list[int | float | list[int | float]], norm_type: str) -> float:
    """
    Calculate a norm for a 1D or 2D array.

    norm_type:
        "l1"         -> Sum of absolute values
        "l2"         -> Square root of sum of squares
        "frobenius"  -> Same calculation as L2, mainly for matrices
    """

    # Flatten the array so the same logic works for 1D and 2D input.
    # [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    values = []

    for row in array:
        if isinstance(row, list):
            values.extend(row)
        else:
            values.append(row)

    if norm_type == "l1":
        return float(sum(abs(x) for x in values))

    elif norm_type == "l2" or norm_type == "frobenius":
        return float(math.sqrt(sum(x * x for x in values)))
    
    return -1