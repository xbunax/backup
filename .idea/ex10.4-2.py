f=open('record.txt','r')
s=f.readlines()
f.close()
name=[]
age=[]
score=[]
sum=0
for i in range(1,len(s)):
    x=list(s[i].split(','))
    name.append(x[0])
    age.append(int(x[1]))
    score.append(int(x[2]))
print("不及格的学生有\n")
for i in range(0,len(score)):
    sum=sum+i
    if score[i]<60:
        print(name[i],age[i],score[i],"\n")
print("J开头的学生有\n")
for i in range(0,len(name)):
    if 'J' in name[i]:
        print(name[i], age[i], score[i], "\n")
print("学生总分是",sum)
