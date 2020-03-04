## Cameron Calv ECE T480
# Finds the coefficients of a polynomial fit using polynomial
# regression (matrix approach). The inputs are the ordinate and
# coordinate data values. The output are the coefficients and coefficient of determination.
from gauss_elim import gauss_elim

def cf_polyfit(ordinate_vals, coord_vals, order):
    n = len(ordinate_vals)
    if (n < order + 1):
        return []
    coef_matrix = []
    for i in range(n):
        coef_matrix.append([])
        for j in range(n):
            coef_matrix[i].append(0)
    coeff_vals = []
    coeff_determination = float('nan')
    for i in range(order):
        for j in range(i-1):
            k = i + j
            sum = 0
            for l in range(n):
                sum = sum + ordinate_vals[l]**k
            coef_matrix[i][j] = sum
            coef_matrix[j][i] = sum
        sum = 0
        for l in range(n):
            sum = sum + coord_vals[l]*ordinate_vals[l]**(i)
        coef_matrix[i][order+2] = sum # This line seems weird

    return coeff_vals, coeff_determination



if __name__ == '__main__':
    print(cf_polyfit([], []))