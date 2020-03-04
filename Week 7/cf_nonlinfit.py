## Cameron Calv ECE T480
# Finds the coefficients of a nonlinear function using nonlinear regression. The
# inputs are the ordinate and coordinate data values, model function (anonymous), and the
# Z matrix(matrix of partial derivatives-anonymous function). The output are the coefficients
# and coefficient of determination.
from gauss_elim import gauss_elim
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cf_nonlinfit(ordinate_vals, coord_vals):
    coeff_vals = []
    coeff_determination = float('nan')
    n = len(coord_vals) # Number of samples per variable

    mod_ordinates = [[]]
    try:
        if len(ordinate_vals[0]) > 1:
            order = len(ordinate_vals)  # Number of independant variables
            for sample in range(n):
                mod_ordinates[0].append(1)
            for dim in ordinate_vals:
                mod_ordinates.append(dim)
    except TypeError:
        # One dimensional data has been supplied
        order = 1
        for sample in range(n):
            mod_ordinates[0].append(1)
        mod_ordinates.append(list(ordinate_vals))

    coef_matrix = []
    val_matrix = []
    for i in range(order + 1):
        coef_matrix.append([])
        for j in range(order + 1):
            coef_matrix[i].append(0)
    for i in range(order+1):
        for j in range(i+1):
            total = 0
            for l in range(n):
                total += mod_ordinates[i][l]*mod_ordinates[j][l]
            coef_matrix[i][j] = total
            coef_matrix[j][i] = total
        total = 0
        for l in range(n):
            total += coord_vals[l]*mod_ordinates[i][l]
        val_matrix.append(total)
    coeff_vals = gauss_elim(coef_matrix, val_matrix, 1e-6)
    estimated_coord_vals = list()
    samp = 0
    for val in coord_vals:
        total = 0
        k = 0
        for coef in coeff_vals:
            total += coef * mod_ordinates[k][samp]
            k += 1
        estimated_coord_vals.append(total)
        samp += 1
    sum_expected_minus_mean_squared = sum(
        [((y - sum(coord_vals) / len(coord_vals)) ** 2) for y in estimated_coord_vals])
    sum_actual_minus_mean_squared = sum([((y - sum(coord_vals) / len(coord_vals)) ** 2) for y in coord_vals])
    coeff_determination = sum_expected_minus_mean_squared / sum_actual_minus_mean_squared
    return coeff_vals, coeff_determination

if __name__ == '__main__':
    list_1 = [[0, 2, 2.5, 1, 4, 7], [0, 1, 2, 3, 6, 2]]
    list_2 = [5, 10, 9, 0, 3, 27]
    print(cf_nonlinfit(list_1, list_2))
    [coefs , corr] = cf_nonlinfit(list_1, list_2)
    mod_list_1 = [[]]
    for sample in range(len(list_2)):
        mod_list_1[0].append(1)
    for dim in list_1:
        mod_list_1.append(dim)
    out_2 = list()
    samp = 0
    for val in list_2:
        total = 0
        k = 0
        for coef in coefs:
            total += coef * mod_list_1[k][samp]
            k += 1
        out_2.append(total)
        samp += 1
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(list_1[0], list_1[1], list_2, label="Data Plot", linewidth=3)
    ax.plot(list_1[0], list_1[1], out_2, label="Nonlinear Fit")
    plt.title("Plot for Nonlinear Fit")
    plt.gca().set_xlabel("Ordinate Values X1")
    plt.gca().set_ylabel("Ordinate Values X2")
    plt.gca().set_zlabel("Ordinate Values Y")
    plt.legend()
    plt.show()