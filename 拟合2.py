from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
def func(a,x,b):
    return a*x+b
x=np.arange(0,30,2)
x0=np.array(x)
y=[4.997218286,7.784128485,10.09053692,12.58914607,17.87466541,4.997218286,7.784128485,10.09053692,12.58914607,17.87466541,39.82053981,42.24124132,49.98748615,52.89232796,57.00752052]
y0=np.array(y)
a1,b1 = optimize.curve_fit(func, x0, y0)[0]