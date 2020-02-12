## Cameron Calv ECE T480
# optim hessian-Calculates the Hessian of a multi-dimensional function. The
# inputs are a column vector of partial derivatives (anonymous) and a column vector
# representing the location
# used to calculate the gradient. The output is the Hessian.

def optim_hessian(col_vect_partial_derivs, col_vect_location):
    hessian = float('nan')
    hess_point = col_vect_location
    partial_xx = col_vect_partial_derivs[0]
    partial_xy = col_vect_partial_derivs[1]
    partial_yx = col_vect_partial_derivs[2]
    partial_yy = col_vect_partial_derivs[3]
    hessian = partial_xx(hess_point[0], hess_point[1])*partial_yy(hess_point[0], hess_point[1]) -\
              partial_xy(hess_point[0], hess_point[1])*partial_yx(hess_point[0], hess_point[1])
    return hessian

if __name__ == '__main__':
    func = lambda x, y: x * (y ** 2)
    func_partial_x = lambda x, y: (y ** 2)
    func_partial_y = lambda x, y: 2 * x * y
    func_partial_xx = lambda x, y: 0
    func_partial_xy = lambda x, y: 2*y
    func_partial_yx = lambda x, y: 2*y
    func_partial_yy = lambda x, y: 2*x
    point = [2, 2]
    hess = optim_hessian([func_partial_xx, func_partial_xy, func_partial_yx, func_partial_yy], point)
    print("The hessian has a value of " + str(hess) + " at the point " + str(point))