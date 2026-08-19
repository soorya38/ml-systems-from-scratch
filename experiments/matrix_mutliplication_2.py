# Matrix times Matrix

# multiply two matrices together (return -1 if shapes of matrix don't align), i.e. 
# C=A⋅B

# Example:
# Input:
# A = [[1,2],[2,4]], B = [[2,1],[3,4]]
# Output:
# [[8, 9], [16, 18]]

# Reasoning:
# Reasoning: Each entry of C is the dot product of a row of A with a column of B. C[0][0] = 1·2 + 2·3 = 8 C[0][1] = 1·1 + 2·4 = 9 C[1][0] = 2·2 + 4·3 = 16 C[1][1] = 2·1 + 4·4 = 18

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(a[0]) != len(b):
        return -1
    
    ans = []
    for row_a in a:
        row = []

        for col_b in zip(*b):
            row.append(sum(x * y for x, y in zip(col_b, row_a)))
        
        ans.append(row)

    return ans