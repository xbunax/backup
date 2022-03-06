from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
def func(x,a,b):
    return a*x+b
x=np.arange(1,30,2)
y=[4.997218286,7.784128485,10.09053692,12.58914607,17.87466541,4.997218286,7.784128485,10.09053692,12.58914607,17.87466541,39.82053981,42.24124132,49.98748615,52.89232796,57.00752052]
a1,b1 = optimize.curve_fit(func, x, y)[0]
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, a1*x+b1, 'g',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()
print(a1,'*x',b1)