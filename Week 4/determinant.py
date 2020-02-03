## Cameron Calv ECE T480
# Calculates the determinant using the Gauss elimination method. The input is a
# # square matrix. The output is the determinant.

def pivot(some_matrix, s_vector, k_value, iter, number_of_pivots_so_far):
    n = iter
    A_matrix = []
    for i in range(len(some_matrix)):
        A_matrix.append([])
        for j in range(len(some_matrix)):
            A_matrix[i].append(some_matrix[i][j])
    pivot = k_value
    big = abs(some_matrix[k_value][k_value]/s_vector[k_value])
    for i in range(k_value, n):
        dummy = abs(some_matrix[i][k_value]/s_vector[i])
        if dummy > big:
            big = dummy
            pivot = i
    if not pivot == k_value:
        for j in range(k_value, n):
            dummy = some_matrix[pivot][j]
            A_matrix[pivot][j] = some_matrix[k_value][j]
            A_matrix[k_value][j] = dummy
        number_of_pivots_so_far += 1
        dummy = s_vector[pivot]
        s_vector[pivot] = s_vector[k_value]
        s_vector[k_value] = dummy
    return A_matrix, s_vector, number_of_pivots_so_far


def eliminate(A_matrix, s_vector, tolerance, pivot_number):
    n = len(A_matrix)
    error = 0
    for k in range(n-1):
        [temp_A, temp_S, temp_pv] = pivot(A_matrix, s_vector, k, n, pivot_number)
        A_matrix = temp_A
        s_vector = temp_S
        pivot_number = temp_pv
        if abs(A_matrix[k][k]/s_vector[k]) < tolerance:
            error = -1
            break
        for i in range(k+1, n):
            factor = A_matrix[i][k]/A_matrix[k][k]
            for j in range(k, n):
                A_matrix[i][j] = A_matrix[i][j] - factor*A_matrix[k][j]
    if abs(A_matrix[n-1][n-1]/s_vector[n-1]) < tolerance:
        error = -1
    return A_matrix, pivot_number, error

def toUpperTriangular(A_matrix):
    n = len(A_matrix)
    solution = []
    tolerance = 1e-6
    pivot_number = 0
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
    [UT_matrix, pivot_number, error] = eliminate(A_matrix, s_vector, tolerance, pivot_number)
    return UT_matrix, pivot_number

def determinant(sqr_matrix):
    [upper_triangular_matrix, num_pivots] = toUpperTriangular(sqr_matrix)
    determ = 1
    for i in range(len(upper_triangular_matrix)):
        for j in range(len(upper_triangular_matrix)):
            if i == j:
                determ = determ*upper_triangular_matrix[i][j]
    determ = determ * (-1)**(num_pivots)
    return determ

if __name__ == '__main__':
    matrix = [[0.3, -0.2, 10], [0.1, 7, -0.3], [3, -0.1, -0.2]]
    print(determinant(matrix))