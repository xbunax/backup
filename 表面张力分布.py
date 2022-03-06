import sympy as sym
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
Rf=8*10**-2#肥皂膜水平半径
Rb=0.95*10**-2
gama=3.58*0.01#表面张力
rou=9.55#kg/m^3
h=3*10**-2#m
g=9.8
def func1(x):
    return sym.acosh(x/Rb)*Rb
x=sym.symbols('x')
def y1(x,i):
    return sym.diff(func1(x),x).subs(x,i)
def y2(x,i):
    return sym.diff(func1(x),x,2).subs(x,i)
h=[]
j=[]
for i in np.arange(Rb,Rf,10**-4):
    h.append(i)
    R = abs((1+y1(x,i)**2)**1.5/y2(x,i))
    s = sym.pi*(Rb*sym.sin(sym.pi/4))
    F = gama*s/R
    j.append(F)
plt.figure()
plt.plot(h,j)
plt.xlabel('Rb/cm')
plt.ylabel('F/N')
plt.show()
print(max(j))
print(y1(x,Rf))


