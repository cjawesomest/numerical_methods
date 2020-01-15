## Cameron Calv ECE T480
import numpy as np

def machine_epsilon():
    epsilon = 1
    while epsilon+1 > 1:
        epsilon = epsilon/2
    return epsilon *2

if __name__ == '__main__':
    print("My calculated Machine Epsilon: ", machine_epsilon())
    print("Numpy's Machine Epsilon: ",np.finfo(float).eps)
    assert(machine_epsilon() == np.finfo(float).eps)
    print("These values are the same!")