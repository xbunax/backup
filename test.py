import sympy as sym
x=sym.symbols('x')
f=sym.E**x
k=sym.integrate(f,x)
print(k)