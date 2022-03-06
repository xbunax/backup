import numpy as np
import matplotlib.pyplot as plt
h=1000
Q=1
dt=0.01
t=2
a=[]
for i in range(h):
    Q=dt*Q/t+Q
    a.append(Q)
x=[i for i in np.arange(0,h*dt,dt)]
plt.plot(x,a)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
