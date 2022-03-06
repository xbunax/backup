print('请输入数据')
x=[]
n=0
a=0
k=[]
z=[]
while n<=1024:
    b=float(input())
    x.append(b)
    n+=1
for i in x:
    a=a+i
c=a/n
for h in x:
    k.append(h-c)
for c in k:
    z.append(c**2)
print(sum(z)/n)


