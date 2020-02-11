## Cameron Calv ECE T480
# • optim gradient-Calculates the gradient of a multi-dimensional function. The inputs are a
# column vector of partial
# derivatives (anonymous) and a column vector representing the location
# used to calculate the gradient. The output is the gradient.
import math

def optim_gradient(col_vect_partial_derivs, col_vect_location):
    gradient = float('nan')
    grad_point = col_vect_location
    partial_vals = []
    for deriv in col_vect_partial_derivs:
        partial_vals.append(deriv(grad_point[0], grad_point[1]))
    try:
        max_direction = math.atan(partial_vals[1]/partial_vals[0])
        slope = math.sqrt((partial_vals[0]**2)+(partial_vals[1]**2))
        return slope
    except ZeroDivisionError:
        return gradient




if __name__ == '__main__':
    func = lambda x, y: x*(y**2)
    func_partial_x = lambda x, y: (y**2)
    func_partial_y = lambda x, y: 2*x*y
    point = [2, 2]
    grad = optim_gradient([func_partial_x, func_partial_y], point)
    print("The gradient has a value of "+str(grad)+" at the point "+str(point))