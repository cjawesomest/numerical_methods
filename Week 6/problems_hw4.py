## Cameron Calv ECE T480
from optim_golden import optim_golden
from optim_gradient import optim_gradient
from optim_hessian import optim_hessian
from optim_mdnewton import optim_mdnewton
from optim_newton import optim_newton
from optim_parabolic import optim_parabolic
from optim_random import optim_random
from optim_steepest_ascent import optim_steepest_ascent
import math
if __name__ == '__main__':
    #Problem 1
    print("Problem 1: Find max of force function!")
    eps_not = 8.85e-12
    q = 2e-5
    rad = 0.9

    max_iter = 10000
    max_error = 1e-4
    upper_limit = 2
    lower_limit = 0
    prob_1_func = lambda x: ((q**2)*x)/((((x**2)+(rad**2))**(3/2))*(4*math.pi*eps_not))
    prob_1_deriv = lambda x: ((q**2)/(4*math.pi*eps_not))*(rad**2-2*(x**2))/(((rad**2) + (x**2))**(5/2))
    prob_1_2nd_deriv = lambda x: (3 * (q**2) * x * (2 *(x**2) - 3 * (rad**2)))/(4 * math.pi * eps_not * (((rad**2) + (x**2))**(7/2)))
    [x_max_gold, gold_val] = optim_golden(prob_1_func, lower_limit, upper_limit, max_iter, max_error)
    [x_max_para, para_val] = optim_parabolic(prob_1_func, lower_limit, upper_limit, max_iter, max_error)
    [x_max_newt, newt_val] = optim_newton(prob_1_func, prob_1_deriv, prob_1_2nd_deriv, lower_limit, upper_limit/2, max_iter, max_error)
    [x_max_rand, rand_val] = optim_random(lambda x, y: prob_1_func(x), [lower_limit, lower_limit], [upper_limit, upper_limit], max_iter)
    print("\t Golden Optimization found a max of "+str(gold_val)+" at x="+str(x_max_gold))
    print("\t Parabolic Optimization found a max of " + str(para_val) + " at x=" + str(x_max_para))
    print("\t\t -Note the fact that the parabolic optimization does not converge for this problem!")
    print("\t Newton Optimization found a max of " + str(newt_val) + " at x=" + str(x_max_newt))
    print("\t Random Optimization found a max of " + str(rand_val) + " at x=" + str(x_max_rand[0]))

    #Problem 2
    print("\nProblem 2: Determine the maximum torque")
    upper_limit = 2
    lower_limit = 0
    prob_2_func = lambda s: (15*(s-(s**2)))/((1-s)*(4*(s**2) - 3*s + 4))
    [x_max_gold, gold_val] = optim_golden(prob_2_func, lower_limit, upper_limit, max_iter, max_error)
    [x_max_rand, rand_val] = optim_random(lambda x, y: prob_2_func(x), [lower_limit, lower_limit],
                                          [upper_limit, upper_limit], max_iter)
    print("\t Golden Optimization found a max of " + str(gold_val) + " at s=" + str(x_max_gold))
    print("\t Random Optimization found a max of " + str(rand_val) + " at s=" + str(x_max_rand[0]))

    #Problem 3
    print("\nProblem 3: Find load for which power is maximum!")
    upper_limit = 10
    lower_limit = 0
    max_error = 1e-6
    R1 = 10
    R2 = 20
    V = 20
    prob_3_func = lambda RL: (((V*(((1/R2)+(1/RL))**(-1)))/(R1 + (((1/R2)+(1/RL))**(-1))))**2)/RL
    [x_max_gold, gold_val] = optim_golden(prob_3_func, lower_limit, upper_limit, max_iter, max_error)
    [x_max_rand, rand_val] = optim_random(lambda x, y: prob_3_func(x), [lower_limit, lower_limit],
                                          [upper_limit, upper_limit], max_iter)
    print("\t Golden Optimization found a max power of " + str(gold_val) + " at RL=" + str(x_max_gold))
    print("\t Random Optimization found a max power of " + str(rand_val) + " at RL=" + str(x_max_rand[0]))
    print("\t\t-This is almost equivalent to the Thevenin Equivalent resistance of 20/3 Ohms")

    #Problem 4
    print("\nProblem 4: Find the minimum of a function.")
    prob_4_func = lambda x, y: ((x - 3)**2) + ((y - 2)**2)
    prob_4_func_neg = lambda x, y: (-1)* (((x - 3)**2) + ((y - 2)**2))
    prob_4_grad_neg = [ lambda x, y: 6-2*x, lambda x, y: 4-2*y]
    prob_4_hess_neg = [ lambda x, y: -2, lambda x, y: 0, lambda x, y: 0, lambda x, y: -2]
    upper_limit = 4
    lower_limit = 0
    max_error = 1e-2
    [xy_max_rand, rand_val] = optim_random(prob_4_func_neg, [lower_limit, lower_limit],
                                          [upper_limit, upper_limit], max_iter)
    [xy_max_sa, sa_val] = optim_steepest_ascent(prob_4_func_neg, prob_4_grad_neg, 1e-2, max_iter, max_error)
    [xy_max_mdn, mdn_val] = optim_mdnewton(prob_4_func_neg, prob_4_grad_neg, prob_4_hess_neg, 1, max_iter, max_error)
    print("\t Random Optimization found a minimum of " + str(
        prob_4_func(xy_max_rand[0], xy_max_rand[1])) + " at x=" + str(
        xy_max_rand[0]) + " and y=" + str(xy_max_rand[1]))
    print("\t Steepest Ascent Optimization found a minimum of " + str(
        prob_4_func(xy_max_sa[0], xy_max_sa[1])) + " at x=" + str(
        xy_max_sa[0]) + " and y=" + str(xy_max_sa[1]))
    print("\t Multidimensional Newton Optimization found a minimum of " + str(
        prob_4_func(xy_max_mdn[0], xy_max_mdn[1])) + " at x=" + str(
        xy_max_mdn[0]) + " and y=" + str(xy_max_mdn[1]))
    print("\t\t-Seems that the multidimensional newton method gives the most exact result!")

    #Problem 5
    print("\nProblem 5: Minimize another function!")
    prob_5_func = lambda x, y: 4*x + 2*y + (x**2) - 2*(x**4) + 2*x*y - 3*(y**2)
    prob_5_func_neg = lambda x, y: (-1) * (4*x + 2*y + (x**2) - 2*(x**4) + 2*x*y - 3*(y**2))
    prob_5_grad_neg = [lambda x, y: 8*(x**3) - 2*x - 2*(y+2), lambda x, y: -2*(x-3*y+1)]
    prob_5_hess_neg = [lambda x, y: 24*(x**2), lambda x, y: 2, lambda x, y: -2, lambda x, y: 6]
    upper_limit = 100
    lower_limit = -100
    max_error = 1e-2
    try:
        [xy_max_rand, rand_val] = optim_random(prob_5_func_neg, [lower_limit, lower_limit],
                                               [upper_limit, upper_limit], max_iter)
        print("\t Random Optimization found a minimum of " + str(
            prob_5_func(xy_max_rand[0], xy_max_rand[1])) + " at x=" + str(
            xy_max_rand[0]) + " and y=" + str(xy_max_rand[1]))
    except OverflowError:
        print("\t Random Optimization found no minimum!")
    try:
        [xy_max_sa, sa_val] = optim_steepest_ascent(prob_5_func_neg, prob_5_grad_neg, 1e-2, max_iter, max_error)
        print("\t Steepest Ascent Optimization found a minimum of " + str(
            prob_5_func(xy_max_sa[0], xy_max_sa[1])) + " at x=" + str(
            xy_max_sa[0]) + " and y=" + str(xy_max_sa[1]))
    except OverflowError:
        print("\t Steepest Ascent Optimization found no minimum!")
    try:
        [xy_max_mdn, mdn_val] = optim_mdnewton(prob_5_func_neg, prob_5_grad_neg, prob_5_hess_neg, 1, max_iter,
                                               max_error)
        print("\t Multidimensional Newton Optimization found a minimum of " + str(
            prob_5_func(xy_max_mdn[0], xy_max_mdn[1])) + " at x=" + str(
            xy_max_mdn[0]) + " and y=" + str(xy_max_mdn[1]))
    except OverflowError:
        print("\t Multidimensional Newton Optimization found no minimum!")
    print("\t\t-Note that this function has no global minimum though some methods find local minima.")

    # Problem 6
    print("\nProblem 6: Minimize yet another function!!")
    prob_6_func = lambda x, y: -8*x + (x**2) + 12*y + 4*(y**2) - 2*x*y
    prob_6_func_neg = lambda x, y: (-1) * (4 * x + 2 * y + (x ** 2) - 2 * (x ** 4) + 2 * x * y - 3 * (y ** 2))
    prob_6_grad_neg = [lambda x, y: 2*(x-y-4), lambda x, y: -2*x+8*y+12]
    prob_6_hess_neg = [lambda x, y: 2, lambda x, y: -2, lambda x, y: -2, lambda x, y: 8]
    upper_limit = 4
    lower_limit = -1
    max_error = 1e-2
    try:
        [xy_max_rand, rand_val] = optim_random(prob_6_func_neg, [lower_limit, lower_limit],
                                               [upper_limit, upper_limit], max_iter)
        print("\t Random Optimization found a minimum of " + str(
            prob_6_func(xy_max_rand[0], xy_max_rand[1])) + " at x=" + str(
            xy_max_rand[0]) + " and y=" + str(xy_max_rand[1]))
    except OverflowError:
        print("\t Random Optimization found no minimum!")
    try:
        [xy_max_sa, sa_val] = optim_steepest_ascent(prob_6_func_neg, prob_6_grad_neg, 1e-2, max_iter, max_error)
        print("\t Steepest Ascent Optimization found a minimum of " + str(
            prob_6_func(xy_max_sa[0], xy_max_sa[1])) + " at x=" + str(
            xy_max_sa[0]) + " and y=" + str(xy_max_sa[1]))
    except OverflowError:
        print("\t Steepest Ascent Optimization found no minimum!")
    try:
        [xy_max_mdn, mdn_val] = optim_mdnewton(prob_6_func_neg, prob_6_grad_neg, prob_6_hess_neg, 1, max_iter,
                                               max_error)
        print("\t Multidimensional Newton Optimization found a minimum of " + str(
            prob_6_func(xy_max_mdn[0], xy_max_mdn[1])) + " at x=" + str(
            xy_max_mdn[0]) + " and y=" + str(xy_max_mdn[1]))
    except OverflowError:
        print("\t Multidimensional Newton Optimization found no minimum!")
    print("\t\t-The max is very pointed and happens fast so random search has a hard time finding it. Newton wins every time!")