path='/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx';
x=xlsread(path,'B87:G87');
y=xlsread(path,'B92:G92');
error=xlsread(path,'B93:G93');
errorbar(x,y*10^-3,error*10^-3);