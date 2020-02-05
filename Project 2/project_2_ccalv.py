## Cameron Calv ECE T480
# Project 2 Main File
# Find and plot various characteristics of a parallel pipe
# system utilizing root finding functions to determine some of these parameters
import math
from newton_rhapson import newton_rhapson
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # #==Establishing our Equations==# #
    # 𝑚̇ = 𝜌Av
    # Where 𝜌 = density(kg / m3);
    # 𝐴 = cross sectional area of pipe(m2)
    # 𝑣 = average speed of fluid in pipe(m / s)
    mass_flow_rate = lambda p, A, v: p*A*v

    # 𝑅e = 𝜌vD/𝜇
    # Where
    # 𝜌 = density(kg / m3)
    # 𝑣 = average speed of fluid in pipe(m / s)
    # 𝐷 = Hydraulic diameter of pipe(for circular pipes, it’s just the pipe diameter) (m / s)
    # 𝜇 = Fluid dynamic viscosity(Pa - s)
    reynolds_number = lambda p, v, D, mu: (p*v*D)/mu

    # ℎ𝐿 = 𝑓*(𝐿/𝐷)*(v^2/(2g))
    # Where
    # 𝐿 = pipe length(m)
    # 𝑣 = average speed of fluid in pipe(m / s)
    # 𝐷 = Hydraulic diameter of pipe( for circular pipes, it’s just the pipe diameter) (m / s)
    # 𝑔 = gravitational acceleration constant(m / s^2)
    # 𝑓 = Darcy friction factor(unitless)
    head_loss = lambda f, L, D, v, g: f*(L/D)*((v**2)/(2*g))

    colebrook_equation = lambda f, eps, D, Re: (1/math.sqrt(f)) + 2*math.log10((eps/D)/3.7 + (2.51/(Re*math.sqrt(f))))
    colebrook_simplified = lambda f, A, B: (1/math.sqrt(f)) + 2*math.log10(A + B/math.sqrt(f))
    colebrook_simple_deriv = lambda f, A, B: (-B)/((math.sqrt(f)**3)*math.log(10)*(A+(B/math.sqrt(f)))) - (1/(2*(math.sqrt(f)**3)))

    # #==Establishing our Specifics==# #
    # #System# #
    gravity = 9.812
    mass_flow_rate_total = 5
    max_iter = 1000
    min_error = 0.00001
    A_calc = lambda eps, D: (eps / D) / 3.7
    B_calc = lambda Re: 2.51 / Re

    # #Pipe 1# #
    L_pipe_1 = 10
    D_pipe_1 = 0.2
    eps_pipe_1 = 0.25e-3
    p_pipe_1 = 1000
    mu_pipe_1 = 0.001
    mass_flow_rate_pipe_1 = lambda v: p_pipe_1*(math.pi*(D_pipe_1/2)**2)*v

    # #Pipe 2# #
    L_pipe_2 = L_pipe_1
    D_pipe_2 = [] # <== Varies
    D_2_max = 0.5
    D_2_min = 0.03
    D_2_step = 0.01
    for i in range(int(round((D_2_max - D_2_min)/D_2_step))):
        D_pipe_2.append(D_2_min + i * D_2_step)
    D_pipe_2.append(D_2_max)
    eps_pipe_2 = eps_pipe_1
    p_pipe_2 = p_pipe_1
    mu_pipe_2 = mu_pipe_1
    mass_flow_rate_pipe_2 = lambda D, v: p_pipe_2 * (math.pi * (D / 2) ** 2) * v

    # #==Plotting for the Project==# #
    # #Set up our Y_value Lists# #
    mass_flow_rates_pipe_1 = []
    mass_flow_rates_pipe_2 = []

    friction_factors_pipe_1 = []
    friction_factors_pipe_2 = []

    reynolds_numbers_pipe_1 = []
    reynolds_numbers_pipe_2 = []

    head_losses_pipe_1 = []
    head_losses_pipe_2 = []

    # To calculate mass flow rate, we begin with an estimate for pipe 1 and determine the velocity.
    # Then we find the head loss and ensure that they are the same or the difference is under some tolerance
    for diameter_pipe_2 in D_pipe_2:
        # print("Testing for pipe 2 diameter: "+str(diameter_pipe_2)+" m")
        velocity_pipe_1 = lambda mass_flow_rate: (4*mass_flow_rate)/(p_pipe_1*math.pi*(D_pipe_1**2))
        velocity_pipe_2 = lambda mass_flow_rate: (4*mass_flow_rate)/(p_pipe_2*math.pi*(diameter_pipe_2**2))
        head_loss_pipe_1 = lambda f, v: f*(L_pipe_1/D_pipe_1)*((v**2)/(2*gravity))
        head_loss_pipe_2 = lambda f, v: f*(L_pipe_2/diameter_pipe_2)*((v**2)/(2*gravity))

        hL_pipe_1 = 1
        hL_pipe_2 = 0
        head_loss_tolerance = 1e-6
        flow_rate_step = 0.01
        flow_rate_1 = 0
        previous_difference = 100000000000
        difference = previous_difference - 1
        tracking_differences = []
        while (abs(hL_pipe_1 - hL_pipe_2) > head_loss_tolerance and flow_rate_1 < mass_flow_rate_total and difference < previous_difference):
            previous_difference = difference
            flow_rate_1 += flow_rate_step

            v_1 = velocity_pipe_1(flow_rate_1)
            v_2 = velocity_pipe_2(mass_flow_rate_total - flow_rate_1)
            A_pipe_1 = A_calc(eps_pipe_1, D_pipe_1)
            Re_pipe_1 = reynolds_number(p_pipe_1, v_1, D_pipe_1, mu_pipe_1)
            B_pipe_1 = B_calc(Re_pipe_1)
            A_pipe_2 = A_calc(eps_pipe_2, diameter_pipe_2)
            Re_pipe_2 = reynolds_number(p_pipe_2, v_2, diameter_pipe_2, mu_pipe_2)
            B_pipe_2 = B_calc(Re_pipe_2)

            # Determine friction factor for pipe 1 and 2
            if (Re_pipe_1 < 2300):
                f_pipe_1 = 64 / Re_pipe_1
            elif (Re_pipe_1 >= 2300 and Re_pipe_1 < 4000):
                # Linear interpolation
                f_low_1 = 64/2300
                solve_for_f_pipe_1 = lambda f: colebrook_simplified(f, A_pipe_1, B_calc(4000))
                solve_for_f_pipe_1_deriv = lambda f: colebrook_simple_deriv(f, A_pipe_1, B_calc(4000))
                output_pipe_1 = newton_rhapson(solve_for_f_pipe_1, solve_for_f_pipe_1_deriv, .03, max_iter, min_error)
                f_high_1 = output_pipe_1[0]
                f_pipe_1 = (Re_pipe_1 - 2300) * (f_high_1 - f_low_1) / (4000 - 2300) + f_low_1
            else:
                solve_for_f_pipe_1 = lambda f: colebrook_simplified(f, A_pipe_1, B_pipe_1)
                solve_for_f_pipe_1_deriv = lambda f: colebrook_simple_deriv(f, A_pipe_1, B_pipe_1)
                output_pipe_1 = newton_rhapson(solve_for_f_pipe_1, solve_for_f_pipe_1_deriv, .03, max_iter, min_error)
                f_pipe_1 = output_pipe_1[0]

            if (Re_pipe_2 < 2300):
                f_pipe_2 = 64/Re_pipe_2
            elif (Re_pipe_2 >= 2300 and Re_pipe_2 < 4000):
                # Linear interpolation
                f_low_2 = 64/2300
                solve_for_f_pipe_2 = lambda f: colebrook_simplified(f, A_pipe_2, B_calc(4000))
                solve_for_f_pipe_2_deriv = lambda f: colebrook_simple_deriv(f, A_pipe_2, B_calc(4000))
                output_pipe_2 = newton_rhapson(solve_for_f_pipe_2, solve_for_f_pipe_2_deriv, .03, max_iter, min_error)
                f_high_2 = output_pipe_2[0]
                f_pipe_2 = (Re_pipe_2 - 2300) * (f_high_2 - f_low_2) / (4000 - 2300) + f_low_2
            else:
                solve_for_f_pipe_2 = lambda f: colebrook_simplified(f, A_pipe_2, B_pipe_2)
                solve_for_f_pipe_2_deriv = lambda f: colebrook_simple_deriv(f, A_pipe_2, B_pipe_2)
                output_pipe_2 = newton_rhapson(solve_for_f_pipe_2, solve_for_f_pipe_2_deriv, .03, max_iter, min_error)
                f_pipe_2 = output_pipe_2[0]
            hL_pipe_1 = head_loss_pipe_1(f_pipe_1, v_1)
            hL_pipe_2 = head_loss_pipe_2(f_pipe_2, v_2)
            # print("\tComparing head loss: "+str(hL_pipe_1)+" & "+str(hL_pipe_2))
            difference = abs(hL_pipe_1 - hL_pipe_2)
            # print("\t\tDifference: " + str(difference))
            tracking_differences.append(difference)
        mass_flow_rates_pipe_1.append(flow_rate_1)
        mass_flow_rates_pipe_2.append(mass_flow_rate_total - flow_rate_1)

        friction_factors_pipe_1.append(f_pipe_1)
        friction_factors_pipe_2.append(f_pipe_2)

        reynolds_numbers_pipe_1.append(Re_pipe_1)
        reynolds_numbers_pipe_2.append(Re_pipe_2)

        head_losses_pipe_1.append(hL_pipe_1)
        head_losses_pipe_2.append(hL_pipe_2)

    fig = plt.figure(1)
    # Plot curve of mass flow rate
    plt.plot(D_pipe_2, mass_flow_rates_pipe_1, label="Pump 1", color='blue')
    plt.plot(D_pipe_2, mass_flow_rates_pipe_2, label="Pump 2", color='red')
    plt.legend()
    plt.xlabel('Diameter of Pipe 2 (m)')
    plt.ylabel('Mass Flow Rate (kg/s)')
    # plt.axis([0.0, 0.5, 0, 0.00175])
    plt.grid(True, which="both")
    plt.title("a) Mass Flow Rate Plot Project 2 Calv")

    fig = plt.figure(2)
    # Plot curve of the friction factor
    plt.plot(D_pipe_2, friction_factors_pipe_1, label="Pump 1", color='blue')
    plt.plot(D_pipe_2, friction_factors_pipe_2, label="Pump 2", color='red')
    plt.legend()
    plt.xlabel('Diameter of Pipe 2 (m)')
    plt.ylabel('Darcy Friction Factor')
    # plt.axis([0.0, 0.5, 0, 0.00175])
    plt.grid(True, which="both")
    plt.title("b) Friction Factor Plot Project 2 Calv")

    fig = plt.figure(3)
    # Plot curve of the Reynold's numbers
    plt.plot(D_pipe_2, reynolds_numbers_pipe_1, label="Pump 1", color='blue')
    plt.plot(D_pipe_2, reynolds_numbers_pipe_2, label="Pump 2", color='red')
    plt.legend()
    plt.xlabel('Diameter of Pipe 2 (m)')
    plt.ylabel('Reynold\'s Number Value')
    # plt.axis([0.0, 0.5, 0, 0.00175])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.grid(True, which="both")
    plt.title("c) Reynold's Number Plot Project 2 Calv")

    fig = plt.figure(4)
    # Plot curve of head loss
    plt.plot(D_pipe_2, head_losses_pipe_1, label="Pump 1", color='blue')
    plt.plot(D_pipe_2, head_losses_pipe_2, label="Pump 2", color='red')
    plt.legend()
    plt.xlabel('Diameter of Pipe 2 (m)')
    plt.ylabel('Head Loss (m)')
    plt.axis([0.0, 0.5, 0, 0.00175])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.grid(True, which="both")
    plt.title("d) Head Loss Plot Project 2 Calv")


    fig = plt.figure(5)
    plt.semilogx(reynolds_numbers_pipe_1, friction_factors_pipe_1, 's', label="Pump 1", color='blue', marker='s')
    plt.semilogx(reynolds_numbers_pipe_2, friction_factors_pipe_2, 's', label="Pump 2", color='red', marker='s')
    plt.legend()
    plt.xlabel('Reynold\'s Number')
    plt.ylabel('Friction Factor')
    # plt.axis([0.0, 0.5, 0, 0.00175])
    plt.grid(True, which="both")
    plt.title("e) Friction Factor vs Reynold's Number Plot Project 2 Calv")
    plt.show()






