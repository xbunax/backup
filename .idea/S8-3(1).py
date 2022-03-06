def delthree():
    pass

f=open(r'd:\test.txt')
x=f.readline()
fw=open(r'd:\out1.txt','w')

i=1
while x:
    n=x.find('#')   #检查注释
    if n!=-1:
        tmp=x[:n]
    else:
        tmp=x
        
    tmp=tmp.strip()
    if  tmp!='':   #不为空行
        #print(tmp)   #显示到屏幕上
        #存入到文件中
        fw.write(tmp+'\n')

    i+=1
    x=f.readline()
    
delthree()
f.close()
fw.close()
