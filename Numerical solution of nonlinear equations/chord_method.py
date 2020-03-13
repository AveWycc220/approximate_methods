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
    CM = ChordMethod()
    print(round(CM.get_result(a,b,e),10))