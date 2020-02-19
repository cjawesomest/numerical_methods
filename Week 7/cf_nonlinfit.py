## Cameron Calv ECE T480
# Finds the coefficients of a nonlinear function using nonlinear regression. The
# inputs are the ordinate and coordinate data values, model function (anonymous), and the
# Z matrix(matrix of partial derivatives-anonymous function). The output are the coefficients
# and coefficient of determination.

def cf_nonlinfit(ordinate_vals, coord_vals, model_func_handle, z_matrix_handles):
    coeff_vals = []
    coeff_determination = float('nan')

    return coeff_vals, coeff_determination



if __name__ == '__main__':
    print(cf_nonlinfit([], [], lambda x: x, [lambda x: x]))