## Cameron Calv ECE T480
# optim parabolic-Finds the maximum of a one-dimensional function between two bounds using
# the parabolic interpolation approach. The inputs are the function(anonymous), lower and
# upper bounds, maximum number of iterations, and the maximum relative error. The outputs
# are the location of the maximum and the maximum value.
import math

def optim_parabolic(function_handle, lower_bound, upper_bound, max_iter, max_error):
    if upper_bound < lower_bound:
        temp = lower_bound
        lower_bound = upper_bound
        upper_bound = temp
    x0 = lower_bound
    x1 = (lower_bound + upper_bound) / 2
    x2 = upper_bound
    iter = 0
    while(1):
        val_x0 = function_handle(x0)
        val_x1 = function_handle(x1)
        val_x2 = function_handle(x2)

        x3 = (val_x0*(x1**2-x2**2)+val_x1*(x2**2-x0**2)+val_x2*(x0**2-x1**2))/\
             (2*val_x0*(x1-x2)+2*val_x1*(x2-x0)+2*val_x2*(x0-x1))

        x0 = x1
        x1 = x2
        x2 = x3

        if not x3 == 0:
            ea = abs((upper_bound - lower_bound)/x3) * 100
        if ea <= max_error or iter >= max_iter:
            break
        iter += 1
    max_location = x3
    max_val = function_handle(max_location)

    return max_location, max_val

if __name__ == '__main__':
    func = lambda x: 2 * math.sin(x) - (x ** 2) / 10.0
    lower = 0
    upper = 4
    max_i = 100
    max_e = 1e-4
    [idx_max, val_max] = optim_parabolic(func, lower, upper, max_i, max_e)
    print("Maximum value of " + str(val_max) + " occurs at x=" + str(idx_max))
