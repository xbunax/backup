f=open('data.txt','r')
nA=0
na=0
n0=0
nr=0
while True:
    x=f.read(1)
    if x=="":
        break
    if x.isupper():
        nA=nA+1
    elif x.islower():
        na=na+1
    elif x.isdigit():
        nr=nr+1
    else:
        n0=n0+1
f.close()
print('na=',na)
print('nA=',nA)
print('n0=',n0)
print('nr=',nr)