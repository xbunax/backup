path='/Users/xbunax/Desktop/cupt/20��/10ʯī����/����.xlsx';
x=xlsread(path,'B12:E12');
y=xlsread(path,'B8:E8');
error=xlsread(path,'B9:E9');
errorbar(x,y,error)
