## Cameron Calv ECE T480
from cf_linear_lsr import cf_linear_lsr
from cf_nonlinfit import cf_nonlinfit
from cf_polyfit import cf_polyfit
from matplotlib import pyplot as plt
import math

if __name__ == '__main__':
    #Problem 1
    print("Problem 1: Fourth-order polyfit to find value at specified point.")
    list_1_prob_1 = [0.25, 0.75, 1.25, 1.5, 2.0]
    list_2_prob_1 = [-0.45, -0.6, 0., 1.88, 6.0]
    [coefs_prob_1, corr_prob_1] = cf_polyfit(list_1_prob_1, list_2_prob_1, 4)
    fit_prob_1 = list()
    for x in list_1_prob_1:
        total = 0
        expo = 0
        for coef in coefs_prob_1:
            total += coef * (x ** expo)
            expo += 1
        fit_prob_1.append(total)
    val_prob_1 = 0
    expo = 0
    for coef in coefs_prob_1:
        val_prob_1 += coef * (1.15 ** expo)
        expo += 1
    plt.figure(1)
    plt.plot(list_1_prob_1, list_2_prob_1, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_1, fit_prob_1, label="Fitted Curve", color='orange')
    plt.legend()
    plt.title("Plot of Current and Voltage for Problem 1")
    plt.xlabel("Current (Amps)")
    plt.ylabel("Voltage (Volts)")
    print("Polyfit gives coefficient values of \n\t"+str(coefs_prob_1)+"\nand a correlation coefficient of \n\t"+str(corr_prob_1))
    print("Interpolating from this curve, the value of the voltage at \n\ti = 1.15 Amps \nis V = \n\t"+str(val_prob_1)+" Volts")

    #Problem 2
    print("\nProblem 2: Estimate L based on the voltage and change in current data.")
    list_1_prob_2 = [1, 2, 4, 6, 8, 10]
    list_2_prob_2 = [5.5, 12.5, 16.5, 32, 38, 49]
    [[coef_1_prob_2, coef_2_prob_2], corr_prob_2] = cf_linear_lsr(list_1_prob_2, list_2_prob_2, 'linear')
    fit_prob_2 = []
    for val in list_1_prob_2:
        fit_prob_2.append(coef_1_prob_2 + coef_2_prob_2 * val)
    plt.figure(2)
    plt.plot(list_1_prob_2, list_2_prob_2, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_2, fit_prob_2, label="Fitted Curve", color='orange')
    plt.legend()
    plt.title("Plot of Change in Current and Voltage for Problem 2, \nL ~ "+str(coef_2_prob_2)+" H")
    plt.xlabel("Change in Current (Amps/Sec)")
    plt.ylabel("Inductor Voltage (Volts)")
    print("Linear regression gives an intercept value of \n\t"+str(coef_1_prob_2)+" \nand an inductance (slope) of \n\t"+str(coef_2_prob_2)+" H")
    print("*Note that the inductance is the steady-state voltage of the inductor since the change in current is zero at DC.")

    #Problem 3
    print("\nProblem 3: Predict population of a small community.")
    list_1_prob_3 = [0, 5, 10, 15, 20]
    list_2_prob_3 = [100, 200, 450, 950, 2000]
    [[coef_1_prob_3_expo, coef_2_prob_3_expo], corr_prob_3_expo] = cf_linear_lsr(list_1_prob_3, list_2_prob_3, 'exponential')
    [[coef_1_prob_3_line, coef_2_prob_3_line], corr_prob_3_line] = cf_linear_lsr(list_1_prob_3, list_2_prob_3, 'linear')
    fit_prob_3_expo = []
    for val in list_1_prob_3:
        fit_prob_3_expo.append(coef_1_prob_3_expo * math.exp(coef_2_prob_3_expo * val))
    fit_prob_3_expo.append(coef_1_prob_3_expo * math.exp(coef_2_prob_3_expo * 25))
    fit_prob_3_line = []
    for val in list_1_prob_3:
        fit_prob_3_line.append(coef_1_prob_3_line + coef_2_prob_3_line * val)
    fit_prob_3_line.append(coef_1_prob_3_line + coef_2_prob_3_line * 25)
    plt.figure(3)
    plt.plot(list_1_prob_3, list_2_prob_3, label="Plotted Curve", color='blue', linewidth=3)
    list_1_prob_3.append(25)
    plt.plot(list_1_prob_3, fit_prob_3_expo, label="Exponential Fit", color='purple')
    plt.plot(list_1_prob_3, fit_prob_3_line, label="Linear Fit", color='pink')
    plt.plot(list_1_prob_3[-1], fit_prob_3_expo[-1], 'o', label="Predicted Pop = "+str(round(fit_prob_3_expo[-1])), color='purple', marker='o')
    plt.plot(list_1_prob_3[-1], fit_prob_3_line[-1], 'o', label="Predicted Pop = "+str(round(fit_prob_3_line[-1])), color='pink', marker='o')
    plt.legend()
    plt.title("Plot of Population Growth and 5 Year Prediction for Problem 3")
    plt.xlabel("Time (Years)")
    plt.ylabel("Population (People)")
    print("Linear regression predicts a population of about \n\t"+str(round(fit_prob_3_line[-1]))+" People")
    print("Exponential regression predicts a population of about \n\t"+str(round(fit_prob_3_expo[-1]))+" People")

    #Problem 4
    print("\nProblem 4: Fit a straight line to a data set and determine the error.")
    list_1_prob_4 = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
    list_2_prob_4 = [5, 6, 7, 6, 9, 8, 6, 10, 12, 12]
    [[coef_1_prob_4, coef_2_prob_4], corr_prob_4] = cf_linear_lsr(list_1_prob_4, list_2_prob_4, 'linear')
    fit_prob_4 = []
    for val in list_1_prob_4:
        fit_prob_4.append(coef_1_prob_4 + coef_2_prob_4 * val)
    std_err_prob_4 = 0
    for idx in range(len(list_1_prob_4)):
        std_err_prob_4 += (list_2_prob_4[idx] - fit_prob_4[idx])**2
    std_err_prob_4 = math.sqrt(std_err_prob_4/(len(list_1_prob_4)-2))
    plt.figure(4)
    plt.plot(list_1_prob_4, list_2_prob_4, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_4, fit_prob_4, label="Fitted Curve", color='orange')
    plt.legend()
    plt.title("Plot of Data and Linear Fit for Problem 4")
    plt.xlabel("X")
    plt.ylabel("Y")
    print("Linear regression computes a slope of \n\t"+str(coef_2_prob_4)+"\nand an intercept of \n\t"+str(coef_1_prob_4))
    print("a correlation coefficient of\n\t"+str(corr_prob_4)+"\nand a standard error of the estimate of\n\t"+str(std_err_prob_4))

    #Problem 5
    print("\nProblem 5: Plot some fits for some data!")
    list_1_prob_5 = [0.75, 2, 3, 4, 6, 8, 8.5]
    list_2_prob_5 = [1.2, 1.95, 2, 2.4, 2.4, 2.7, 2.6]
    [[coef_1_prob_5_sgr, coef_2_prob_5_sgr], corr_prob_5_sgr] = cf_linear_lsr(list_1_prob_5, list_2_prob_5,'saturation-growth-rate')
    [[coef_1_prob_5_pow, coef_2_prob_5_pow], corr_prob_5_pow] = cf_linear_lsr(list_1_prob_5, list_2_prob_5,'power')
    [coefs_prob_5_poly, corr_prob_5_poly] = cf_polyfit(list_1_prob_5, list_2_prob_5, 2)
    fit_prob_5_sgr = []
    for val in list_1_prob_5:
        fit_prob_5_sgr.append(coef_1_prob_5_sgr * (val / (coef_2_prob_5_sgr + val)))
    fit_prob_5_pow = []
    for val in list_1_prob_5:
        fit_prob_5_pow.append(coef_1_prob_5_pow * (val ** coef_2_prob_5_pow))
    fit_prob_5_poly = []
    for x in list_1_prob_5:
        total = 0
        expo = 0
        for coef in coefs_prob_5_poly:
            total += coef * (x ** expo)
            expo += 1
        fit_prob_5_poly.append(total)
    plt.figure(5)
    plt.plot(list_1_prob_5, list_2_prob_5, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_5, fit_prob_5_sgr, label="Saturated-Growth Fit", color='purple')
    plt.plot(list_1_prob_5, fit_prob_5_pow, label="Power Fit", color='pink')
    plt.plot(list_1_prob_5, fit_prob_5_poly, label="Parabola Fit", color='magenta')
    plt.text(4.5, 2.0, "a) Sat-Gro: "+str(round(coef_1_prob_5_sgr,3))+"*(X / ("+str(round(coef_2_prob_5_sgr,3))+"+X))")
    plt.text(4.5, 1.9, "b) Power: "+str(round(coef_1_prob_5_pow,3))+"*(X^"+str(round(coef_2_prob_5_pow,3))+")")
    plt.text(4.5, 1.8, "c) Parabola: "+str(round(coefs_prob_5_poly[0],3))+"+"+str(round(coefs_prob_5_poly[1],3))+"X"+str(round(coefs_prob_5_poly[2],3))+"X^2")
    plt.legend()
    plt.title("Plot of Data Various Fits for Problem 5")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Problem 6
    print("\nProblem 6: Fit the data with a power model and interpolate.")
    list_1_prob_6 = [2.5, 3.5, 5, 6, 7.5, 10, 12.5, 15, 17.5, 20]
    list_2_prob_6 = [13, 11, 8.5, 8.2, 7, 6.2, 5.2, 4.8, 4.6, 4.3]
    [[coef_1_prob_6, coef_2_prob_6], corr_prob_6_pow] = cf_linear_lsr(list_1_prob_6, list_2_prob_6, 'power')
    fit_prob_6 = []
    for val in list_1_prob_6:
        fit_prob_6.append(coef_1_prob_6 * (val ** coef_2_prob_6))
    plt.figure(6)
    plt.plot(list_1_prob_6, list_2_prob_6, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_6, fit_prob_6, label="Fitted Curve", color='orange')
    plt.legend()
    plt.title("Plot of Data and Power Fit for Problem 6")
    plt.xlabel("X")
    plt.ylabel("Y")
    print("Power regression says that at \n\tx = 9\nthe value of the function should be\n\t"+str(coef_1_prob_6 * (9 ** coef_2_prob_6)))

    # Problem 7
    print("\nProblem 7: Plot some data with an exponential fit")
    list_1_prob_7 = [0.4, 0.8, 1.2, 1.6, 2, 2.3]
    list_2_prob_7 = [800, 975, 1500, 1950, 2900, 3600]
    [[coef_1_prob_7, coef_2_prob_7], corr_prob_7] = cf_linear_lsr(list_1_prob_7, list_2_prob_7, 'exponential')
    fit_prob_7 = []
    for val in list_1_prob_7:
        fit_prob_7.append(coef_1_prob_7 * math.exp(coef_2_prob_7 * val))
    plt.figure(7)
    plt.plot(list_1_prob_7, list_2_prob_7, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_7, fit_prob_7, label="Fitted Curve", color='orange')
    plt.legend()
    plt.title("Plot of Data and Exponential Fit for Problem 7")
    plt.xlabel("t")
    plt.ylabel("p")

    # Problem 8
    print("\nProblem 8: Plot more data with various curves")
    list_1_prob_8 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    list_2_prob_8 = [17,24, 31, 33, 37, 37, 40, 40, 42, 41]
    [[coef_1_prob_8_line, coef_2_prob_8_line], corr_prob_8_line] = cf_linear_lsr(list_1_prob_8, list_2_prob_8, 'linear')
    [[coef_1_prob_8_pow, coef_2_prob_8_pow], corr_prob_8_pow] = cf_linear_lsr(list_1_prob_8, list_2_prob_8, 'power')
    [[coef_1_prob_8_sgr, coef_2_prob_8_sgr], corr_prob_8_sgr] = cf_linear_lsr(list_1_prob_8, list_2_prob_8, 'saturation-growth-rate')
    [coefs_prob_8_poly, corr_prob_8_poly] = cf_polyfit(list_1_prob_8, list_2_prob_8, 2)
    fit_prob_8_line = []
    for val in list_1_prob_8:
        fit_prob_8_line.append(coef_1_prob_8_line + coef_2_prob_8_line * val)
    fit_prob_8_pow = []
    for val in list_1_prob_8:
        fit_prob_8_pow.append(coef_1_prob_8_pow * (val ** coef_2_prob_8_pow))
    fit_prob_8_sgr = []
    for val in list_1_prob_8:
        fit_prob_8_sgr.append(coef_1_prob_8_sgr * (val / (coef_2_prob_8_sgr + val)))
    fit_prob_8_poly = []
    for x in list_1_prob_8:
        total = 0
        expo = 0
        for coef in coefs_prob_8_poly:
            total += coef * (x ** expo)
            expo += 1
        fit_prob_8_poly.append(total)
    plt.figure(8)
    plt.plot(list_1_prob_8, list_2_prob_8, label="Plotted Curve", color='blue', linewidth=3)
    plt.plot(list_1_prob_8, fit_prob_8_line, label="Linear Fit", color='purple')
    plt.plot(list_1_prob_8, fit_prob_8_pow, label="Power Fit", color='pink')
    plt.plot(list_1_prob_8, fit_prob_8_sgr, label="Saturation-Growth Fit", color='magenta')
    plt.plot(list_1_prob_8, fit_prob_8_poly, label="Parabola Fit", color='red')
    plt.text(25, 27.5, "a) Linear Correlation: "+str(round(corr_prob_8_line, 3)))
    plt.text(25, 27.5-1.5, "b) Power Correlation: "+str(round(corr_prob_8_pow, 3)))
    plt.text(25, 27.5-1.5*2, "c) Sat-Grow Correlation: "+str(round(corr_prob_8_sgr, 3)))
    plt.text(25, 27.5-1.5*3, "d) Parabola Correlation: "+str(round(corr_prob_8_poly, 3)))
    plt.legend()
    plt.title("Plot of Data Various Fits for Problem 8")
    plt.xlabel("X")
    plt.ylabel("Y")
    print("The curve with the highest correlation coefficient is Saturation-Growth, therefore it is the best fit.")

    # Problem 9
    print("\nProblem 9: ")

    plt.show()
