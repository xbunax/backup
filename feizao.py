import math as m
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.misc import derivative
from sympy import *
import sympy
a0=[-0.06947,-0.07012,-0.06183,-0.06722,0.04589]
a1=[0.00264,0.002468,0.001017,0.001348,0.05933]
b1=[-0.0002948,0.001787,-0.00606,0.003432,0.008236]
rou=10.0**3
D0=(2.88*10**-3+2.721*10**-3+2.77*10**-3)/3
gama=71.97*10**-3
a2=[0.001304,0.000459,-0.001163,0.003517,0.01514]
b2=[0.003597,-0.0007819,8.861*10**-5,0.0009032,0.01271]
w=[3.002,4.712,4.284,2.48,1.447]
def func1(x,l):
    return a0[l]+a1[l]*sympy.cos(w[l]*x)+b1[l]*sympy.sin(w[l]*x)
def func2(x,l):
    a0[l]=float(a0[l])
    a1[l]=float(a1[l])
    b1[l]=float(b1[l])
    a2[l]=float(a2[l])
    b2[l]=float(b2[l])
    w[l]=float(w[l])
    return a0[l]+a1[l]*sympy.cos(w[l]*x)+b1[l]*sympy.sin(x*w[l])+a2[l]*sympy.cos(2*x*w[l])+b2[l]*sympy.sin(2*w[l]*x)
x=sympy.symbols('x')
def U0(i,l):
    return diff(func2(x,l),x).subs(x,i)
#
# We=rou*U0(0.25,3)**2*D0/gama
# print(We)
h=9.0*10**-2
g=9.8
m=0.09*10**-3
E=m*g*h
Rf=8*10**-2#肥皂膜水平半径
Rb=1*10**-2
gama=40*10**-3
fai=2*(sympy.acosh(Rf/Rb))
Es=3.1415926*gama*Rb**2*(sympy.sinh(fai)+fai)-2*3.1415926*gama*(Rf**2-Rb**2)
k=Es/E
print(k)
