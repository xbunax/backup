path=('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx');
x=xlsread(path,'G65:J65');
y=xlsread(path,'G71:J71');
error=xlsread(path,'G72:J72');
errorbar(x,y*10^-3,error*10^-3);
