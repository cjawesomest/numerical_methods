## Cameron Calv ECE T480
# optim steepest ascent-Calculates the location and maximum value of a multi-dimensional
# function using the steepest ascent approach. Inputs are the multi-dimensional function
# (anonymous), gradient of function (anonymous), initial step size, maximum number of
# iterations, and maximum relative error. The output are the location and maximum value
from optim_golden import optim_golden

def optim_steepest_ascent(md_function_handle, gradient_handle, init_step_size, max_iter, max_error):
    max_location = float('nan')
    max_val = float('nan')
    prev_x = -1
    prev_y = 1
    iter = 1
    while(1):
        next_x = lambda h: prev_x + h*gradient_handle[0](prev_x, prev_y)
        next_y = lambda h: prev_y + h*gradient_handle[1](prev_x, prev_y)
        h_func = lambda h: md_function_handle(next_x(h), next_y(h))

        [h_max, h_max_val] = optim_golden(h_func, -init_step_size, init_step_size, max_iter, max_error)

        current_x = next_x(h_max)
        current_y = next_y(h_max)

        if not current_x == 0:
            ea = abs((current_x - prev_x)/current_x)*100
        if ea <= max_error or iter >= max_iter:
            break

        prev_x = current_x
        prev_y = current_y
        iter += 1
    max_location = [current_x, current_y]
    max_val = md_function_handle(current_x, current_y)
    return max_location, max_val

if __name__ == '__main__':
    func = lambda x, y: 2*x*y + 2*x - (x**2) - 2*(y**2)
    grad = [lambda x, y: 2*y + 2 - 2*x, lambda x, y: 2*x - 4*y]
    [max_idxs, max_value] = optim_steepest_ascent(func, grad, 1e-2, 10000, 1e-4)
    print("Maximum value of " + str(max_value) + " occurs at x=" + str(max_idxs[0]) + " and y=" + str(max_idxs[1]))