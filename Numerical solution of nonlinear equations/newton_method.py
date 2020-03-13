import math
from sympy import diff, symbols

class NewtonMethod:
    # Method that return the given equation.
    def __function(self, x): 
        return x * 10 - 4
    def __df(self):
        x = symbols('x')
        return diff(x* 10 -4)
    def get_result(self, a, e, x):
        __max_iter = 1000
        i = 0
        while(i < __max_iter):
            x = a - self.__function(a)/self.__df()
            a = x
            if(self.__function(x) <= e):
                return x
            i += 1
        return x
