x=xlsread('','B79:G79');
y=xlsread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx','B84:G84');
error=xlsread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx','B85:G85');
errorbar(x,y.^-1,error)