n=input("输入")
n=list(n.split(','))
a=[]
for i in n:
    a.append(int(i))
print("均值",sum(a)/len(a))
