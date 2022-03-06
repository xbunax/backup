with open('python.py','r') as f1:
    x=list(f1.readlines())
    a=[]
    for i in range(len(x)):
        s=x[i]
        for h in range(len(s)):
            if s[h]!=" ":
                a.append(s[h])
            elif s[h]=="#":
                for j in range(i,len(s)+1):
                    del s[j]
    with open('python2.txt','w') as f2:
        a=str(a)
        f2.write(a)


