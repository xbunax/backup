path=('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ�ʵ��ߴ���.xlsx');
x=xlsread(path,'A25:A30');
y=xlsread(path,'G25:G30');
error=xlsread(path,'H25:H30');
errorbar(x,y,error)