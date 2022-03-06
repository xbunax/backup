import numpy as np
import matplotlib.pyplot as plt
edge=[0]
face=[0]
point=[]
alpha=[]
a=0
b=0
n=50
for i in range(1,n):
    p=(8*(-1)**(i-1))/(3*(i/2)**2)**0.5
    point.append(p)
e=0
for j in range(2,n):
    for i in np.arange(1-j/2,j/2-1,1):
        e=e+(12*(-1)**(j-1))/(2*(j/2)**2+i**2)**0.5
        edge.append(e)
f=0
for j in range(2,n):
    for i in np.arange(1-j/2,j/2-1,1):
        for k in np.arange(1-j/2,j/2-1,1):
            f=f+(6*(-1)**(j-1))/((j/2)**2+i**2+k**2)**0.5
            face.append(f)
for i in range(1,n-1):
    a=b+(1/8)*point[i]+(1/4)*edge[i]+0.5*face[i]
    b=b+point[i]+edge[i]+face[i]
    alpha.append((3**0.5/2)*a)
print(sum(alpha)/len(alpha))
plt.plot(alpha)
plt.show()