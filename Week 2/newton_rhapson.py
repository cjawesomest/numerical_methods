## Cameron Calv ECE T480
# Finds the root of a function using the Newton-Rhapson approach. Inputs are
# the function(anonymous),the derivative of the function(anonymous),initial guess, maximum
# number of iterations, and maximum absolute relative error. The outputs should be the root
# and a table of iteration results

def newton_rhapson(function_handle, derivative_handle, init_guess, max_iter, max_error):
    iter_results = []
    root = float('nan')

    return root, iter_results