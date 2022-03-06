f=open(r'd:\test.txt')
x=f.readline()
i=1
while x:
    tmp='#'+str(i)+'.'
    print(tmp.ljust(4),end='')
    print(x.strip())
    i+=1
    x=f.readline()

f.close()
