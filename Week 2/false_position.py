## Cameron Calv ECE T480
# Finds the roots of a function using the false position approach. Inputs are the
# function(anonymous), upper and lower limits, maximum number of iterations, and maximum
# absolute relative error. The outputs should be the root and a table of iteration results.

def false_position(function_handle, upper_limit, lower_limit, max_iter, max_error):
    iter_results = []
    root = float('nan')

    return root, iter_results