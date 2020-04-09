import math
import numpy as np
import matplotlib.pyplot as pl

MAX_POINTS_X_LAGRANGE = 1000
MAX_POINTS_X_NEWTON = 1000


def f(x):
    return 2 * math.sin(x)
def lagranz(x,y,t):
    polynom=0
    for j in range(len(y)):
        numerator=1; denumerator=1
        for i in range(len(x)):
            if i==j:
                pass   
            else: 
                numerator=numerator*(t-x[i])
                denumerator=denumerator*(x[j]-x[i])
        polynom=polynom+y[j]*numerator/denumerator
    return polynom

if __name__ == '__main__':
    x = np.linspace(0,2*math.pi,50, dtype = float)
    y = np.array([f(x[i]) for i in range(len(x))], dtype=float)
    xnew=np.linspace(np.min(x),np.max(x),MAX_POINTS_X_LAGRANGE)
    ynew=[lagranz(x,y,i) for i in xnew]
    pl.plot(xnew,ynew, color = 'red')
    pl.plot(x,y, color = 'blue')
    pl.grid()
    pl.show()