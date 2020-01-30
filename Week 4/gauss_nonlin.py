## Cameron Calv ECE T480
# Solves a system of nonlinear equations using the Gauss elimination method.
# The input is the matrix of nonlinear equations F and the partial derivative matrix Z. The
# output is the solution X, which is a column vector.
from gauss_elim import gauss_elim

def gauss_nonlin(F_system, partial_deriv_Z_matrix):
    solution = [float('nan')]
    return solution

if __name__ == '__main__':
    system = [[]]
    partial_derivs = [[]]
    print(gauss_nonlin(system, partial_derivs))
