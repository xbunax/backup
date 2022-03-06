eleList=[(1,2),(2,3),(4,5)]
result = {}
num = 1
for i in eleList:
    result[i] = num
    num+=1
result[(2,3)]=(2,3)
if result[(2,3)]==(2,3):
    print(True)
m=1
for i in result:
    print(i,result[i])
k=[]
for i in result.keys():
    k.append(result.get(i))
print(k.count(1))