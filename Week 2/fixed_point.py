## Cameron Calv ECE T480
# Finds the root of a function using the fixed point approach. Inputs are the function(anonymous),
# initial guess, maximum number of iterations, and maximum absolute relative error. The outputs
# should be the root and a table of iteration results.
import math

def fixed_point(function_handle, init_guess, max_iter, max_error):
    # Results key:
    #   [0]: iteration number
    #   [1]: previous x
    #   [2]: current x
    #   [3]: percent error
    iter_results = []

    function_plus_x = lambda x: function_handle(x) + x
    prev_x = init_guess
    current_x = float('nan')
    iter_count = 1
    error = max_error + 1
    while(error >= max_error and iter_count < max_iter):
        iter_info = []

        current_x = function_plus_x(prev_x)
        error = abs((current_x - prev_x)/current_x)*100

        iter_info.append(iter_count)
        iter_info.append(prev_x)
        iter_info.append(current_x)
        iter_info.append(error)
        iter_results.append(iter_info)

        iter_count += 1
        prev_x = current_x

    root = current_x

    return root, iter_results

if __name__ == '__main__':
    function = lambda x: math.exp(-x) - x
    print(fixed_point(function, 0, 100, 0.05))