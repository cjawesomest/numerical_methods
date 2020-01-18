## Cameron Calv ECE T480
# Finds the root of a function using the Newton-Rhapson approach. Inputs are
# the function(anonymous),the derivative of the function(anonymous),initial guess, maximum
# number of iterations, and maximum absolute relative error. The outputs should be the root
# and a table of iteration results
import math

def newton_rhapson(function_handle, derivative_handle, init_guess, max_iter, max_error):
    # Results key:
    #   [0]: iteration number
    #   [1]: previous x
    #   [2]: current x
    #   [3]: function value at current x
    #   [4]: percent error
    iter_results = []
    iter_count = 1
    current_x = float('nan')
    prev_x = init_guess
    error = max_error + 1
    while(error >= max_error and iter_count < max_iter):
        iter_info = []
        current_x = prev_x - (function_handle(prev_x))/(derivative_handle(prev_x))
        error = abs((current_x - prev_x) / current_x) * 100

        iter_info.append(iter_count)
        iter_info.append(prev_x)
        iter_info.append(current_x)
        iter_info.append(function_handle(current_x))
        iter_info.append(error)

        iter_results.append(iter_info)

        prev_x = current_x
        iter_count += 1
    root = current_x

    return root, iter_results

if __name__ == '__main__':
    function = lambda x: 3- 2*math.exp(x)
    derivative = lambda x: -2*math.exp(x)
    print(newton_rhapson(function, derivative, 0, 100, 0.05))