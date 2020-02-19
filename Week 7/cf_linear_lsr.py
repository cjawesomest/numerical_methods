## Cameron Calv ECE T480
# Finds the coefficients that best fit data using linear regression. The inputs are the
# ordinate values and corresponding co-ordinate values, and the type of fit(linear, exponential,
# power, saturation-growth-rate). The outputs are the coefficient values and the coefficient of
# determination.

def cf_linear_lsr(ordinate_vals, coord_vals, fit_type):
    coeff_vals = []
    coeff_determination = float('nan')
    if fit_type.lower() == 'linear':
        return 'linear'
    elif fit_type.lower() == 'exponential':
        return 'exponential'
    elif fit_type.lower() == 'power':
        return 'power'
    elif fit_type.lower() == 'saturation-growth-rate':
        return 'saturation-growth-rate'
    else:
        return coeff_vals, coeff_determination



if __name__ == '__main__':
    print(cf_linear_lsr([], [], 'SATURATIONGROWTH-RATE'))