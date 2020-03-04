## Cameron Calv ECE T480
# Finds the coefficients that best fit data using linear regression. The inputs are the
# ordinate values and corresponding co-ordinate values, and the type of fit(linear, exponential,
# power, saturation-growth-rate). The outputs are the coefficient values and the coefficient of
# determination.
import math
from matplotlib import pyplot as plt

def cf_linear_lsr(ordinate_vals, coord_vals, fit_type):
    coeff_vals = []
    coeff_determination = float('nan')
    if not len(ordinate_vals) == len(coord_vals):
        return [], []
    # Output format : Y = a0 + a1*X
    if fit_type.lower() == 'linear':
        # Code credit goes to Mr. Cameron James Calv who wrote this linear regression code
        # for his ECE303 class
        # Thanks 'Me Of The Past' *Thumbs Up*
        if (len(ordinate_vals) == len(coord_vals)):
            n = len(ordinate_vals)
            sum_x = sum(ordinate_vals)
            sum_y = sum(coord_vals)
            mean_x = sum(ordinate_vals) / len(ordinate_vals)
            mean_y = sum(coord_vals) / len(coord_vals)
            sum_x_square = sum([x ** 2 for x in ordinate_vals])
            sum_y_square = sum([y ** 2 for y in coord_vals])
            sum_xy = sum(ordinate_vals[i] * coord_vals[i] for i in range(n))
            ## Residual code in case a 'through origin approach is desired
            # if (through_origin):
            #     coef_a0 = sum_xy / sum_x_square
            #     estimated_coord_vals = list()
            #     for x in ordinate_vals:
            #         estimated_coord_vals.append(coef_a0 * x)
            #     sum_ei_squared = sum([((coord_vals[i] - coef_a0 * ordinate_vals[i]) ** 2) for i in range(n)])
            #     sum_actual_minus_mean_squared = sum([((y - mean_y) ** 2) for y in coord_vals])
            #     coeff_determination = 1 - (sum_ei_squared / sum_actual_minus_mean_squared)
            #     return [coef_a0, coeff_determination]
            # else:
            coef_a1 = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_square) - (sum_x ** 2))
            coef_a0 = mean_y - coef_a1 * mean_x
            estimated_coord_vals = list()
            for x in ordinate_vals:
                estimated_coord_vals.append(coef_a0 + coef_a1 * x)
            sum_expected_minus_mean_squared = sum([((y - mean_y) ** 2) for y in estimated_coord_vals])
            sum_actual_minus_mean_squared = sum([((y - mean_y) ** 2) for y in coord_vals])
            coeff_determination = sum_expected_minus_mean_squared / sum_actual_minus_mean_squared
            return [coef_a0, coef_a1], coeff_determination
    # Output format : Y = a*exp(b*X)
    elif fit_type.lower() == 'exponential':
        [[coef_a0, coef_a1] , coeff_determination] = cf_linear_lsr(ordinate_vals,
                [math.log(y) for y in coord_vals], 'linear')
        coef_a0 = math.exp(coef_a0)
        return [coef_a0, coef_a1], coeff_determination
    # Output format : Y = a*(X^b)
    elif fit_type.lower() == 'power':
        [[coef_a0, coef_a1], coeff_determination] = cf_linear_lsr([math.log10(x) for x in ordinate_vals],
                [math.log10(y) for y in coord_vals], 'linear')
        coef_a0 = 10**coef_a0
        return [coef_a0, coef_a1], coeff_determination
    # Output format : Y = a*(X/(b + X))
    elif fit_type.lower() == 'saturation-growth-rate':
        [[coef_a0, coef_a1], coeff_determination] = cf_linear_lsr([1/x for x in ordinate_vals],
                [1/y for y in coord_vals], 'linear')
        coef_a1 = coef_a1/coef_a0
        coef_a0 = 1/coef_a0
        return [coef_a0, coef_a1], coeff_determination
    else:
        return coeff_vals, coeff_determination



if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    list_2 = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5]
    # list_1 = [0.7, 1.2, 2.1, 3.2, 5.8];
    # list_2 = [7.0, 5.0, 3.0, 2.0, 1.0];
    # list_1 = [1.2, 2.2, 3.5, 5.0, 7.9];
    # list_2 = [8.0, 6.8, 5.2, 3.0, 1.0];
    # list_1 = [1, 2, 3, 4, 5]
    # list_2 = [0.5, 1.7, 3.4, 5.7, 8.4]
    # configuration = 'Linear'
    # configuration = 'Exponential'
    # configuration = 'Power'
    configuration = 'Saturation-Growth-Rate'
    [[coef_1, coef_2], r] = cf_linear_lsr(list_1, list_2, configuration)
    out_2 = []
    if configuration.lower() == 'linear':
        for val in list_1:
            out_2.append(coef_1 + coef_2*val)
    elif configuration.lower() == 'exponential':
        for val in list_1:
            out_2.append(coef_1*math.exp(coef_2*val))
    elif configuration.lower() == 'power':
        for val in list_1:
            out_2.append(coef_1*(val**coef_2))
    elif configuration.lower() == 'saturation-growth-rate':
        for val in list_1:
            out_2.append(coef_1*(val/(coef_2 + val)))
    print(cf_linear_lsr(list_1, list_2, configuration.lower()))
    plt.plot(list_1, list_2)
    plt.plot(list_1, out_2)
    plt.title("Plot for "+configuration+" Fit Calv HW 5")
    plt.xlabel("Ordinate Values")
    plt.ylabel("Coordinate Values")
    plt.show()