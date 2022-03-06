def f(n):
    return n**2+n-6
def g(a,b):
    c=(a+b)/2
    while f(c)>1e-10:
        c=(a+b)/2
        if f(a)*f(c)>=0:
            a=c
        else:
            b=c
    return c
print(g(1,3))
