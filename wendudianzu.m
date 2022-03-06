x=xlsread('','B79:G79');
y=xlsread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx','B84:G84');
error=xlsread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx','B85:G85');
errorbar(x,y.^-1,error)