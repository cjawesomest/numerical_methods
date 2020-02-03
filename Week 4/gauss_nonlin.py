## Cameron Calv ECE T480
# Solves a system of nonlinear equations using the Gauss elimination method.
# The input is the matrix of nonlinear equations F and the partial derivative matrix Z. The
# output is the solution X, which is a column vector.
from gauss_elim import gauss_elim
from mmult import mmult
from tpose import tpose
import math

def gauss_nonlin(F_system, partial_deriv_Z_matrix):
    max_error = 1e-5
    tolerance = 1e-5
    initial_guesses = [2.5, 3.5]
    prev_guesses = initial_guesses
    # A_matrix = []
    # for i in range(len(partial_deriv_Z_matrix)):
    #     A_matrix.append([])
    #     for j in range(len(A_matrix)):
    #         A_matrix[i].append(partial_deriv_Z_matrix[i][j](prev_guesses))
    b_vector = mmult(partial_deriv_Z_matrix, tpose(prev_guesses))
    for i in range(len(b_vector)):
        b_vector[i] = -1*F_system[i](prev_guesses) + b_vector[i]
    gauss_elim(A_matrix, b_vector, tolerance)
    return #solution

if __name__ == '__main__':
    # Solution x=2, y=3
    system = [lambda x, y: x ** 2 + x * y - 10, lambda x, y: y + 3 * x * (y ** 2) - 57]
    partial_derivs = [[lambda x, y: 2 * x + y, lambda x, y: x],
                          [lambda x, y: 3 * (y ** 2), lambda x, y: 1 + 6 * x * y]]

    # Solution x≈1.39889, y≈1.34804, z≈1.06491
    # system = [lambda x, y, z: math.exp(x) + math.exp(y) - math.exp(z) - 5,
    #           lambda x, y, z: math.exp(2*x) - math.exp(2*y) + math.exp(2*z) - 10,
    #           lambda x, y, z: -1*math.exp(3*x) + math.exp(3*y) + math.exp(3*z) - 15]
    # partial_derivs = [[lambda x, y, z: math.exp(x), lambda x, y, z: math.exp(y), lambda x, y, z: -1*math.exp(z)],
    #           [lambda x, y, z: 2*math.exp(2*x), lambda x, y, z: -2*math.exp(2*y), lambda x, y, z: 2*math.exp(2*z)],
    #           [lambda x, y, z: -3*math.exp(3*x), lambda x, y, z: 3*math.exp(3*y), lambda x, y, z: 3*math.exp(3*z)]]
    print(gauss_nonlin(system, partial_derivs))
