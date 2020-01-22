## Cameron Calv ECE T480
# Solves a systems of nonlinear equations using the fixed point approach. Inputs are the function (anonymous),
# initial guess, maximum iterations, and maximum absolute
# relative error. The outputs should be the root and a table of iteration results.
import math

def nonlin_fixed_point(function_handles, init_guesses, max_iter, max_error):
    # Assumes functions have been properly manipulated
    if(len(function_handles) == 2 and len(init_guesses) == len(function_handles)):
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
        x_equals = function_handles[0]
        y_equals = function_handles[1]
        x_error = max_error + 1
        y_error = max_error + 1
        while (x_error >= max_error and y_error >= max_error and iter_count < max_iter):
            iter_info = []

            current_x = x_equals(prev_x, prev_y)
            current_y = y_equals(current_x, prev_y)

            x_error = abs((current_x - prev_x) / current_x) * 100
            y_error = abs((current_y - prev_y) / current_y) * 100

            iter_info.append(iter_count)
            iter_info.append(prev_x)
            iter_info.append(current_x)
            iter_info.append(prev_y)
            iter_info.append(current_y)
            iter_info.append(x_equals(current_x, current_y))
            iter_info.append(y_equals(current_x, current_y))


            iter_results.append(iter_info)
            iter_count += 1
            prev_x = current_x
            prev_y = current_y

        roots = [current_x, current_y]
        return roots, iter_results
    else:
        return [], []


if __name__ == '__main__':
    x_equals = lambda x, y: math.sqrt(10 - x*y)
    y_equals = lambda x, y: math.sqrt((57 - y)/(3*x))
    system = [x_equals, y_equals]
    output = nonlin_fixed_point(system, [1.5, 3.5], 100,  0.01)
    roots = output[0]
    results = output[1]
    print("Roots for X and Y:"+str(roots))
    print("Iteration|Previous X|Current X|Previous Y|Current Y|X Equals Value|Y Equals Value|X Error|Y Error")
    for entry in results:
        print(entry)