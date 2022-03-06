def huiwen(n):
    n=str(n)
    n=list(n)
    a=[]
    b=[]
    for h in range(len(n)-1,-1,-1):
        b.append(n[h])
    if n==b:
        return 'yes'
    else:
        return 'not'
print(huiwen(1234321))

