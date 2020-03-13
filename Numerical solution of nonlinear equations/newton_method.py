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

def is_digit(str):
    if str.isdigit():
       return True
    else:
        try:
            float(str)
            return True
        except ValueError:
            return False   

if __name__ == "__main__":
    print("Input the borders of section")
    a = input()
    b = input()
    print("Input accuracy")
    e = input()
    if (is_digit(a) and is_digit(b) and is_digit(e)):
        a = float(a)
        b = float(b)
        e = float(e)
    else:
        print("Wrong input. Try again..")
        raise SystemExit('ValueError')
    NM = NewtonMethod()
    print(round(NM.get_result(a,b,e),10))
