## Cameron Calv ECE T480
# Computes the LU decomposition of a square matrix A. The input is a square
# matrix A. The output are the lower diagonal matrix L and the upper diagonal matrix A.

## Cameron Calv ECE T480
# Performs Gauss elimination(with partial pivoting). Inputs are the array of system
# coefficients (the A matrix) and the resultant column vector (the b vector). The output is a
# column vector X that is the solution of the system of equations Ax = b.
def pivot(some_matrix, s_vector, k_value, iter):
    n = iter
    A_matrix = []
    for i in range(len(some_matrix)):
        A_matrix.append([])
        for j in range(len(some_matrix)):
            A_matrix[i].append(some_matrix[i][j])
    pivot = k_value
    big = abs(A_matrix[k_value][k_value]/s_vector[k_value])
    for i in range(k_value, n):
        dummy = abs(A_matrix[i][k_value]/s_vector[i])
        if dummy > big:
            big = dummy
            pivot = i
    if not pivot == k_value:
        for j in range(k_value, n):
            dummy = some_matrix[pivot][j]
            A_matrix[pivot][j] = some_matrix[k_value][j]
            A_matrix[k_value][j] = dummy
        dummy = s_vector[pivot]
        s_vector[pivot] = s_vector[k_value]
        s_vector[k_value] = dummy
    return A_matrix,  s_vector


def find_factors(A_matrix, s_vector, tolerance):
    n = len(A_matrix)
    factors = []
    for i in range(n-1):
        factors.append([])
    error = 0
    for k in range(n-1):
        [temp_A, temp_S] = pivot(A_matrix, s_vector, k, n)
        A_matrix = temp_A
        s_vector = temp_S
        if abs(A_matrix[k][k]/s_vector[k]) < tolerance:
            error = -1
            break
        for i in range(k+1, n):
            factor = A_matrix[i][k]/A_matrix[k][k]
            factors[k].append(factor)
            for j in range(k, n):
                A_matrix[i][j] = A_matrix[i][j] - factor*A_matrix[k][j]
    if abs(A_matrix[n-1][n-1]/s_vector[n-1]) < tolerance:
        error = -1
    return A_matrix, factors, error

def lu_decomp(A_matrix):
    n = len(A_matrix)
    solution = []
    tolerance = 1e-6
    for row in range(n):
        solution.append(0)
    s_vector = []
    for i in range(n):
        s_vector.append([])
    for i in range(n):
        s_vector[i] = abs(A_matrix[i][0])
        for j in range(1, n):
            if abs(A_matrix[i][j] > s_vector[i]):
                s_vector[i] = abs(A_matrix[i][j])
    [temp_A, factors, error] = find_factors(A_matrix, s_vector, tolerance)
    U_matrix = temp_A
    L_matrix = []
    for i in range(n):
        L_matrix.append([])
        for j in range(n):
            if i == j:
                L_matrix[i].append(1)
            elif j > i:
                L_matrix[i].append(0)
            else:
                L_matrix[i].append(factors[j][i-j-1])
    return L_matrix, U_matrix



if __name__ == '__main__':
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    # A = [[0.3, -0.2, 10], [0.1, 7, -0.3], [3, -0.1, -0.2]]
    print(lu_decomp(A))
