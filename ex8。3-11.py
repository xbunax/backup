import math
def g(a,b):
    n=100000
    h=(b-a)/n
    f=[]
    d=h*((math.sin(a)+math.sin(b))/2)
    for i in range(1,n):
        f.append(math.sin(a+i*h))
    g=h*sum(f)
    return g+d
print(g(0,3.14))
