## Cameron Calv ECE T480
# optim mdnewton-Calculates the location and maximum value of a multi-dimensional function
# using the Newton approach. Inputs are the multi-dimensional function (anonymous), gradient
# of function (anonymous), Hessian of function (anonymous),initial step size, maximum number
# of iterations, and maximum relative error. The output are the location and maximum value.
from optim_gradient import optim_gradient
from optim_hessian import optim_hessian

def optim_mdnewton(md_function_handle, gradient_handle, hessian_handle, init_step_size, max_iter, max_error):
    prev_x = init_step_size
    prev_y = init_step_size
    partial_x = gradient_handle[0]
    partial_y = gradient_handle[1]
    partial_xx = hessian_handle[0]
    partial_xy = hessian_handle[1]
    partial_yx = hessian_handle[2]
    partial_yy = hessian_handle[3]
    iter = 1
    while(1):
        hessian_determinant = partial_xx(prev_x, prev_y)*partial_yy(prev_x, prev_y) - partial_xy(prev_x, prev_y)*partial_yx(prev_x, prev_y)
        inv_hess = [partial_yy(prev_x, prev_y)/hessian_determinant, -partial_xy(prev_x, prev_y)/hessian_determinant, \
                    -partial_yx(prev_x, prev_y)/hessian_determinant, partial_xx(prev_x, prev_y)/hessian_determinant]
        current_x = prev_x - (inv_hess[0]*partial_x(prev_x, prev_y) + inv_hess[1]*partial_y(prev_x, prev_y))
        current_y = prev_y - (inv_hess[2]*partial_x(prev_x, prev_y) + inv_hess[3]*partial_y(prev_x, prev_y))

        if not current_x == 0:
            ea = abs((current_x - prev_x)/current_x)*100
        if ea <= max_error or iter >= max_iter:
            break
        iter += 1
    location = [current_x, current_y]
    max_val = md_function_handle(current_x, current_y)
    return location, max_val

if __name__ == '__main__':
    func = lambda x, y: 2*x*y + 2*x - (x**2) - 2*(y**2)
    func_partial_x = lambda x, y: 2*y + 2 - 2*x
    func_partial_y = lambda x, y: 2*x - 4*y
    func_partial_xx = lambda x, y: -2
    func_partial_xy = lambda x, y: 2
    func_partial_yx = lambda x, y: 2
    func_partial_yy = lambda x, y: -4
    [max_idxs, max_value] = optim_mdnewton(func, [func_partial_x, func_partial_y], [func_partial_xx, func_partial_xy,
            func_partial_yx, func_partial_yy], 1, 10000, 1e-4)
    print("Maximum value of " + str(max_value) + " occurs at x=" + str(max_idxs[0]) + " and y=" + str(max_idxs[1]))