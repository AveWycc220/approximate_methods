""" Module for numerical integration """
import math

f = lambda x: x**2 + 2

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

class NumInt():
    """ Class for methods of numerical integration """

    @staticmethod
    def simpson(a, b, eps):
        """
        Simpson's method
        a,b - Limits of integration
        eps - Accuracy
        """ 
        n = 1 / eps
        dn = n / 2
        second = NumInt.__simpson_integral(a, b, n)
        first = second
        n += dn
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

    @staticmethod
    def rectangle(a, b, eps):
        """ Rectangle method """
        n = eps
        first = NumInt.__rectangle(a, b, n)
        n *= 0.1
        second = NumInt.__rectangle(a, b, n)
        while math.fabs(first-second) > eps:
            first = second
            n *= 0.1
            second = NumInt.__rectangle(a, b, n)
        return second

    @staticmethod
    def __rectangle(a, b, h):
        """ Rectangle integral """
        s = 0
        x = a
        while x <= b - h:
            x += h
            s += h* f(x+h/2)
        return s
    
    @staticmethod
    def trapezoid(a, b, eps):
        """ Trapezoid method """
        n = eps
        first = NumInt.__trapezoid(a, b, n)
        n *= 0.1
        second = NumInt.__trapezoid(a, b, n)
        while math.fabs(first-second) > eps:
            first = second
            n *= 0.1
            second = NumInt.__trapezoid(a, b, n)
        return second

    @staticmethod
    def __trapezoid(a, b, h):
        """ Trapezoid integral """
        s = 0
        x = a + h
        while x < b: 
            x += h
            s += f(x)
        s = h*(s+(f(a)+ f(b))/2)
        return s

if __name__ == "__main__":
    # left -> a, right -> b, accuracy -> eps
    print("Input the left border")
    left = input()
    print("Input the right border")
    right = input()
    print("Input accuracy")
    accuracy = input()
    if (is_digit(left) and is_digit(right) and is_digit(accuracy)):
        left = float(left)
        right = float(right)
        accuracy = float(accuracy)
    else:
        print("Wrong input. Try again..")
        raise SystemExit('ValueError')
    print(F"For a = {left} | b = {right} | eps = {accuracy} ->")
    print(F"Simpson's method = {NumInt.simpson(left, right, accuracy)} ")
    print(F"Rectangle method = {NumInt.rectangle(left, right, accuracy)} ")
    print(F"Trapezoid method = {NumInt.trapezoid(left, right, accuracy)} ")