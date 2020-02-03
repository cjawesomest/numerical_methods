## Cameron Calv ECE T480
from determinant import determinant
from gauss_elim import gauss_elim
from gauss_jordan import gauss_jordan
from gauss_nonlin import gauss_nonlin
from gauss_seidel import gauss_seidel
from inv_lu import inv_lu
from lu_decomp import lu_decomp
from matinv import matinv
from mmult import mmult
from tpose import tpose

if __name__ == '__main__':
    #Problem 1 (Solution: x = 68/69 = 0.98550724637, y = 101/69 = 1.46376811594, z = 21/23 = 0.91304347826)
    print("Problem 1: Sole a system of equations!")
    prob_1_system = [[0, -3, 7], [1, 2, -1], [5, -2, 0]]
    prob_1_rhs = [2, 3, 2]
    deter = determinant(prob_1_system)
    print("a)\tThe determinant of this system is:" + str(deter))
    cramer_sol = []
    for i in range(len(prob_1_rhs)):
        numerator_matrix = []
        for j in range(len(prob_1_system)):
            numerator_matrix.append([])
            for k in range(len(prob_1_system[0])):
                if i == k:
                    numerator_matrix[j].append(prob_1_rhs[j])
                else:
                    numerator_matrix[j].append(prob_1_system[j][k])
        cramer_sol.append(determinant(numerator_matrix)/deter)
    print("b)\tSolved using Cramer's rule: "+str(cramer_sol))
    # prob_1_system = [[0, -3, 7], [1, 2, -1], [5, -2, 0]]
    # prob_1_rhs = [2, 3, 2]
    print("c)\tSolved using Gauss Elimination: "+str(gauss_elim(prob_1_system, prob_1_rhs, 1e-6)))
    print("d)\tSolved using Gauss Jordan: "+str(gauss_jordan(prob_1_system, prob_1_rhs, 1e-6)))
    try:
        print("e)\tSolved using Gauss Seidel: "+str(gauss_seidel(prob_1_system, prob_1_rhs, 0.8)))
    except ZeroDivisionError:
        print("e)\tCannot by solved using Gauss Seidel! We have diagonal zero elements!")
    mult_inv_sol = mmult(matinv(prob_1_system), prob_1_rhs)
    for i in range(len(mult_inv_sol)): mult_inv_sol[i] = mult_inv_sol[i][0]
    print("f)\tSolved using mmult and matinv: "+str(mult_inv_sol))

    #Problem 2
    print("\nProblem 2: Solve another system of equations!")
    prob_2_system = [[2, -6, -1], [-3, -1, 7], [-8, 1, -2]]
    prob_2_rhs = [-38, -32, -20]

    #Problem 3
    print("\nProblem 3: Solve some equations with LU!")
    prob_3_system = [[3, -2, 1], [2, 6, -4], [-1, -2, 5]]
    prob_3_rhs = [-10, 44, -26]

    #Problem 4
    print("\nProblem 4: Figure out an engineering problem!")
    prob_4_system = [[15, 17, 19], [0.3, 0.4, 0.55], [1.0, 1.2, 1.5]]
    prob_4_rhs = [3890, 95, 282]

    #Problem 5
    print("\nProblem 5: Solve a circuit problem now!")
    prob_5_system = [[55, -20, 0, -25], [0, 1, 0, 0], [0, -1, 37, -4], [-25, 0, -4, 29]]
    prob_5_rhs = [0, -10, 0, 100]