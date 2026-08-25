# Expected Value and Variance of an n-Sided Die

# Write a Python function that computes the expected value and variance of a fair n-sided die roll. The die has faces numbered 1 through n, each equally likely. The function should return a tuple (expected_value, variance).

# Example:
# Input:
# dice_statistics(6)
# Output:
# (3.5, 2.9167)

# Reasoning:
# For n=6, the expected value is (6+1)/2 = 3.5 and the variance is (6^2-1)/12 = 35/12 ≈ 2.9167.

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	exp = sum(x for x in range(1, n+1)) / n
	var = ((n ** 2)-1) / 12
	return (exp, var)