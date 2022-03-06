import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
#(rou*g*w**2*R**2*p*x*0.5*(1-(2*1.68*p)/(3*(2*(1+(1+1.68*p)**0.5+1.68*p)))))/pe>1:
a=[[],[],[],[],[],[]]
b=[[],[],[],[],[],[]]
rou=10**3
g=10
H0=0.06
pe=10**5
R=0.0013#气泡半径
plt.figure()
plt.grid()
l=['150hz','160hz','170hz','180hz','190hz','200hz']
c=[150,160,170,180,190,200]
for f in range(len(c)):
    for A in np.arange(0,0.005,0.000001):
        for x in np.arange(0,0.01, 0.00001):

                w = 2 * m.pi * c[f]
                vp=rou*H0*g/pe#无量纲参量
                wp=A*w**2/g#无量纲参量
                p=A**2/R**2
                if 10**-7<x-(2*g*pe*(2*(1+(1+1.68*p)**0.5)+1.68*p))/(rou*w**4*A**2*(2*(1+(1+1.68*p)**0.5)+1.68*p/3))<10**-6:
                    a[f].append(x)
                    b[f].append(A)
    plt.plot(b[f],a[f],label=l[f])
    plt.legend(loc='upper right')
plt.xlabel('A')
plt.ylabel('x')
plt.xlim(0,0.005)
plt.ylim(0,0.01)
plt.show()
print('over')