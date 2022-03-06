with open("/Users/xbunax/Downloads/数据2.txt") as f:
    s=f.readlines()
l=[]
x=[]
y=[]
for z in range(0,len(s)):
    l=list(s[z].split('\t'))
    x.append((l[0]))
    print(l)

