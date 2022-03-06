import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import math as m
with open('/Users/xbunax/Downloads/20191017.txt') as f:
 s=f.readlines()
 f.close()
x=[]
y=[]
b=[0]
x1=[]
y1=[]
x2=[]
y2=[]
for z in range(0,len(s)):
    l=list(s[z].split('\t'))
    x.append((l[0]))
    y.append(l[1].rstrip("\n"))

for h in range(0,len(x)):
    if x[h]=='':
        b.append(h)
b.append(len(x))
for l in range(0,len(b)-1):
    x1.append([])
    y1.append([])
for t in range(0,len(b)-1):
    if t!=0:
        for c in range(b[t]+1,b[t+1]):
            x1[t].append(float(x[c]))
            y1[t].append(float(y[c].strip("\n")))
    elif t==0:
        for c in range(b[t],b[t+1]):
            x1[t].append(float(x[c]))
            y1[t].append(float(y[c].strip("\n")))
n2=1#间隔几个干涉条纹取值
xielv1=[]#干涉斜率
xielv2=[]#衍射斜率
xielv3=0
bochang=635  #激光波长
ganshe=[]
yanshe=[]
D=0.8#激光到光屏距离D
d1=1.203#弹簧平行间距真实值d1
a1=0.186333333#铁丝直径真实值a1
a=16.9#α角度真实值
p=1.444#弹簧竖直间距p
R=2.5425#弹簧半径真实值R
def func(x,a,b):
    return a*x+b
def nihe(x,y):
    x0=np.array(x)
    y0=np.array(y)
    a10,b10 = optimize.curve_fit(func,x0,y0)[0]
    return a10
b1=len(x1)
for g in range(0,len(b)-2):
    for i in range(0,len(x1[g])-1,2):
        ganshe.append(((x1[g][i]-x1[g][i+1])**2+(y1[g][i]-y1[g][i+1])**2)**0.5*1000)
    xa=[o for o in range(1,len(ganshe)+1)]
    ya=ganshe
    ak=nihe(xa,ya)
    xielv1.append(ak)
    ganshe.clear()
for d in range(0,len(x1[b1-1])-1,2):
    yanshe.append(((x1[b1-1][d]-x1[b1-1][d+1])**2+(y1[b1-1][d]-y1[b1-1][d+1])**2)**0.5*1000)
xy=[kp for kp in range(1,len(yanshe)+1)]
xielv2.append(nihe(xy,yanshe))
xielv3=sum(xielv1)/len(xielv1)
d12=2*bochang*10**-6*D*1000/xielv3
a12=2*bochang*10**-6*D*1000/float(xielv2[0])
p1=d12/m.cos((a/360)*m.pi)
R1=p1/(2*m.pi*m.tan((a/360)*m.pi))
print('实验值，测量值')
print('弹簧平行间距实验值d1',d12,d1,'mm')
print('弹簧平行间距相对误差d1',(abs(d12-d1)/d1)*100,'%')
print('铁丝直径实验值a1',a12,a1,'mm')
print('铁丝直径相对误差a1',(abs(a12-a1)/a1)*100,'%')
print('弹簧竖直间距p',p1,p,'mm')
print('弹簧竖直间距相对误差p',(abs(p1-p)/p)*100,'%')
print('弹簧半径测量值R',2*R1,2*R,'mm')
print('弹簧半径相对误差R',(abs(R1-R)/R)*100,'%')






