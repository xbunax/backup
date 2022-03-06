import math as m
import numpy as np
import sympy
import matplotlib.pyplot as plt
Rb=0.01#小球半径
Rf=0.08#肥皂膜水平半径
fai=2*(sympy.acosh(Rf/Rb))
gama=32*10**-3
v=0.09
m=0.09*10**-3
g=9.8
h=8.03*10**-2
x=[]
y=[]
EK1=0.5*m*v**2
EK2=m*g*h
Es=3.1415926*gama*Rb**2*(sympy.sinh(fai)+fai)-2*3.1415926*gama*(Rf**2-Rb**2)
k=Es/EK2
print("Es",Es)
print("Ek",EK2)
# print('Eg',Eg)
print("k",k)