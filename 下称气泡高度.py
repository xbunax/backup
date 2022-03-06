import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
#(rou*g*w**2*R**2*p*x*0.5*(1-(2*1.68*p)/(3*(2*(1+(1+1.68*p)**0.5+1.68*p)))))/pe>1:
a=[]
b=[]
rou=10**3
g=10
H0=0.06
f=200
pe=10**5
R=0.0013#气泡半径
w=2*m.pi*f
for A in np.arange(0,0.05,0.00001):
    for x in np.arange(0, 0.006, 0.00001):
        vp=rou*H0*g/pe#无量纲参量
        wp=A*w**2/g#无量纲参量
        p=A**2/R**2
        if 10**-7<x-(2*g*pe*(2*(1+(1+1.68*p)**0.5)+1.68*p))/(rou*w**4*A**2*(2*(1+(1+1.68*p)**0.5)+1.68*p/3)):
            a.append(x)
            b.append(A)
plt.figure()
plt.grid()
plt.plot(b,a,alpha=0.6)
plt.xlabel('A')
plt.ylabel('x')
plt.xlim(0,0.05)
plt.ylim(0,0.006)
plt.plot(0.0242,0.0185,'o',alpha=0.4,color='green')
plt.show()
print(b)
print(a)