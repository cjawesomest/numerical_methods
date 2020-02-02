## Cameron Calv ECE T480
# Computes the LU decomposition of a square matrix A. The input is a square
# matrix A. The output are the lower diagonal matrix L and the upper diagonal matrix A.

def pivot(A_matrix, o_vector, s_vector, k_value):
    n = len(A_matrix)
    pivot = k_value
    big = abs(A_matrix[o_vector[k_value]][k_value]/s_vector[o_vector[k_value]])
    for i in range(k_value, n):
        dummy = abs(A_matrix[o_vector[i]][k_value]/s_vector[o_vector[i]])
        if dummy > big:
            big = dummy
            pivot = i
    dummy = o_vector[pivot]
    o_vector[pivot] = o_vector[k_value]
    o_vector[k_value] = dummy
    return A_matrix, o_vector, s_vector

def decompose(A_matrix, tolerance, o_vector, s_vector, error):
    n = len(A_matrix)
    for i in range(n):
        o_vector[i] = i
        s_vector[i] = abs(A_matrix[i][0])
        for j in range(1, n):
            if abs(A_matrix[i][j]) > s_vector[i]:
                s_vector[i] = abs(A_matrix[i][j])
    for k in range(n-1):
        [temp_A, temp_o, temp_s] = pivot(A_matrix, o_vector, s_vector, k)
        A_matrix = temp_A
        o_vector = temp_o
        s_vector = temp_s
        if abs(A_matrix[o_vector[k]][k]/s_vector[o_vector[k]]) < tolerance:
            error = -1
            print(A_matrix[o_vector[k]][k]/s_vector[o_vector[k]])
            break
        for i in range(k, n):
            factor = A_matrix[o_vector[i]][k]/A_matrix[o_vector[k]][k]
            A_matrix[o_vector[i]][k] = factor
            for j in range(k, n):
                A_matrix[o_vector[i]][j] = A_matrix[o_vector[i]][j] - factor*A_matrix[o_vector[k]][j]
        if abs(A_matrix[o_vector[k]][k]/s_vector[o_vector[k]]) < tolerance:
            error = -1
            print(A_matrix[o_vector[k]][k]/s_vector[o_vector[k]])
    return A_matrix, o_vector, s_vector, error


def lu_decomp(A_matrix, b_vector, tolerance):
    n = len(A_matrix)
    error = 0
    s_vector = []
    o_vector = []
    for i in range(n):
        s_vector.append([])
        o_vector.append([])
    [temp_A, temp_o, temp_s, error] = decompose(A_matrix, tolerance, o_vector, s_vector, error)
    A_matrix = temp_A
    o_vector = temp_o
    s_vector = temp_s
    if not error == -1:
        substitute(A_matrix, o_vector, b_vector, solution)



if __name__ == '__main__':
    matrix = [[]]
    print(lu_decomp(matrix))