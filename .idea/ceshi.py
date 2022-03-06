class A:
    def fun1(self):
        print("fun1 A")
    def fun2(self):
        print("fun2 B")
class B(A):
    def fun1(self):
        print("fun1 B")
    def fun3(self):
        print("fun2 B")
b=B()
b.fun1()
b.fun2()
a=A()
a.fun1()
a.fun2()