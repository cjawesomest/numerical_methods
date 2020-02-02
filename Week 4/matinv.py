## Cameron Calv ECE T480
# Performs the inverse of a square matrix A. The input is a square matrix A, and the
# output is a square matrix.
from inv_lu import inv_lu

def matinv(sqr_matrix):
    inverse = inv_lu(sqr_matrix)
    return inverse

if __name__ == '__main__':
    matrix = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    print(matinv(matrix))