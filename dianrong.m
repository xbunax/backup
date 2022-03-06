path='/Users/xbunax/Desktop/cupt/20年/10石墨导线/电容.xlsx';
x=xlsread(path,'B12:E12');
y=xlsread(path,'B8:E8');
error=xlsread(path,'B9:E9');
errorbar(x,y,error)
