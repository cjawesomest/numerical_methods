## Cameron Calv ECE T480
# Solves a systems of nonlinear equations using the Newton-Rhapson
# approach. Inputs are the function (anonymous), matrix of derivatives(anonynous functions),initial
# guess, maximum iterations, and maximum absolute relative error. The outputs should be the
# root and a table of iteration results.

def nonlin_newton_rhapson(function_handle, derivative_handles_matrix, init_guess, max_iter, max_error):
    iter_results = []
    root = float('nan')

    return root