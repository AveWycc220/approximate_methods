import math

class ChordMethod:
    # Method that return the given equation.
    def __function(self, x): 
        return x * 10 - 4
    def get_result(self, a, b, e):
        while(math.fabs(b - a) > e):
    	    a = b - (b - a) * self.__function(b) / (self.__function(b) - self.__function(a))
    	    b = a + (a - b) * self.__function(a) / (self.__function(a) - self.__function(b))
        return b