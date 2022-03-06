import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]
x=[0.2,0.5,1]
for y in np.arange(0,2,0.0001):
    for z in np.arange(0,5,0.001):
        if (100/y)*((2+2*(1+1.68*z**2)**0.5+1.68*z**2)/(2+2*(1+1.68*z**2)**0.5+1.68*z**2/3))>10:
            b.append(y)
            c.append(z)
print(b)
plt.figure()
plt.plot(c,b)
plt.ylim(0,2)
plt.xlabel('c')
plt.ylabel('b')
plt.legend()
plt.show()