## Cameron Calv ECE T480
# • optim newton-Finds the maximum of a one-dimensional function between two bounds using
# Newton’s approach. The inputs are the first and second derivatives of the function(anonymous),
# lower and upper bounds, maximum number of iterations, and the maximum relative error.
# The outputs are the location of the maximum and the maximum value
import math

def optim_newton(function_handle, first_deriv_handle, second_deriv_handle, lower_bound, upper_bound, max_iter, max_error):
    init_guess = 0.5* (lower_bound + upper_bound)
    prev_x = init_guess
    iter = 0
    while(1):
        current_x = prev_x - first_deriv_handle(prev_x)/second_deriv_handle(prev_x)
        current_x_val = function_handle(prev_x)

        if not current_x == 0:
            ea = abs((current_x - prev_x)/current_x)*100
        if ea <= max_error or iter >= max_iter:
            break
        iter += 1
        prev_x = current_x
    max_location = current_x
    max_val = current_x_val

    return max_location, max_val

if __name__ == '__main__':
    func = lambda x: 2 * math.sin(x) - (x ** 2) / 10.0
    func_1_deriv = lambda x: 2 * math.cos(x) - (x/5.0)
    func_2_deriv = lambda x: (-2) * math.sin(x) - (1/5.0)

    lower = 0
    upper = 4
    max_i = 100
    max_e = 1e-4
    [idx_max, val_max] = optim_newton(func, func_1_deriv, func_2_deriv, lower, upper, max_i, max_e)
    print("Maximum value of " + str(val_max) + " occurs at x=" + str(idx_max))