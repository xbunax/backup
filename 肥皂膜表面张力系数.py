import numpy as np
import matplotlib.pyplot as plt
import math as m
Rf=8*10**-2#肥皂膜水平半径
Rb=0.8*10**-2
#gama=3.12*0.1#表面张力
mass=2*10**-3
v=1#speed
E=0.5*mass*v**2
k=[]
x=[]
plt.figure()
for gama in np.arange(0.0001,0.7,10**-4):
    fai=2*m.cosh(Rf/Rb)**-1
    Es=m.pi*gama*Rb**2*(m.sinh(fai)+fai)-2*m.pi*gama*(Rf**2-Rb**2)
    k.append(Es/E)
    x.append(gama)
    if Es / E < 0:
        break
plt.plot(x,k)
plt.show()