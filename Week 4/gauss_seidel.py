## Cameron Calv ECE T480
# Uses the Gauss-Seidel method to solve system of equations. The input is the
# matrix A, the column vector b, and relaxation weighting factor λ. The output is a solution
# column vector X.

def gauss_seidel(A_matrix, b_vector, relaxation_factor):
    n = len(A_matrix)
    imax = 100
    e_min = 1e-5
    x_vector = []
    for i in range(n):
        x_vector.append(0)
        dummy = A_matrix[i][i]
        for j in range(n):
            A_matrix[i][j] = A_matrix[i][j]/dummy
        b_vector[i] = b_vector[i]/dummy
    for i in range(n):
        sum = b_vector[i]
        for j in range(n):
            if not i == j:
                sum -= A_matrix[i][j]*x_vector[j]
        x_vector[i] = sum
    iter = 1
    sentinel = 0
    while( not sentinel == 1 and iter < imax):
        if iter == 1:
            sentinel = 1
        for i in range(n):
            old = x_vector[i]
            sum = b_vector[i]
            for j in range(n):
                if not i == j:
                    sum -= A_matrix[i][j]*x_vector[j]
            x_vector[i] = relaxation_factor*sum + (1-relaxation_factor)*old
            if (sentinel == 1 and not x_vector[i] == 0):
                ea = abs((x_vector[i] - old)/x_vector[i])
                if (ea > e_min):
                    sentinel = 0
        iter += 1
    return x_vector



if __name__ == '__main__':
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]
    relax_dude = .87
    print(gauss_seidel(A, b, relax_dude))