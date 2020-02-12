## Cameron Calv ECE T480
# • optim random-Finds the location and maximum value of a two-dimensional function using the
# random search approach. The inputs are the two-dimensional function(anonymous), bounds
# for each dimension, and the number of trials. The outputs are the location of the maximum
# and the maximum value
import random
import math

def optim_random(twod_function_handle, lower_bounds, upper_bounds, num_trials):
    upper_bound_x = upper_bounds[0]
    upper_bound_y = upper_bounds[1]
    lower_bound_x = lower_bounds[0]
    lower_bound_y = lower_bounds[1]
    if upper_bound_x < lower_bound_x:
        temp = lower_bound_x
        lower_bound_x = upper_bound_x
        upper_bound_x = temp
    if upper_bound_y < lower_bound_y:
        temp = lower_bound_y
        lower_bound_y = upper_bound_y
        upper_bound_y = temp
    max_location_x = float('nan')
    max_location_y = float('nan')
    max_val = -1e10
    trial = 0
    while(1):
        guess_x = lower_bound_x + (upper_bound_x - lower_bound_x) * random.random()
        guess_y = lower_bound_y + (upper_bound_y - lower_bound_y) * random.random()
        guess_val = twod_function_handle(guess_x, guess_y)

        if guess_val > max_val:
            max_location_x = guess_x
            max_location_y = guess_y
            max_val = guess_val
        if trial > num_trials:
            break
        trial += 1

    return [max_location_x, max_location_y], max_val

if __name__ == '__main__':
    func = lambda x, y: y - x - 2*(x**2) - 2*x*y - (y**2)
    upper = [2, 3]
    lower = [-2, 1]
    max_iter = 10000
    [max_idxs, max_value] = optim_random(func, lower, upper, max_iter)
    print("Maximum value of " + str(max_value) + " occurs at x=" + str(max_idxs[0]) + " and y=" + str(max_idxs[1]))