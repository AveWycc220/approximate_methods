""" Module for numerical integration """
import math

f = lambda x: x**2 + 2

class NumInt():
    """ Class for methods of numerical integration """

    @staticmethod
    def simpson(a, b, eps):
        """
        Simpson's method
        a,b - Limits of integration
        eps - Accuracy
        """ 
        n = 100 # Started number of steps
        dn = n / 2
        second = NumInt.__simpson_integral(a, b, n)
        first = second
        n += dn
        if n%2 == 1:
            n += 1
        second = NumInt.__simpson_integral(a, b, n)
        while math.fabs(first-second) > eps:
            first = second
            n += dn
            if n%2 == 1:
                n += 1
            second = NumInt.__simpson_integral(a, b, n)
        return second

    @staticmethod
    def __simpson_integral(a, b, n):
        """ Simpson's integral """
        h = (b-a)/n
        s = f(a) + f(b)
        x = a + h
        while x < b - h:
            s += 4 * f(x) + 2 *f(x+h)
            x += 2*h
        return h/3 * (s+4*f(b-h))

if __name__ == "__main__":
    left = 0
    right = 20
    accuracy = 0.001
    NumInt.simpson(left, right, accuracy)

