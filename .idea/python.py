import pickle
with open("student.dat","wb") as f:
    while True:
        id=int(input("请输入学号:"))
        if id<0:
            break
        name=input("请输入姓名")
        sex=input("请输入性别")
        age=input("请输入年龄")
        print("************")
        record=(id,name,sex,age)
        try:
            pickle.dump(record,f)
        except:
            print("写入文件异常")
with open("student.dat","rb") as f:
    result=[]
    try:
        while record:
            record=pickle.load(f)
            result.append(record)
    except EOFError:
        f.close()
print(result)
result=sorted(result,key=(lambda result:result[0]))
print("学号","姓名","性别","年龄")
for record in result:
    print("%3d%4s%4s%4d"%(record[0],record[1],record[2],record[3]))

