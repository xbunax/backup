from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d
figure=plt.figure()
#ax = Axes3D(figure)
ax=figure.gca(projection="3d")
x1=np.linspace(-6,6,1000)
y1=np.linspace(-6,6,1000)
x,y =np.meshgrid(x1,y1)
z=((20-20*(x**2-y**2)/(x**2+y**2)**2)**2+(-40*x*y/(x**2+y**2)**2)**2)**0.5
#ax.plot_surface(x,y,z,rstride=10,cstride=4,cmap=cm.YlGnBu_r)
ax.plot_surface(x,y,z,cmap="rainbow")
plt.show()




