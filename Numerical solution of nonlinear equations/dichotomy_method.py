import math

class DichotonomyMethod:
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

if __name__ == "__main__":
        print("Input the borders of section")
        a = int(input())
        b = int(input())
        print("Input accuracy")
        e = float(input())
        DM = DichotonomyMethod()
        print(DM.get_result(a,b,e))
