## least squares algorithm
from sympy import Matrix
import numpy as np
"""
Least squares alg applied programmatically:
    1. take in vector points
    2. create the design matrix X
    3. Transpose design matrix, call it X^T
    4. compute X^T X and X^T y
    5. Set up equation, find inverse of X^T X 
"""


m = Matrix([[4, 6], [6, 14]])

inverse = m.inv()

# A = np.array([[7/10, -3/10], 
#               [-3/10,  1/5]])
# B = np.array([[6, 11]])

# result = A @ B


print(inverse)

def get_matrix_inverse(m):
    """
    gets the inverse by setting up [A | I], doing row operations such that A turns into the identity matrix
    and I turns into the inverse. 
    """
    n = len(m)
    # Create the augmented matrix [m | I]
    inverse = [[float(i == j) for j in range(n)] for i in range(n)]
    
    # Copy m to avoid modifying the original matrix
    matrix_copy = [row[:] for row in m]

    for i in range(n):
        # Pivot search: find the row with the largest value in the current column
        pivot_row = i
        for k in range(i + 1, n):
            if abs(matrix_copy[k][i]) > abs(matrix_copy[pivot_row][i]):
                pivot_row = k
        
        # Swap rows in both the original and augmented matrices
        matrix_copy[i], matrix_copy[pivot_row] = matrix_copy[pivot_row], matrix_copy[i]
        inverse[i], inverse[pivot_row] = inverse[pivot_row], inverse[i]

        # Division by pivot to make leading element 1
        pivot = matrix_copy[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError("Matrix is singular and cannot be inverted.")
            
        for j in range(n):
            matrix_copy[i][j] /= pivot
            inverse[i][j] /= pivot

        # Elimination of other rows
        for k in range(n):
            if k != i:
                factor = matrix_copy[k][i]
                for j in range(n):
                    matrix_copy[k][j] -= factor * matrix_copy[i][j]
                    inverse[k][j] -= factor * inverse[i][j]
    return inverse
