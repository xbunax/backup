path='/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx';
x=xlsread(path,'B87:G87');
y=xlsread(path,'B92:G92');
error=xlsread(path,'B93:G93');
errorbar(x,y*10^-3,error*10^-3);