path=('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔导线次数.xlsx');
x=xlsread(path,'A25:A30');
y=xlsread(path,'G25:G30');
error=xlsread(path,'H25:H30');
errorbar(x,y,error)