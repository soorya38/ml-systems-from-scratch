# Random Train/Validation/Test Split with Shuffling

# Implement a function random_split that randomly partitions a dataset into training, validation, and test subsets based on given fractions. The function should:

# Take a 2D NumPy array data of shape (n, d), a float train_frac, a float validation_frac, and an integer seed for reproducibility.
# Shuffle the rows of the dataset using np.random.default_rng(seed).permutation(n) to generate a random ordering of row indices.
# Compute split indices using floor division via int():
# train_end = int(n * train_frac)
# validation_end = train_end + int(n * validation_frac)
# Return a list of three NumPy arrays [train, validation, test] corresponding to the shuffled rows in those three index ranges. The remaining rows after the validation split form the test set.
# The sum of train_frac and validation_frac is guaranteed to be less than or equal to 1.0.

# Example:
# Input:
# data = np.arange(20).reshape(10, 2), train_frac=0.7, validation_frac=0.1, seed=123
# Output:
# train has 7 rows, validation has 1 row, test has 2 rows
# Reasoning:
# With n=10, train_end = int(100.7) = 7 and validation_end = 7 + int(100.1) = 8. After shuffling row indices with the given seed, the first 7 shuffled rows go to train, the next 1 to validation, and the remaining 2 to test.

import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = len(data)

    rows = np.random.default_rng(seed).permutation(n)
    t = int(n * train_frac)
    v = t + int(n * validation_frac)

    return [
        data[rows[:t]],
        data[rows[t:v]],
        data[rows[v:]]
    ]