f=lambda x,y: x if x>y else y
n=input()
a,b,c=map(int,n.split(','))
if f(a,b)==a:
    if f(a,c)==c:
        print(c)
    else:
        print(a)
else:
    if f(b,c)==b:
        print(b)
    else:
        print(c)