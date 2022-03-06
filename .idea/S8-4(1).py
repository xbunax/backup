def StudentFind(AllStudent,index,msg):
    n=len(AllStudent)
    c=0
    for i in range(n):
        if AllStudent[i][index].find(msg)!=-1:
            #print(AllStudent[i])    #######
            for j in range(len(AllStudent[i])):
                print(AllStudent[i][j],end=' ')
            print()
            c+=1
    if c==0:
        print('无')

def ReadStudent(AllStudent,fname):
    f=open(fname)
    x=f.readline()
    x=f.readline()
    while x:
        tmpList=(x.strip()).split(',')
        AllStudent.append(tmpList)
        x=f.readline()

    f.close()
    
AllStudent=[]
ReadStudent(AllStudent,r'd:\sample.csv')

x=input()
fieldname,msg=x.split('=')
if fieldname=='姓名':
    index=1
elif fieldname=='省份':
    index=5
    
StudentFind(AllStudent,index,msg)



