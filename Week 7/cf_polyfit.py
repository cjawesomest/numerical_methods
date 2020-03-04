## Cameron Calv ECE T480
# Finds the coefficients of a polynomial fit using polynomial
# regression (matrix approach). The inputs are the ordinate and
# coordinate data values. The output are the coefficients and coefficient of determination.
from gauss_elim import gauss_elim
from matplotlib import pyplot as plt

def cf_polyfit(ordinate_vals, coord_vals, order):
    n = len(ordinate_vals)
    if (n < order + 1):
        return []
    coef_matrix = []
    val_matrix = []
    for i in range(order+1):
        coef_matrix.append([])
        for j in range(order+1):
            coef_matrix[i].append(0)
    coeff_vals = []
    coeff_determination = float('nan')
    for i in range(order+1):
        for j in range(i+1):
            k = i + j
            total = 0
            for l in range(n):
                total = total + ordinate_vals[l]**k
            coef_matrix[i][j] = total
            coef_matrix[j][i] = total
        total = 0
        for l in range(n):
            total = total + coord_vals[l]*ordinate_vals[l]**(i)
        val_matrix.append(total)
    # print(coef_matrix)
    # print(val_matrix)
    coeff_vals = gauss_elim(coef_matrix, val_matrix, 1e-6)
    estimated_coord_vals = list()
    for x in ordinate_vals:
        total = 0
        expo = 0
        for coef in coeff_vals:
            total += coef*(x**expo)
            expo += 1
        estimated_coord_vals.append(total)
    sum_expected_minus_mean_squared = sum([((y - sum(coord_vals)/len(coord_vals)) ** 2) for y in estimated_coord_vals])
    sum_actual_minus_mean_squared = sum([((y - sum(coord_vals)/len(coord_vals)) ** 2) for y in coord_vals])
    coeff_determination = sum_expected_minus_mean_squared / sum_actual_minus_mean_squared
    return coeff_vals, coeff_determination



if __name__ == '__main__':
    list_1 = [0, 1, 2, 3, 4, 5]
    list_2 = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
    print(cf_polyfit(list_1, list_2, 2))
    [coefs, correlate] = cf_polyfit(list_1, list_2, 2)
    out_2 = list()
    for x in list_1:
        total = 0
        expo = 0
        for coef in coefs:
            total += coef * (x ** expo)
            expo += 1
        out_2.append(total)
    plt.plot(list_1, list_2)
    plt.plot(list_1, out_2)
    plt.title("Plot for Polynomial Fit Calv HW 5")
    plt.xlabel("Ordinate Values")
    plt.ylabel("Coordinate Values")
    plt.show()