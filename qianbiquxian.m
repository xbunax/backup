x=xlsread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx','L7:R7');
y=xlsread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx','L13:R13');
error=xlsread('/Users/xbunax/Desktop/cupt/20��/10ʯī����/Ǧ������.xlsx','L19:R19');
errorbar(x,y,error);