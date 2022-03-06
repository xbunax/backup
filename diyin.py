import math
import numpy as np
import matplotlib.pyplot as plt
a=[]
b=[]
for i in np.arange(0,1,0.001):
    for h in np.arange(0,1.5,0.001):
        if i-math.log(h)<10**-4:
            a.append(h)
            b.append(i)
plt.figure()
plt.plot(a,c)
plt.ylim(0,1)
plt.xlabel('c')
plt.ylabel('b')
plt.legend()
plt.show()