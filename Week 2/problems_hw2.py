## Cameron Calv ECE T480
from bisection import bisection
from false_position import false_position
from fixed_point import fixed_point
from incremental import incremental
from modified_secant import modified_secant
from newton_rhapson import newton_rhapson
from nonlin_fixed_point import nonlin_fixed_point
from nonlin_newton_rhapson import nonlin_newton_rhapson

import math

if __name__ == '__main__':
    max_iter = 200

    #Problem 1
    print("Problem 1: Find real roots of f(x) = -12 - 21x - 18x^2 - 2.75x^3 in the range x: [-10, 10].")
    prob_1_func = lambda x: -12 - 21*x - 18*(x**2) - 2.75*(x**3)
    low_limit = -10
    upper_limit = 10
    stop_criterion = 0.001
    root_brackets = incremental(prob_1_func, low_limit, upper_limit, 1/stop_criterion)
    print("Search within the brackets found by the 'incremental' function!")
    for bracket in root_brackets:
        print("--Within bracket: "+str(bracket))
        output_bisection = bisection(prob_1_func, bracket[1], bracket[0], max_iter, stop_criterion)
        root_b = output_bisection[0]
        print("\t--'Bisection' finds a root at: "+str(root_b))
        output_false_pos = false_position(prob_1_func, bracket[1], bracket[0], max_iter, stop_criterion)
        root_fp = output_false_pos[0]
        print("\t--'False Position' finds a root at: "+str(root_fp))

    #Problem 2
    print("\nProblem 2: The volume of a tank is V (m^3) = pi*h^2*(3*R-h)/3")
    print("Find the height (m) {between 0 and R} to fill a tank of radius 3 (m) so that the volume is 30 (m^3).")
    solve_for_volume = lambda R, h: math.pi*(h**2)*((3*R - h)/(3))
    prob_2_func = lambda V, R, h: solve_for_volume(R, h)-V
    volume = 30 # meters cubed
    radius = 3 # meters
    solve_for_h = lambda h: prob_2_func(volume, radius, h)
    stop_criterion = 0.001
    low_limit = 0
    upper_limit = radius
    root_brackets = incremental(solve_for_h, low_limit, upper_limit, 1/stop_criterion)
    print("Search within the brackets found by the 'incremental' function!")
    for bracket in root_brackets:
        print("--Within bracket: " + str(bracket))
        output_bisection = bisection(solve_for_h, bracket[1], bracket[0], max_iter, stop_criterion)
        root_b = output_bisection[0]
        print("\t--'Bisection' predicts a height of: " + str(root_b) + " meters.")
        output_false_pos = false_position(solve_for_h, bracket[1], bracket[0], max_iter, stop_criterion)
        root_fp = output_false_pos[0]
        print("\t--'False Position' predicts a height of: " + str(root_fp) + " meters.")

    #Problem 3
    print("\nProblem 3: Find the value of t where a current given by i(t)=9*e^(-t)*sin(2*pi*t) equals 3 Amps.")
    solve_for_current = lambda t: 9*math.exp(-t)*math.sin(2*math.pi*t)
    prob_3_func = lambda I, t: solve_for_current(t) - I
    current = 3 # Amps
    solve_for_t = lambda t: prob_3_func(current, t)
    # Plug in derivative for Newton-Rhapson
    solve_for_t_deriv = lambda t: 9*math.exp(-t)*(2*math.pi*math.cos(2*math.pi*t)-math.sin(2*math.pi*t))
    # Perturbation fraction for Modified-Secant
    perturbation = 1*(10**(-6))
    stop_criterion = 0.001
    init_guess = 0.001 # Seconds
    print("Set our initial guess equalt to: "+str(init_guess)+" seconds")
    output_new_rhap = newton_rhapson(solve_for_t, solve_for_t_deriv, init_guess, max_iter, stop_criterion)
    print("--'Newton Rhapson' finds that 't' equals: "+str(output_new_rhap[0]))
    output_mod_sec = modified_secant(solve_for_t, init_guess, perturbation, max_iter, stop_criterion)
    print("--'Modified Secant' finds that 't' equals: " + str(output_mod_sec[0]))
    output_fix_poi = fixed_point(solve_for_t, init_guess, max_iter, stop_criterion)
    print("--'Fixed Point' finds that 't' equals: " + str(output_fix_poi[0]))
    output_fix_poi = fixed_point(solve_for_t, 0.01, max_iter, stop_criterion)
    print("----'Fixed Point' for initial guess 0.01: " + str(output_fix_poi[0]))
    output_fix_poi = fixed_point(solve_for_t, 0.0002, max_iter, stop_criterion)
    print("----'Fixed Point' for initial guess 0.0002: " + str(output_fix_poi[0]))
    print("Note that for this problem, the initial guess either diverges or converges the approximations.")

    #Problem 4
    print("\nProblem 4: Find the value of N given the relationships for resistivity of silicon.")
    solve_for_mu = lambda mu_not, T, T_not : mu_not*((T/T_not)**(-2.42))
    solve_for_little_n = lambda N, ni : (1/2)*(N+math.sqrt(N**2+4*(ni**2)))
    solve_for_rho = lambda q, n, mu : 1/(q*n*mu)
    q_val = 1.6*(10**(-19))
    ni_val = 6.21*(10**9)
    T_val = 1000
    T_not_val = 300
    mu_not_val = 1300
    rho_val = 6*(10**6)
    prob_4_func = lambda N : solve_for_rho(q_val, solve_for_little_n(N, ni_val), solve_for_mu(mu_not_val, T_val, T_not_val)) - rho_val
    stop_criterion = 0.001
    init_guess =  1
    perturbation = 1 * (10 ** (-6))
    output_bisection = bisection(prob_4_func, 1*(10**15), 0, max_iter, stop_criterion)
    print("\t--'Bisection' predicts a doping density of: " + str(output_bisection[0]) + " inverse centimeters cubed.")
    output_mod_sec = modified_secant(prob_4_func, 1, perturbation, max_iter, stop_criterion)
    print("\t--'Modified Secant' predicts a doping density of: " + str(output_mod_sec[0]) + " inverse centimeters cubed.")

    #Problem 5
    print("\nProblem 5: Solve for distance from a charged ring that gives a force of 1 Newton. ")
    solve_for_force = lambda x, q, Q, e_not, radius: (q*Q*x)/(4*math.pi*e_not*((x**2 + radius**2)**(3/2)))
    q_value = 2*(10**(-5))
    Q_value = q_value
    e_not_value = 8.85*(10**(-12))
    radius_value = 0.9
    force_value = 1
    prob_5_func = lambda x: solve_for_force(x, q_value, Q_value, e_not_value, radius_value) - force_value
    # Plug in derivative for Newton-Rhapson
    prob_5_deriv = lambda x: ((q_value*Q_value)/(4*math.pi*e_not_value))*(radius_value**2-2*(x**2))/(((radius_value**2) + (x**2))**(5/2))
    # Perturbation fraction for Modified-Secant
    perturbation = 1 * (10 ** (-6))
    stop_criterion = 0.001
    init_guess = 0.01  # Meters
    print("Set our initial guess equal to: " + str(init_guess) + " meters")
    output_new_rhap = newton_rhapson(prob_5_func, prob_5_deriv, init_guess, max_iter, stop_criterion)
    print("--'Newton Rhapson' finds that 'x' equals: " + str(output_new_rhap[0]))
    output_mod_sec = modified_secant(prob_5_func, init_guess, perturbation, max_iter, stop_criterion)
    print("--'Modified Secant' finds that 'x' equals: " + str(output_mod_sec[0]))
    output_fix_poi = fixed_point(prob_5_func, 0.22, max_iter, stop_criterion)
    print("--'Fixed Point' finds that 'x' equals: " + str(output_fix_poi[0]))

    #Problem 6
    print("\nProblem 6: Solve for the impedance of a parallel RLC circuit.")
    solve_for_one_over_z = lambda omega, R, C, L : math.sqrt(1/(R**2)+(omega*C-1/(omega*L))**2)
    R_value = 225
    C_value = 0.6 * (10**(-6))
    L_value = 0.5
    Z_value = 75
    prob_6_func = lambda omega: (1/(solve_for_one_over_z(omega, R_value, C_value, L_value))) - Z_value
    output_bisection = bisection(prob_6_func, 10*(10**2), 1, max_iter, stop_criterion)
    root_b = output_bisection[0]
    print("--'Bisection' finds the angular frequency to be: " + str(root_b))
    output_false_pos = false_position(prob_6_func, 10*(10**2), 1, max_iter, stop_criterion)
    root_fp = output_false_pos[0]
    print("--'False Position' finds the angular frequency to be: " + str(root_fp))

    #Problem 7
    print("\nProblem 7: Solve for the frequency of a series RLC circuit.")
    print("Note the problem asks for 1kHz, but this is not possible, instead solving for 10 Hz")
    solve_for_omega = lambda R, C, L: math.sqrt(1/(L*C) - (R/(2*L))**2)
    C_value = 1.0 * (10 ** (-4))
    L_value = 5
    omega_value = 10
    prob_7_func = lambda R: solve_for_omega(R, C_value, L_value) - omega_value
    #For Newton Rhapson
    prob_7_deriv = lambda R: (-R)/(4*(L_value**2)*math.sqrt((1/(C_value*L_value))-((R**2)/(4*(L_value**2)))))
    output_bisection = bisection(prob_7_func, 447, 0, max_iter, stop_criterion)
    root_b = output_bisection[0]
    print("--'Bisection' finds the resistance to be: " + str(root_b))
    output_false_pos = false_position(prob_7_func, 447, 0, max_iter, stop_criterion)
    root_fp = output_false_pos[0]
    print("--'False Position' finds the resistance to be: " + str(root_fp))
    output_new_rhap = newton_rhapson(prob_7_func, prob_7_deriv, 447, max_iter, stop_criterion)
    print("--'Newton Rhapson' finds the resistance to be " + str(output_new_rhap[0]))

    #Problem 8
    print("\nProblem 8: Solve the system of equations! First with some rearranging.")
    func_1 = lambda x, y: -(x**2)+x+0.75 - y
    func_2 = lambda x, y: y + 5*x*y - x**2
    x_equals = lambda x, y: (x**2 - y)/(5*y)
    y_equals = lambda x, y: -(x**2) + x + 0.75
    output_fp = nonlin_fixed_point([x_equals, y_equals], [1.2, 1.2], max_iter, stop_criterion)
    roots_fp = output_fp[0]
    print("--'Nonlinear Fixed Point' finds the roots to be: " + str(roots_fp[0]) + " and "+str(roots_fp[1]))
    y_partial_deriv_x = lambda x, y: 5*y - 2*x
    y_partial_deriv_y = lambda x, y: 1 + 5*x
    x_partial_deriv_x = lambda x, y: -2*x + 1
    x_partial_deriv_y = lambda x, y: -1
    system_derivatives = [[x_partial_deriv_x, x_partial_deriv_y], [y_partial_deriv_x, y_partial_deriv_y]]
    output_nr = nonlin_newton_rhapson([func_1, func_2], system_derivatives, [1.2, 1.2], max_iter, stop_criterion/10)
    roots_nr = output_nr[0]
    print("--'Nonlinear Newton Rhapson' finds the roots to be: " + str(roots_nr[0]) + " and " + str(roots_nr[1]))
    print("Looks like they find different roots!")

    #Problem 9
    print("\nProblem 9: Solve another system!")
    x_equals = lambda x, y: (x-4)**2 + (y-4)**2 - 5
    y_equals = lambda x, y: x**2 + y**2 - 16
    system = [x_equals, y_equals]

    x_partial_deriv_x = lambda x, y: 2*(x-4)
    x_partial_deriv_y = lambda x, y: 2*(y-4)
    y_partial_deriv_x = lambda x, y: 2*x
    y_partial_deriv_y = lambda x, y: 2*y
    system_derivatives = [[x_partial_deriv_x, x_partial_deriv_y], [y_partial_deriv_x, y_partial_deriv_y]]
    output_nr = nonlin_newton_rhapson(system, system_derivatives, [2.1, 2.2], max_iter, stop_criterion / 10)
    roots_nr = output_nr[0]
    print("--'Nonlinear Newton Rhapson' finds the roots to be: " + str(roots_nr[0]) + " and " + str(roots_nr[1]))


