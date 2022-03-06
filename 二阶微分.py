import numpy as np
import matplotlib.pyplot as plt
import math as m
u0=0
x=0
dx=0.01
h=1000
y1=[]
u1=[0]
y=0
u=0
def fx(x):
    return 9*m.sin(x)-6*x
for i in np.arange(h):
    x=x+dx
    y=y+dx*(fx(x))
    y1.append(y)
    x=x+dx
for j in range(len(y1)-1):
    u=(y1[j+1]-y1[j])*dx+u
    u1.append(-u)
x=[i for i in np.arange(0,h*dx,dx)]
plt.plot(x,u1)
plt.show()
# y2=[]
# x2=[]
# for i in np.arange(0,100,0.1):
#     x2.append(i)
#     y2.append(m.sin(3*i)+i**3)
# plt.plot(x2,y2)
# plt.show()


