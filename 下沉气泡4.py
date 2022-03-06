import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
a=[]
b=[]
c=[]
rou=10**3
g=10
H0=0.16
f=150
pe=10**5
R=0.0009#气泡半径
w=2*m.pi*f
for x in np.arange(0,2,0.001):
    for A in np.arange(0,1,0.001):
        p= A ** 2 / R ** 2
        vp = rou * H0 * g / pe
        wp = A  * w ** 2 / g
        if x-2*H0*(1+(1+1.68*p)**0.5+1.68*p)/vp*wp**2*(1+(1+1.68*p)**0.5+1.68*p/3)<=10**-3:
            b.append(x)
            c.append(A)
print(b)
plt.figure()
plt.plot(c,b)
plt.ylim(0,2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()