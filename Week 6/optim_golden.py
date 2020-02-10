## Cameron Calv ECE T480
# • optim golden-Finds the maximum of a one-dimensional function between two bounds using
# the golden rule. The inputs are the function(anonymous), lower and upper bounds, maximum
# number of iterations, and the maximum relative error. The outputs are the location of the
# maximum and the maximum value.
import math

def optim_golden(function_handle, lower_bound, upper_bound, max_iter, max_error):
    if upper_bound < lower_bound:
        temp = lower_bound
        lower_bound = upper_bound
        upper_bound = temp
    phi = (math.sqrt(5) - 1)/2
    iter = 0
    while(1):
        d = (phi)*(upper_bound - lower_bound)
        x1 = lower_bound + d
        x2 = upper_bound - d
        if function_handle(x1) < function_handle(x2):
            xopt = x1
            upper_bound = x1
        else:
            xopt = x2
            lower_bound = x2
        iter += 1
        if not xopt == 0:
            ea = (2 - phi) * abs((upper_bound - lower_bound)/xopt) * 100
        if ea <= max_error or iter >= max_iter:
            break
    max_idx = xopt
    max_value = function_handle(xopt)
    return max_idx, max_value

if __name__ == '__main__':
    func = lambda x: 2*math.sin(x) - (x**2)/10.0
    lower = 0
    upper = 4
    max_i = 100
    max_e = 1e-4
    [idx_max, val_max] = optim_golden(func, lower, upper, max_i, max_e)
    print("Maximum value of "+str(val_max)+" occurs at x="+str(idx_max))
