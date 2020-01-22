## Cameron Calv ECE T480
# Solves a systems of nonlinear equations using the Newton-Rhapson
# approach. Inputs are the function (anonymous), matrix of derivatives(anonynous functions),initial
# guess, maximum iterations, and maximum absolute relative error. The outputs should be the
# root and a table of iteration results.

import math
def nonlin_newton_rhapson(function_handles, derivative_handles_matrix, init_guesses, max_iter, max_error):
    if (len(function_handles) == 2 or len(init_guesses) == len(function_handles) and len(derivative_handles_matrix) == len(function_handles)):
        # Results key:
        #   [0]: iteration number
        #   [1]: previous x
        #   [2]: current x
        #   [3]: previous y
        #   [4]: current y
        #   [5]: 1st function value at current x, y
        #   [6]: 2nd function value at current x, y
        #   [7]: percent error x
        #   [8]: percent error y
        iter_results = []
        iter_count = 1
        current_x = float('nan')
        current_y = float('nan')
        prev_x = init_guesses[0]
        prev_y = init_guesses[1]
        func_1 = function_handles[0]
        func_2 = function_handles[1]

        x_partial_x = derivative_handles_matrix[0][0]
        x_partial_y = derivative_handles_matrix[0][1]
        y_partial_x = derivative_handles_matrix[1][0]
        y_partial_y = derivative_handles_matrix[1][1]
        jacobian = lambda x, y: x_partial_x(x, y)*y_partial_y(x, y) - x_partial_y(x, y)*y_partial_x(x, y)
        jacobian_value = float('nan')

        x_error = max_error + 1
        y_error = max_error + 1
        while (x_error >= max_error and y_error >= max_error and iter_count < max_iter):
            iter_info = []

            jacobian_value = jacobian(prev_x, prev_y)
            current_x = prev_x - (func_1(prev_x, prev_y)*y_partial_y(prev_x, prev_y)-
                         func_2(prev_x, prev_y)*x_partial_y(prev_x, prev_y))/jacobian_value
            current_y = prev_y -(func_2(prev_x, prev_y)*x_partial_x(prev_x, prev_y)-
                         func_1(prev_x, prev_y)*y_partial_x(prev_x, prev_y))/jacobian_value

            x_error = abs((current_x - prev_x) / current_x) * 100
            y_error = abs((current_y - prev_y) / current_y) * 100

            iter_info.append(iter_count)
            iter_info.append(prev_x)
            iter_info.append(current_x)
            iter_info.append(prev_y)
            iter_info.append(current_y)
            iter_info.append(func_1(current_x, current_y))
            iter_info.append(func_2(current_x, current_y))

            iter_results.append(iter_info)
            iter_count += 1
            prev_x = current_x
            prev_y = current_y

        roots = [current_x, current_y]
        return roots, iter_results
    else:
        return [], []


if __name__ == '__main__':
    first_func = lambda x, y: x**2 + x*y - 10
    second_func = lambda x, y: y + 3*x*(y**2) - 57
    system = [first_func, second_func]

    x_partial_deriv_x = lambda x, y: 2*x + y
    x_partial_deriv_y = lambda x, y: x
    y_partial_deriv_x = lambda x, y: 3*(y**2)
    y_partial_deriv_y = lambda x, y: 1+6*x*y
    system_derivatives = [[x_partial_deriv_x, x_partial_deriv_y ],[y_partial_deriv_x, y_partial_deriv_y]]

    output = nonlin_newton_rhapson(system, system_derivatives, [1.5, 3.5], 100, 0.01)
    roots = output[0]
    results = output[1]
    print("Roots for X and Y:" + str(roots))
    print("Iteration|Previous X|Current X|Previous Y|Current Y|X Equals Value|Y Equals Value|X Error|Y Error")
    for entry in results:
        print(entry)
