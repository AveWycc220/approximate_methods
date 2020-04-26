import math
import numpy as np
import matplotlib.pyplot as pl

step_lagrange = 0.7
newton_step = 0.4


def f(xf):
    return math.cos(xf)

def lagrange(xl,yl,t):
    polynom=0
    for j in range(len(yl)):
        numerator=1; denumerator=1
        for i in range(len(xl)):
            if i==j:
                pass   
            else: 
                numerator=numerator*(t-xl[i])
                denumerator=denumerator*(xl[j]-xl[i])
        polynom=polynom+yl[j]*numerator/denumerator
    return polynom

def delta(y_d,k,i):
    c=1.0
    s=0.0
    for j in range(k):
        s=s+c*y_d[i+k-j]
        c=c*(-1)*(k-j)/(j+1)
    return s

def newton(x_n,y_n):
    z = 0
    j = 0
    s_list = list()
    h = int(round(10/newton_step))
    while j < 10:
        j += newton_step
        s = y[0]
        a=1
        for i in range(1,h):
            a *= (z-x_n[i-1])/(i*newton_step)
            s += delta(y_n,i,0)*a
        z += newton_step
        s_list.append(s)
    return s_list

if __name__ == '__main__':
    x = np.array([x for x in np.arange(0,10,0.5)], dtype = float)
    x_list = [x for x in np.arange(0,10,newton_step)]
    y = np.array([f(x[i]) for i in range(len(x))], dtype=float)
    y_list = [f(x_list[i]) for i in range(len(x_list))]
    xnew=np.array([x for x in np.arange(0,10,step_lagrange)],dtype = float)
    ylagrange=[lagrange(x,y,i) for i in xnew]
    ynewton = newton(x_list,y_list)
    pl.axis(xlim=(0, 10), ylim=(-100, 100))
    pl.plot(xnew,ylagrange, color = 'red', label = 'lagrange')
    pl.plot(x,y, color = 'blue', label = '2 * sin(x)', linestyle='dashed')
    pl.plot(x_list,ynewton, color = 'green', label = 'newton')
    pl.grid()
    pl.xlim(0,10)
    pl.ylim(-50,50)
    pl.show()