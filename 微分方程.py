import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def func(y, t):
    return t * math.sqrt(y)

YS=odeint(func,y0=1,t=np.arange(0,10.1,0.1))

t=np.arange(0,10.1,0.1)
plt.plot(t, YS, label='odeint')
plt.legend()
plt.show()