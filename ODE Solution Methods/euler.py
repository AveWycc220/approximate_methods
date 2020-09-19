import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
import sys

""" CONST """
WIDTH = 12
HEIGHT = 8

""" Functions """ 

f = lambda x,y: ((2 * (x ** 4) + 2 * y)/x)
check = lambda x: (x ** 2) * ((x ** 2) - 79/9)

def modified_euler(x, y, n, h):
    """ Modified Euler Method """
    print('Modified Euler Method')
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        ytemp = y[i] + h/2 * f(x[i], y[i])
        y[i+1] = y[i] + h*f(x[i]+h/2, ytemp)
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return y

def euler_recount(x, y, n, h):
    """ Method of Euler with Recount """
    print('Method of Euler with Recount')
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        ytemp = y[i] + h*f(x[i], y[i])
        y[i+1] = y[i] + h/2 * (f(x[i], y[i]) + f(x[i]+ h, ytemp))
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return y

def euler_right_diff(x, y, n, h):
    """ Method of Euler with Right Differences """
    print('Method of Euler with Right Differences')
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        y[i+1] = y[i] + h*f(x[i], y[i])
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return y

def euler_left_diff(x, y, n, h):
    print('Method of Euler with Left Differences')
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    for i in range(n-1):
        y[i+1] = y[i] + h*f(x[i+1], y[i+1])
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return y

def euler_central_diff(x, y, n, h):
    print('Method of Euler with Central Differences')
    print((' ' * 19) + 'X' + (' ' * 22) + 'Y' + (' ' * 16) + 'Y_Check')
    y[1] = y[0] + h*f(x[0], y[0])
    for i in range(1, n-1):
        y[i+1] = y[i-1] + 2*h*f(x[i], y[i])
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return y

def create_plots(h, n):
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    x[0] = 3
    for i in range(n-1): 
        x[i+1] = x[i] + h
    y[0] = 2
    sns.set()
    plt.figure(figsize=(WIDTH,HEIGHT))
    y_check = [check(x[i]) for i in range(len(x))]
    plt.plot(x, y_check, color='red')
    y_rf = euler_right_diff(x, y, n, h)
    plt.plot(x, y_rf, color='black')
    y_lf = euler_left_diff(x, y, n, h)
    plt.plot(x, y_lf, color='green')
    y_cd = euler_central_diff(x, y, n, h)
    plt.plot(x, y_cd, color='blue')
    y_me = modified_euler(x, y, n, h)
    plt.plot(x, y_me, color='indigo')
    y_er = euler_recount(x, y, n, h)
    plt.plot(x, y_er, color='saddlebrown')
    plt.legend(['Analytical', 'Euler with Right Differences', 'Euler with Left Differences', \
     'Method of Euler with Central Differences', 'Modified Euler', 'Euler with Recount'])
    plt.xlabel("Value of x")
    plt.ylabel("Value of y")
    plt.title(f'h = {h}',fontdict={'size': 18})
    plt.show()


if __name__ == "__main__":
    a = 3
    b = 4
    h_list = [0.25, 0.1, 0.05, 0.01]
    for h in h_list:
        n = math.ceil(((b-a)/h + 1))
        create_plots(h, n)