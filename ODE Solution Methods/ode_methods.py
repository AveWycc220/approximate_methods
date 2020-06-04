import ast
import math
from matplotlib import pyplot as plt

f = lambda x,y: ((x+1)**(3))+((2*y)/(x+1))
check = lambda x: ((x+1)**4)/2

def modified_euler(x, y, n):
    print("Modified Euler")
    for i in range(n-1): 
        ytemp = y[i] + h/2 * f(x[i], y[i])
        y[i+1] = y[i] + h*f(x[i]+h/2, ytemp)
        x[i+1] = x[i] + h
        print(F'{x[i+1]:20} | {y[i+1]:20} | {check(x[i+1]):20}')
    return x,y

if __name__ == "__main__":
    a = 0
    b = 1
    h = ast.literal_eval(input("Input the value of step\n"))
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

