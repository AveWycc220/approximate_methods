import math

class DichotonomyMethod:
    # Method that return the given equation.
    def __function(self, x): 
        return x * 10 - 4
    def get_result(self, a, b, e):
        if (self.__function(a)/self.__function(b) > 0.0):
            return "The signs at the ends of the line are the same."
        while math.fabs(a-b) > e:
            c = (a+b)/2
            if(self.__function(c) == 0):
                return c
            if(self.__function(a) * self.__function(c) < 0):
                b = c
            else:
                a = c
        return c

