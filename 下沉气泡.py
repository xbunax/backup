import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
a=[]
b=[]
c=[]
rou=10**3
g=10
H0=0.12
f=150
pe=10**5
A=0.0121
w=2*m.pi*f
vp=rou*H0*g/pe
wp=A*w**2/g
x=[0.2,0.5,1]
for y in np.arange(0,2,0.001):
    for z in np.arange(0,5,0.001):
        if y*0.1*0.5*(1-2/3*((1.68*z**2)/(2*(1+(1+1.68*z**2))**0.5+1.68*z**2)))>1:
            b.append(y)
            c.append(z)
print(b)
plt.figure()
plt.plot(c,b)
plt.ylim(0,2)
plt.xlabel('c')
plt.ylabel('b')
plt.show()