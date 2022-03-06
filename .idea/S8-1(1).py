f=open('d:\in.txt')
s=f.read()
e=''
for i in range(len(s)):
    #print(s[i])
    if s[i].isupper():
        e+=s[i].lower()
    else:
        e+=s[i]
print(e)
f.close()
