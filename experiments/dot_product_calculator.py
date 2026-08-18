# Dot Product Calculator

# Write a Python function to calculate the dot product of two vectors. 
# The function should take two arrays as input and return the dot product as a single number.

# Example:
# Input:
# vec1 = np.array([1, 2, 3]), vec2 = np.array([4, 5, 6])
# Output:
# 32

# Reasoning:
# The function calculates the dot product by multiplying corresponding elements of the two vectors and summing the results. For vec1 = [1, 2, 3] and vec2 = [4, 5, 6], the result is (1 * 4) + (2 * 5) + (3 * 6) = 32.

def dot_product(a: list[int|float], b: list[int|float]) -> int:
	# Calculate the dot product of two vectors.
	# If vectors have different lengths, return -1.
	if len(a) != len(b):
		return -1
	
	return sum(x * y for x, y in zip(a, b))