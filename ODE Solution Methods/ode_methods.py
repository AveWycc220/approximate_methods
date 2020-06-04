import ast
import sys
import math
from matplotlib import pyplot as plt

f = lambda x,y: ((x+1)**(3))+((2*y)/(x+1))
check = lambda x: ((x+1)**4)/2

def modified_euler(x, y, n):
    print("Modified Euler")
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1): 
        ytemp = y[i] + h/2 * f(x[i], y[i])
        y[i+1] = y[i] + h*f(x[i]+h/2, ytemp)
        x[i+1] = x[i] + h
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y

def euler_recount(x, y, n): 
    print("Euler With Recount")
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        ytemp = y[i] + h*f(x[i], y[i])
        y[i+1] = y[i] + h/2 * (f(x[i], y[i]) + f(x[i]+ h, ytemp))
        x[i+1] = x[i] + h
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y

def runge_kutta(x, y, n): 
    print("Method of Runge-Kutta")
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1): 
        k0 = f(x[i], y[i])
        k1 = f(x[i] + h/2, y[i] + h*k0/2)
        k2 = f(x[i] + h/2, y[i] + h*k1/2)
        k3 = f(x[i] + h, y[i]+h*k2)
        y[i+1] = y[i] + h/6 * (k0 + 2*k1 + 2*k2 + k3)
        x[i+1] = x[i] + h
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y

def adams(x, y, n, h): 
    print("Adams Method")
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    f_list = [0 for i in range (n)]
    f_list[0] = f(x[0], y[0])
    x[1] = x[0] + h
    y[1] = y[0] + h*f_list[0]
    f_list[1] = f(x[1], y[1])
    print(F'{x[1]:20} | {y[1]:20} | {check(x[1]):20}')
    x[2] = x[1] + h
    y[2] = y[1] + h*((3/2)*f_list[1]-(1/2)*f_list[0])
    f_list[2] = f(x[2], y[2])
    print(F'{x[2]:20} | {y[2]:20} | {check(x[2]):20}')
    x[3] = x[2] + h
    y[3] = y[2] + (h/12)*(23*f_list[2] - 16*f_list[1] + 5*f_list[0])
    f_list[3] = f(x[3], y[3])
    print(F'{x[3]:20} | {y[3]:20} | {check(x[3]):20}')
    for i in range(3, n-1):
        y[i+1] = y[i] + (h/24)*(55*f_list[i] - 59*f_list[i-1] + 37*f_list[i-2] - 9*f_list[i-3])
        x[i+1] = x[i] + h
        f_list[i+1] = f(x[i+1], y[i+1])
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y

if __name__ == "__main__":
    a = 0
    b = 1
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
    x[0] = 0
    y[0] = 1/2
    x_me, y_me = modified_euler(x, y, n)
    plt.plot(x_me,y_me,'o', ms=2, color='black')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximation Solution with Modified Euler's Method")
    plt.show()
    x_er, y_er = euler_recount(x, y, n)
    plt.plot(x_er,y_er,'o', ms=2, color='black')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximation Solution with Euler's Method With Recount")
    plt.show()
    x_rk, y_rk = runge_kutta(x, y, n)
    plt.plot(x_rk,y_rk,'o', ms=2, color='black')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximation Solution with Runge-Kutta Method")
    plt.show()
    x_a, y_a = adams(x, y, n, h)
    plt.plot(x_a,y_a,'o', ms=2, color='black')
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title("Approximation Solution with Adams Method")
    plt.show()