import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
h=1000#分成1000份
rc=2#常数
dt=0.01#步长
t=0#初值
q=1#初值
a=[]
for i in np.arange(h):
    q=(dt*q/2*rc+q)/(1+dt/2)
    a.append(q)
x=[i for i in np.arange(0,h*dt,dt)]
fx=[]
error=[]
for i in range(len(a)):
    fx.append(sym.E**(x[i]/rc))
    error.append(sym.E**(x[i]/rc)-a[i])
plt.plot(x,a,x,fx,x,error)
plt.xlabel('x')
plt.ylabel('y')
plt.show()