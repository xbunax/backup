with open('sample.txt') as f:
    for i in f:
        if 'a'<=i<='z':
            s1=i.upper()
            print(s1)
        else:
            s2=i.lower()
            print(s2)

