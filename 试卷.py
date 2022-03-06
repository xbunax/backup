with open("sample.csv",encoding='GBK') as f:
    s=f.readlines()
    f.close()
    number = []
    name = []
    sub = []
    sex = []
    age = []
    where = []
for i in range(1, len(s)):
    x=list(s[i].split(','))
    number.append(x[0])
    sub.append(x[2])
    sex.append(x[3])
    age.append(x[4])
    name.append(x[1])
    where.append(x[5])
print("输入:")
n = input()
n = n.split("=")
l=0
k=0
if n[0] == "姓名":
        for h in range(len(name)):
            if n[1] in name[h]:
                l+=1
                print(number[h], name[h], sub[h], sex[h], age[h], where[h], end='\n')
            elif l==0 and h==len(name)-1:
                print("无匹配记录")
elif n[0] == "省份":
    for j in range(len(where)):
        if n[1] in where[j]:
            l+=1
            print(number[j], name[j], sub[j], sex[j], age[j], where[j], end='\n')
        elif l==0 and j==len(where)-1:
            print("无匹配记录")
elif n[0]!="姓名" and n[0]!="省份":
    print("请输入姓名或者省份")
