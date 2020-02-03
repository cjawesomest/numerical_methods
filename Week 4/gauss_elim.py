## Cameron Calv ECE T480
# Performs Gauss elimination(with partial pivoting). Inputs are the array of system
# coefficients (the A matrix) and the resultant column vector (the b vector). The output is a
# column vector X that is the solution of the system of equations Ax = b.
def pivot(some_matrix, some_rhs, s_vector, k_value, iter):
    n = iter
    A_matrix = []
    b_vector = []
    for i in range(len(some_matrix)):
        A_matrix.append([])
        b_vector.append(some_rhs[i])
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
        dummy = some_rhs[pivot]
        b_vector[pivot] = some_rhs[k_value]
        b_vector[k_value] = dummy
        dummy = s_vector[pivot]
        s_vector[pivot] = s_vector[k_value]
        s_vector[k_value] = dummy
    return A_matrix, b_vector, s_vector


def eliminate(A_matrix, s_vector, b_vector, tolerance):
    n = len(A_matrix)
    error = 0
    for k in range(n-1):
        [temp_A, temp_B, temp_S] = pivot(A_matrix, b_vector, s_vector, k, n)
        A_matrix = temp_A
        b_vector = temp_B
        s_vector = temp_S
        if abs(A_matrix[k][k]/s_vector[k]) < tolerance:
            error = -1
            break
        for i in range(k+1, n):
            factor = A_matrix[i][k]/A_matrix[k][k]
            for j in range(k+1, n):
                A_matrix[i][j] = A_matrix[i][j] - factor*A_matrix[k][j]
            b_vector[i] = b_vector[i] - factor * b_vector[k]
    if abs(A_matrix[n-1][n-1]/s_vector[n-1]) < tolerance:
        error = -1
    return A_matrix, b_vector, error

def substitute(A_matrix, b_vector, x_vector):
    n = len(A_matrix)
    x_vector[n-1] = b_vector[n-1] / A_matrix[n-1][n-1]
    for i in reversed(range(n-1)):
        total = 0
        for j in range(i, n):
            total += A_matrix[i][j]*x_vector[j]
        x_vector[i] = (b_vector[i] - total)/A_matrix[i][i]
    return A_matrix, b_vector, x_vector

def gauss_elim(A_matrix, b_vector, tolerance):
    n = len(A_matrix)
    solution = []
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
    [temp_A, temp_B, error] = eliminate(A_matrix, s_vector, b_vector, tolerance)
    A_matrix = temp_A
    b_vector = temp_B
    if not error == -1:
        [temp_A, temp_B, temp_sol] = substitute(A_matrix, b_vector, solution)
        A_matrix = temp_A
        b_vector = temp_B
        solution = temp_sol
    return solution



if __name__ == '__main__':
    A = [[70, 1, 0], [60, -1, 1], [40, 0, -1]]
    b = [636.7, 518.6, 307.4]
    # A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    # b = [7.85, -19.3, 71.4]
    # A = [[-0.2, -0.1, 3], [-0.3, 7, 0.1], [10, -0.2, 0.3]]
    # b = [7.85, -19.3, 71.4]
    tolerance = 1e-6

    print(gauss_elim(A, b, tolerance))
