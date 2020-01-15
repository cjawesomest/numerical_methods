## Cameron Calv ECE T480
import math

def fact(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1 and isinstance(n, int):
        result = 1
        current_mult = n
        while current_mult != 0:
            result = result * current_mult
            current_mult = current_mult - 1
        return result
    else:
        return 0

if __name__ == '__main__':
    test_num = 1
    print("My calculated factorial of 10: ", fact(test_num))
    print("Real factorial of 10: ", math.factorial(test_num))
    assert(fact(test_num) == math.factorial(test_num))
    print("These values are the same!")
