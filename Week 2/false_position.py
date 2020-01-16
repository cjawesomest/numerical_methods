## Cameron Calv ECE T480
# Finds the roots of a function using the false position approach. Inputs are the
# function(anonymous), upper and lower limits, maximum number of iterations, and maximum
# absolute relative error. The outputs should be the root and a table of iteration results.

def false_position(function_handle, upper_limit, lower_limit, max_iter, max_error):
    # Results key:
    #   [0]: iteration number
    #   [1]: low x
    #   [2]: high x
    #   [3]: mid x
    #   [4]: value at mid x
    #   [5]: percent error
    iter_results = []
    iter_count = 1
    if (upper_limit < lower_limit):
        temp = lower_limit
        lower_limit = upper_limit
        upper_limit = temp
    elif (upper_limit == lower_limit):
        return []
    low_x = lower_limit
    high_x = upper_limit
    mid_x = high_x - (function(high_x)*(low_x - high_x))/(function(low_x)-function(high_x))
    previous_mid_x = mid_x
    error = max_error + 1
    while (error >= max_error and iter_count <= max_iter):
        mid_x = high_x - (function(high_x)*(low_x - high_x))/(function(low_x)-function(high_x))

        low_value = function_handle(low_x)
        mid_value = function_handle(mid_x)
        high_value = function_handle(high_x)

        error = abs((mid_x - previous_mid_x) / (mid_x)) * 100

        iter_info = []
        iter_info.append(iter_count)
        iter_info.append(low_x)
        iter_info.append(high_x)
        iter_info.append(mid_x)
        iter_info.append(mid_value)
        iter_info.append(error)
        if (iter_count == 1):
            error = 100000000  # Some big number

        if (low_value < 0 and mid_value < 0) or (low_value > 0 and mid_value > 0):
            low_x = mid_x
        elif (high_value < 0 and mid_value < 0) or (high_value > 0 and mid_value > 0):
            high_x = mid_x
        else:
            iter_results.append(iter_info)
            root = mid_x
            return root, iter_results

        iter_results.append(iter_info)
        iter_count += 1
        previous_mid_x = mid_x
    root = mid_x
    return root, iter_results


if __name__ == '__main__':
    function = lambda x: (x ** 3 + 2 * (x ** 2) - 5 * x - 6)
    print(false_position(function, -2.8, -3.8, 100, 0.05))