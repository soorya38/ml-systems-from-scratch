# Empirical Probability Mass Function (PMF)

# Problem
# Given a list of integer samples drawn from a discrete distribution, implement a function to compute the empirical Probability Mass Function (PMF). The function should return a list of (value, probability) pairs sorted by the value in ascending order. If the input is empty, return an empty list.

# Example:
# Input:
# samples = [1, 2, 2, 3, 3, 3]
# Output:
# [(1, 0.16666666666666666), (2, 0.3333333333333333), (3, 0.5)]

# Reasoning:
# Counts are {1:1, 2:2, 3:3} over 6 samples, so probabilities are 1/6, 2/6, and 3/6 respectively, returned sorted by value.

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    v = {}
    for x in samples:
        v[x] = v.get(x, 0) + 1
    
    ans = []
    for x in v:
        ans.append((x, v.get(x, 0) / len(samples)))
    return ans