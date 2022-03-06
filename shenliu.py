import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pylab as lp
from pylab import *
from scipy.ndimage import measurements
from IPython.display import display,clear_output
lp.rcParams['figure.figsize'] = (8, 8)
from scipy.ndimage import measurements
import cv2
plt.ioff()
ax=plt.gca()
N=100
cc=-0.01
dd=0
R = np.random.random((N,N))
colors = ['red','black','white']
cmap = mpl.colors.ListedColormap(colors)
out=widgets.Output()
button=widgets.Button(description='Next')
cc +=0.02
B = np.where(R < cc, 1, 0)
B1=logical_not(B)*1
lw, num = measurements.label(B)
w=np.max(lw)
area = measurements.sum(B, lw, index=arange(lw.max() + 1))
sB=B.sum()
w1=np.max(area)
ix=[i for i, x in enumerate(area) if x == w1]
a = np.array(ix)
C = np.where(lw ==a[0], 1, 0)
C1 = logical_not(C)*1
D=B1+C1
ama = logical_not(D)*1
sama=ama.sum()
p=sB/(N*N)
im1 = ax.imshow(D, cmap=cmap, interpolation='nearest')