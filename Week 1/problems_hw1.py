## Cameron Calv ECE T480
from machine_epsilon import machine_epsilon
from fact import fact
from deriv1 import deriv1
from deriv2 import deriv2
from math import pi
from math import cos
from matplotlib import pyplot as plt

if __name__ == '__main__':
    #Problem 1: What is my machine epsilon?
    print("Problem 1: What is my machine epsilon?")
    print("My machine epsilon is "+str(machine_epsilon())+"\n")

    #Problem 2
    print("Problem 2: Calculate f(n) = summation(1/(i^4) for i=1 to n. n = 10000")
    actual = (pi * pi * pi * pi) / (90)
    print("Actual : " + str(actual))
    forward_sum = 0
    for i in range(1, 10000):
        forward_sum = forward_sum + (1/(i*i*i*i))
    print("Forward Approx: "+str(forward_sum))
    print("Relative Accuracy: "+str((forward_sum/actual)*100)+"%")
    backward_sum = 0
    for i in reversed(range(1, 10000)):
        backward_sum = backward_sum + (1/(i*i*i*i))
    print("Backward Approx: "+str(backward_sum))
    print("Relative Accuracy: "+str((backward_sum/actual)*100)+"%\n")

    #Problem 3
    print("Problem 3: Estimate e^(-5) using series expansion and inverted series expansion")
    actual = 6.737947*(10**(-3))
    print("Actual : "+str(actual))
    num_terms = 20
    series_approx = 0
    for i in range(num_terms):
        series_approx = series_approx + ((-1)**(i))*(((5)**(i))/fact(i))
    print("Series Approx: "+str(series_approx))
    print("Relative Accuracy: "+str((series_approx/actual)*100)+"%")
    inv_series_approx = 0
    for i in range(num_terms):
        inv_series_approx = inv_series_approx + (((5)**(i))/fact(i))
    inv_series_approx = inv_series_approx**(-1)
    print("Inverted Series Approx: "+str(inv_series_approx))
    print("Relative Accuracy: "+str((inv_series_approx/actual)*100)+"%\n")

    #Problem 4
    print("Problem 4: Add terms to the approximation of cos(pi/3) until error falls beyond two sigfigs.")
    sig_bits = 2
    eps = 10**(-sig_bits)
    actual = cos(pi/3)
    approx = 0
    num_terms_count = 0
    print("Actual : "+str(actual))
    while (abs(actual-approx)>=eps):
        num_terms_count = num_terms_count + 1
        approx_sum = 0
        for i in range(num_terms_count):
            approx_sum = approx_sum + ((-1)**(i))*((pi/3)**(2*i))/(fact(2*i))
        approx = approx_sum
        print(str(num_terms_count)+": Term(s) |\tApprox: "+str(approx)+" |\tError: "+str(abs(approx-actual)))
    print("It took "+str(num_terms_count)+" terms to approximate within "+str(sig_bits)+" significant figures!\n")

    #Problem 5
    print("Problem 5: Approximate x^3 - 2x + 4 from [-2, 2] with step size 0.25 and determine if 1st or 2nd deriv approximation is better. ")
    x_values = [-2.0, -1.75, -1.5, -1.25, -1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    function = lambda x: x**3 - 2*x + 4
    step_size = 0.25
    function_1st_deriv = lambda x: 3*(x**2) - 2
    first_diff_derivs = deriv1(x_values, function, step_size)
    for_1st_deriv = first_diff_derivs[0]
    back_1st_deriv = first_diff_derivs[1]
    cent_1st_deriv = first_diff_derivs[2]
    actual_1st_deriv = []
    for x in x_values:
        actual_1st_deriv.append(function_1st_deriv(x))

    function_2nd_deriv = lambda x: 6*x
    second_diff_derivs = deriv2(x_values, function, step_size)
    for_2nd_deriv = second_diff_derivs[0]
    back_2nd_deriv = second_diff_derivs[1]
    cent_2nd_deriv = second_diff_derivs[2]
    actual_2nd_deriv = []
    for x in x_values:
        actual_2nd_deriv.append(function_2nd_deriv(x))

    #Plot all derivatives
    fig = plt.figure(1)
    plt.plot(x_values, actual_1st_deriv, label="Actual")
    plt.plot(x_values, for_1st_deriv, label="Forward")
    plt.plot(x_values, back_1st_deriv, label="Backward")
    plt.plot(x_values, cent_1st_deriv, label="Central")
    plt.legend()
    plt.title("Approximation of 1st Derivative : Central Most Accurate")

    fig_2 = plt.figure(2)
    plt.plot(x_values, actual_2nd_deriv, label="Actual")
    plt.plot(x_values, for_2nd_deriv, label="Forward")
    plt.plot(x_values, back_2nd_deriv, label="Backward")
    plt.plot(x_values, cent_2nd_deriv, label="Central")
    plt.legend()
    plt.title("Approximation of 2nd Derivative : Central Most Accurate")
    plt.show()