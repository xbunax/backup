x=xlsread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx','L7:R7');
y=xlsread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx','L13:R13');
error=xlsread('/Users/xbunax/Desktop/cupt/20年/10石墨导线/铅笔曲线.xlsx','L19:R19');
errorbar(x,y,error);