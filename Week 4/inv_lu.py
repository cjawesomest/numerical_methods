## Cameron Calv ECE T480
# Calculates the inverse of a matrix using the LU decomposition approach. The input is
# a square matrix A. The output is a square matrix which is the inverse of matrix A.
from lu_decomp import lu_decomp
from gauss_elim import gauss_elim
from tpose import tpose

def inv_lu(sqr_matrix):
    n = len(sqr_matrix)
    identity = []
    inv_tpose = []
    [L_matrix, U_matrix] = lu_decomp(sqr_matrix)
    for i in range(n):
        identity.append([])
        for j in range(n):
            if i == j:
                identity[i].append(1)
            else:
                identity[i].append(0)
    for idk in range(n):
        b_vector = identity[idk]
        L_sol = gauss_elim(L_matrix, b_vector, 1e-6)
        U_sol = gauss_elim(U_matrix, L_sol, 1e-6)
        inv_tpose.append(U_sol)
    return tpose(inv_tpose)



if __name__ == '__main__':
    matrix = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    print(inv_lu(matrix))