## Cameron Calv ECE T480
# Project 1 Main File
# Find and plot the operating point of a system of pumps and valve by finding the root
# of the equation Head Gain - Head Loss = 0 utilizing the bisection approach and the
# the false_position approach.
import math
from matplotlib import pyplot as plt
from bisection import bisection
from false_position import false_position


if __name__ == '__main__':
    ## Set variables and constants
    H_0_value = 50      # Meters
    A_value = 0
    B_value = -2
    F_0_value = 100     # Meters Cubed per Second

    K_prime_value = 0.2 # Units (unspecified in project outline)
    g_value = 9.8       # Meters per Second Squared


    ## Set up equations for the Head Gain of a Pump
    pump_parameter_c = lambda A, B: 1 - math.e - A - B
    pump_equation = lambda F, H_0, A, B, F_0 : \
        H_0*math.log(math.e + A*(F/F_0) + B*(F/F_0)**2 + pump_parameter_c(A, B)*(F/F_0)**3)
    # Plug in parameters for this project
    head_gain_per_pump = lambda F : pump_equation(F, H_0_value, A_value, B_value, F_0_value)

    ## Set up equations for the Head Loss of the Valve
    valve_equation = lambda V_dot, K_prime, g : K_prime*((V_dot**2)/(2*g))
    # Plug in parameters for this project
    head_loss_per_valve = lambda F : valve_equation(F, K_prime_value, g_value)

    ## Equations for combining head loss/gain in series
    series_head = lambda H1, H2 : H1 + H2

    ## Now for the final functions that will be plotted and rooted
    single_pump_head_gain = lambda F : head_gain_per_pump(F)
    series_pumps_head_gain = lambda F : series_head(head_gain_per_pump(F),head_gain_per_pump(F))
    parallel_pumps_head_gain = lambda F : head_gain_per_pump(F/2)
    single_valve_head_loss = lambda F : head_loss_per_valve(F)

    single_scenario = lambda F : single_pump_head_gain(F) - single_valve_head_loss(F)
    series_scenario = lambda F : series_pumps_head_gain(F) - single_valve_head_loss(F)
    parallel_scenario = lambda F : parallel_pumps_head_gain(F) - single_valve_head_loss(F)


    ## Find intersection points using the bisection method
    bisection_root_single, bisection_results_single = bisection(single_scenario, 100, 0, 1000, 0.001)
    bisection_root_series, bisection_results_series = bisection(series_scenario, 100, 0, 1000, 0.001)
    bisection_root_parallel, bisection_results_parallel = bisection(parallel_scenario, 200, 0, 1000, 0.001)

    ## Find intersection points using the false_position method
    fp_root_single, fp_results_single = false_position(single_scenario, 100, 0, 1000, 0.001)
    fp_root_series, fp_results_series = false_position(series_scenario, 100, 0, 1000, 0.001)
    fp_root_parallel, fp_results_parallel = false_position(parallel_scenario, 200, 0, 1000, 0.001)


    ## Plot all of our curves
    F_values = []
    single_pump_head_values = []
    series_pumps_head_values = []
    parallel_pumps_head_values = []
    single_valve_head_values = []
    for i in range(250):
        F_values.append(i)
        try:
            single_pump_head_values.append(single_pump_head_gain(i))
        except ValueError:
            pass
        try:
            series_pumps_head_values.append(series_pumps_head_gain(i))
        except ValueError:
            pass
        try:
            parallel_pumps_head_values.append(parallel_pumps_head_gain(i))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        try:
            single_valve_head_values.append(single_valve_head_loss(i))
        except ValueError:
            pass

    fig = plt.figure(1)
    # Plot curves and Bisection Roots
    plt.plot(F_values[0 : len(single_pump_head_values)], single_pump_head_values, label="Single Pump")
    plt.plot(F_values[0 : len(series_pumps_head_values)], series_pumps_head_values, label="Two Series Pumps")
    plt.plot(F_values[0 : len(parallel_pumps_head_values)], parallel_pumps_head_values, label="Two Parallel Pumps")
    plt.plot(F_values[0 : len(single_valve_head_values)], single_valve_head_values, label="Valve Head Loss")
    # Plot Intersection Points
    plt.plot(bisection_root_single, single_valve_head_loss(bisection_root_single), 'bo')
    plt.plot(bisection_root_series, single_valve_head_loss(bisection_root_series), 'bo')
    plt.plot(bisection_root_parallel, single_valve_head_loss(bisection_root_parallel), 'bo')
    plt.legend()
    plt.xlabel('Volumetric Flow Rate ($m^3$/s)')
    plt.ylabel('Head (m)')
    plt.axis([0, 200, 0, 100])
    title_line_1 = "Bisection Approach"
    title_line_2 = "Single: "+str(round(bisection_root_single,4))+"($m^3$/s), Head: "+\
                   str(round(single_valve_head_loss(bisection_root_single),4))+" m"
    title_line_3 = "Series: "+str(round(bisection_root_series,4))+"($m^3$/s), Head: "+\
                   str(round(single_valve_head_loss(bisection_root_series),4))+" m"
    title_line_4 = "Parallel: "+str(round(bisection_root_parallel,4))+"($m^3$/s), Head: "+\
                   str(round(single_valve_head_loss(bisection_root_parallel),4))+" m"
    plt.title(title_line_1+"\n"+title_line_2+"\n"+title_line_3+"\n"+title_line_4, fontsize=9)
    plt.subplots_adjust(top=0.82)



    fig = plt.figure(2)
    # Plot curves and Bisection Roots
    plt.plot(F_values[0: len(single_pump_head_values)], single_pump_head_values, label="Single Pump")
    plt.plot(F_values[0: len(series_pumps_head_values)], series_pumps_head_values, label="Two Series Pumps")
    plt.plot(F_values[0: len(parallel_pumps_head_values)], parallel_pumps_head_values, label="Two Parallel Pumps")
    plt.plot(F_values[0: len(single_valve_head_values)], single_valve_head_values, label="Valve Head Loss")
    # Plot Intersection Points
    plt.plot(fp_root_single, single_valve_head_loss(fp_root_single), 'bo')
    plt.plot(fp_root_series, single_valve_head_loss(fp_root_series), 'bo')
    plt.plot(fp_root_parallel, single_valve_head_loss(fp_root_parallel), 'bo')
    plt.legend()
    plt.xlabel('Volumetric Flow Rate ($m^3$/s)')
    plt.ylabel('Head (m)')
    plt.axis([0, 200, 0, 100])
    title_line_1 = "False-Position Approach"
    title_line_2 = "Single: " + str(round(fp_root_single,4)) + "($m^3$/s), Head: " + \
                   str(round(single_valve_head_loss(fp_root_single), 4)) + " m"
    title_line_3 = "Series: " + str(round(fp_root_series,4)) + "($m^3$/s), Head: " + \
                   str(round(single_valve_head_loss(fp_root_series),4)) + " m"
    title_line_4 = "Parallel: " + str(round(fp_root_parallel,4)) + "($m^3$/s), Head: " + \
                   str(round(single_valve_head_loss(fp_root_parallel),4)) + " m"
    plt.title(title_line_1 + "\n" + title_line_2 + "\n" + title_line_3 + "\n" + title_line_4, fontsize=9)
    plt.subplots_adjust(top=0.82)
    plt.show()

