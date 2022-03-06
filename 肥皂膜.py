import numpy as np
import matplotlib.pyplot as plt
import math as m
Rf=8*10**-2#肥皂膜水平半径
#Rb=1*10**-2
gama=3.12*0.1#表面张力
mass=2*10**-3
h=4*10**-2
g=9.8
v=(2*g*h)**0.5
E=0.5*mass*v**2
k=[]
x=[]
plt.figure()
for Rb in np.arange(0.001,0.05,10**-3):
    fai=2*m.cosh(Rf/Rb)**-1
    Es=m.pi*gama*Rb**2*(m.sinh(fai)+fai)-2*m.pi*gama*(Rf**2-Rb**2)
    k.append(Es/E)
    x.append(Rb)
    if Es / E < 0:
        break
plt.plot(x,k)
plt.show()