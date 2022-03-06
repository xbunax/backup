import numpy as np
import matplotlib.pyplot as plt
import math as m
Rf=8*10**-2#肥皂膜水平半径
#Rb=1*10**-2
gama=3.58*0.01#表面张力
rou=9.55#kg/m^3
h=3*10**-2#m
g=9.8
v=(2*g*h)**0.5
#E=0.5*mass*v**2
k=[]
x=[]
y=[]
for Rb in np.arange(0.01,0.08,0.001):
    E=(rou*4*m.pi*Rb**3/3)*g*h
    fai=2*m.acosh(Rf/Rb)
    Es = m.pi * gama * Rb ** 2 * (m.sinh(fai) + fai) - 2 * m.pi * gama * (Rf ** 2 - Rb ** 2)
    y.append(Es/E)
    x.append(Rb)
    if Es/E-1<10**-4:
        print(Rb)
plt.plot(x,y)
plt.show()
