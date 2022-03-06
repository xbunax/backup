import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D
import math as m
import cv2
import tkinter.messagebox
import tkinter
img = cv2.imread('/Users/xbunax/Desktop/资料/创新实验/第二次最终测量/初始.png', cv2.IMREAD_GRAYSCALE)
# size=img.shape
# Y=np.arange(0,size[0],1)
# X=np.arange(0,size[1],1)
# X,Y=np.meshgrid(X,Y)
# fig=plt.figure()
# ax=Axes3D(fig)
# ax.plot_surface(X,Y,img,cmap='rainbow')
# plt.show()
# print('ok')
f = open('初始.csv','w',encoding='utf-8')
scv_write=csv.writer(f)
for i in range(len(img)):
    scv_write.writerow(img[i])
f.close()
wb=csv.reader(open('初始.csv','r'))
contant=[]
a1=[]
bochang=650*10**-9#m波长
fangdalv=0.5
a2=10.5#铁丝之间夹脚
p=0.75#弹簧间距真实值
k=0.00038#N/mm
def pailiezuhe(x):
    return int(((len(x)-1)*len(x)*(len(x)-2))/6)
def suiji(a):
    x=[[] for o in range(int(pailiezuhe(a)))]
    o=0
    for j in range(len(x)):
        for m in range(len(x)):
            for n in range(len(x)):
                if j!=m and j!=n and m!=n:
                    x[o].append(j)
                    x[o].append(m)
                    x[o].append(n)
        o+=1
    return x
def dingbiao(xiangsu,changdu):
    bili=(xiangsu/changdu)#a是像素个数 x是对应长度
    return bili
for line in wb:
    for f in range(len(line)):
        a1.append(float(line[f]))
    contant.append(max(a1))
    a1=[]
def center(a):
    b=[]
    for i in range(2500,3500):
        if contant[i]<=200:
            b.append(i)
    return sum(b)/len(b)
n0=len(contant)/2#中心条纹
D=45*10**-2#m到ccd距离
a=0.195*10**-3#m铁丝直径
xiangsu=250#定标像素
changdu=2.5*10**-3#m定标长度
def yanshe(D,bochang,a,n):
    x1=[]
    xn=bochang*D/a
    xn1=xn*dingbiao(xiangsu,changdu)
    n2=int((len(contant)-n0)/xn1)
    for i in range(1,n2):
        if n == 1:  # 向右循环
            x1.append(n0+i*xn1)
        if n == 2 :#向左循环
            x1.append(n0-i*xn1)
    if min(x1)<0 or max(x1)>len(contant):
        print('something wrong')
    return x1
def ganshe(x1):
    xn = bochang * D / a
    xn1 = xn * dingbiao(xiangsu, changdu)
    n2 = int(n0 / xn1)
    x2=[[] for p in range(len(x1))]
    x3=[[] for p in range(len(x1))]
    o=0
    for h in range(len(x1)-1):
        for l in range(int(x1[h]),int(x1[h+1])):
            if contant[l-1]>contant[l]<contant[l+1]:
                x2[o].append((l,contant[l]))

        x2[o]=sorted(x2[o],key=lambda x:x[1],reverse=False)
        x3[o].append(x2[o][1][0])
        x3[o].append(x2[o][2][0])
        x3[o].append(x2[o][3][0])
            #if len(x2[0])>=2:
             #   break
        #for m in range(int(h+1),1,-1):
         #   if contant[m-1]>contant[m]<contant[m+1]:
          #      x2[o].append(m)
           # if len(x2[o])>=4:
            #    break

        o+=1
    return x3
xo1=yanshe(D,bochang,a,1)
xo2=yanshe(D,bochang,a,2)
for i in range(6):
    del xo1[i]
# xo1=sorted(xo1)
# for i in range(len(xo1)-1,len(xo1)-20,-2):#5、4圈左28  3圈左20  2圈右6 1圈右5
#     del xo1[i]
# print(len(xo1))
x21=ganshe(xo1)
# y2=[]
# for i in xo1:
#     y2.append(contant[int(i)])
# y2=np.array(y2)
# x2=np.array(xo1)
# plot1=plt.scatter(x2,y2)
# x=[i for i in range(1,len(contant)+1)]
# y1=np.array(contant)
# x1=np.array(x)
# plot1=plt.plot(x1,y1,alpha=0.5)
# plt.show()
def func(x,a,b):
    return a*x+b
def nihe(x,y):
    x0=np.array(x)
    y0=np.array(y)
    a10,b10 = optimize.curve_fit(func,x0,y0)[0]
    return a10
def ganshenihe(a,a12):
    xz=[[] for p in range(len(a))]
    xn=[]
    for g in range(len(a)):
        for j in a[g]:
            p=(m.cos(a12*m.pi/360)*2*abs(j-n0))/dingbiao(xiangsu,changdu)
            xz[g].append(p*1000)
        x=[o for o in range(1,len(xz[g])+1)]
        if len(x) == len(xz[g]) and len(x)!=0:
            xn.append(nihe(x,sorted(xz[g])))
    return sum(xn)/len(xn)
def yanshenihe(y,a):
    x=[i for i in range(1,len(y)+1)]
    y1=[]
    for j in y:
        o=(m.cos(a*m.pi/360)*2*abs(j-n0))/dingbiao(xiangsu,changdu)
        y1.append(o*1000)
    return nihe(x,y1)
a2=10.5#铁丝之间夹角
x211=[]
x212=[]
# for l in range(len(x21)):
#   if l>2:
#        x211.append(x21[l])
# for l in range(len(x22)):
#     if l>2:
#         x212.append(x22[l])
def zuixiaopiancha(x):
    a1=[]
    a2=[]
    for k in range(len(x)):
        for j in range(len(x[k])):
            k=ganshenihe(x[k][j],a2)
            d12 = 2 * bochang * 10 ** 6 * D / float(k)
            p1 = d12 / m.cos((a2 / 360) * m.pi)  # 弹簧竖直间距
            a1.append(p1)
            a2.append(abs(p1-p)/p)
    a1=sorted(a1)
    a2=sorted(a2)
    return a1[0],a2[0]
xielv2=ganshenihe(x21,a2)
xielv1=yanshenihe(xo1,a2)
d12=2*bochang*10**6*D/float(xielv2)
a12=2*bochang*10**6*D/float(xielv1)
p1=d12/m.cos((a2/360)*m.pi)#弹簧竖直间距
R1=p1/(2*m.pi*m.tan((a/360)*m.pi))
xiangduiwucha=100*abs(p1-p)/p
p1=round(p1,2)
xiangduiwucha=round(100*abs(p1-p)/p,2)
# print(xo1)
p11='弹簧间距结果{}mm\n相对误差{}%'.format(p1,xiangduiwucha)
# window=tkinter.Tk()
# window.geometry(600*600)
# def hit():
#     tkinter.messagebox.showinfo(title='结果',message=p11)
# b=tkinter.Button(window,text='ok',command=hit().pack())
# tkinter.mainloop()
tkinter.messagebox.showinfo('结果',p11)
print('弹簧间距',p1,'mm')
print('相对误差',100*abs(p1-p)/p,'%')








