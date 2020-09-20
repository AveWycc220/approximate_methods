import ast
import sys
import math

f = lambda x,y,u: (2*x*u)/(1+x**2)
check = lambda x: x**3 + 3*x

def euler_method(x, y, u, n):
    print("Euler")
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*u[i]
        u[i+1] = u[i] + h*f(x[i], y[i], u[i])
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y,u

if __name__ == "__main__":
    a = 0
    b = 3
    try:
        h = ast.literal_eval(input("Input the value of step\n"))
        if not isinstance(h, (float,int)): 
            print('Wrong Input')
            sys.exit('Error : Wrong Input')
    except ValueError:
        print('Wrong Input')
        sys.exit('Error : Wrong Input')
    n = math.ceil(((b-a)/h + 1))
    x = [0 for i in range (n)]
    y = [0 for i in range (n)]
    u = [0 for i in range (n)]
    y[0] = 0
    u[0] = 3
    x,y,u = euler_method(x, y, u, n)