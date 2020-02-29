import math

class DichotonomyMethod:
    # Method that return the given equation.
    def __function(self, x): 
        return x * 10 - 4
    def get_result(self, a, b, e):
        while math.fabs(a-b) > e:
            c = (a+b)/2
            if(self.__function(c) == 0):
                return c
            if(self.__function(a) * self.__function(c) < 0):
                b = c
            else:
                a = c
        return c

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
    if (a.isdigit() and b.isdigit() and is_digit(e)):
        a = int(a)
        b = int(b)
        e = float(e)
    else:
        print("Wrong input. Try again..")
        raise SystemExit('ValueError')
    DM = DichotonomyMethod()
    print(DM.get_result(a,b,e))
