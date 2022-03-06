import math as m
import numpy as np
import sympy as sym
from scipy.misc import derivative
import matplotlib.pyplot as plt
h=100000
R=0.001
rou=10**3
gama=35*10**-2
g=9.8
Bo=rou*g*R**2/gama
fai=3*m.pi/4
zs=(1-(1+4*Bo*(1-m.cos(fai)))**0.5)/2*Bo
zstart=0
zend=zs
y=np.zeros(h)
k=100
dx=((zend/R)-(zstart/R))/(h-1)
z=np.linspace(zstart/R,zend/R,num=h)
a=zend/R
for j in np.arange(1,len(y)-1):
        y[-1]=m.sin(fai)
        y[-1]=y[-2]+(m.tan(fai)**-1)*dx
        y[0]=2
        y[1]=y[0]+k*dx
        y[j+1]=(1/y[j-1])*dx**2*(1+(((y[j]-y[j-1])/dx)**2))-Bo*z[j-1]*dx**2*(1+((y[j]-y[j-1])/dx)**2)**1.5+(2*y[j]-y[j-1])
        if y[j+1]>y[j] and abs(abs((y[j+1]-y[j])/dx)-abs(m.tan(fai)**-1))<=1e-3:
                print(j)
                print(abs(abs((y[j+1]-y[j])/dx)-abs(m.tan(fai)**-1)))
                break
y1=[]
y1.append(m.tan(fai)**-1)
for i in range(1,len(z)-1):
        a=(z[i]-z[i-1])/(y[i]-y[i-1])
        y1.append(a)
y1.append(k)
plt.plot(y,y1)
y=y[:j]
y=R*y
z=z[:len(y)]
z=R*z
plt.figure()
plt.plot(y,z)
plt.show()
print(y1[-1],y1[-2],y1[-3])
