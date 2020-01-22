## Cameron Calv ECE T480
# Finds the root of a function using the modified secant approach. Inputs are
# the function(anonymous),initial guess,perturbation fraction, maximum number of iterations,
# and maximum absolute relative error. The outputs should be the root and a table of iteration
# results.

def modified_secant(function_handle, init_guess, perturbation_fraction, max_iter, max_error):
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

        current_x = prev_x - (perturbation_fraction*prev_x*function_handle(prev_x))\
                    /(function_handle(prev_x+perturbation_fraction*prev_x)-function_handle(prev_x))
        error = abs((current_x - prev_x) / current_x) * 100

        iter_info.append(iter_count)
        iter_info.append(prev_x)
        iter_info.append(current_x)
        iter_info.append(function_handle(current_x))
        iter_info.append(error)

        iter_results.append(iter_info)
        iter_count += 1
        prev_x = current_x

    root = current_x

    return root, iter_results

if __name__ == '__main__':
    function = lambda x: x**3 - x**2*(3541/2500) - x*(48741701/5000000) + (41249804989/2500000000)
    output = modified_secant(function, 4, 1*(10**(-6)), 100, 5*(10**(-6)))
    root = output[0]
    results = output[1]
    print("Root for function: " + str(root))
    print("Iteration|Previous X|Current X|Value at Current X|Error")
    for entry in results:
        print(entry)