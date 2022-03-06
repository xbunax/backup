import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlwt
from matplotlib.pyplot import MultipleLocator
size=20
a=0.6
def percolate(size=100,a=0.593):
    k=np.zeros((size+1,size+1))
    M=[]
    N=size**2
    point=N*a
    while True:
        x=random.randint(1,size-1)
        y=random.randint(1,size-1)
        if [x,y] not in M:
            M.append([x,y])
        if len(M)==point:
            break
    for i in range(0,len(M)):
        x1=M[i][0]
        y1=M[i][1]
        k[x1][y1]=1
    return k
k=percolate(20,0.6)
# workbook = xlwt.Workbook(encoding = 'utf-8')
# worksheet = workbook.add_sheet('My Worksheet')
# for i in range(len(k)):
#     for j in range(len(k[i])):
#         worksheet.write(i,j,k[i][j])
workbook.save('percolation.xls')
colors=['white','black']
cmap=mpl.colors.ListedColormap(colors)
x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(1)
plt.figure()
ax=plt.gca()
plt.imshow(k,cmap=cmap)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlabel('y')
plt.ylabel('x')
plt.show()
# m1 = []
# m2 = []
# m3 = []
# def find(x,y):
#     if k[x][y]==1:
#         if ([x,y] not in m1) and ([x,y] not in m2) and ([x,y] not in m3):
#           if k[x][y+1]==1 and (x<size-1 or y<size-1):
#             m1.append([x+1,y])
#             print('m1',m1)
#             find(x,y+1)
#           if k[x+1][y]==1 and (x<size-1 or y<size-1):
#             m2.append([x+1,y])
#             print('m2',m2)
#             find(x+1,y)
#           if k[x-1][y]==1 and (x<size-1 or y<size-1):
#             m3.append([x-1,y])
#             find(x-1,y)
#             print('m3',m3)
#         else:
#             return 'repeat'
#     elif k[x][y]!=1:
#         return 'not find'
# def rfind(x,y):
#     if k[x][y]==1:
#         if k[x][y+1]==1:
#             print(x,y+1,'rfind')
#             rfind(x,y+1)
#         else:
#             return 1
#     else:
#         return 'not find'
# def upfind(x,y):
#     if k[x][y]==1:
#         if k[x-1][y]==1:
#             print(x-1,y,'2')
#             upfind(x-1,y)
#         else:
#             return 2
#     else:
#         return 'not find'
# def downfind(x,y):
#     if k[x][y]==1:
#         if k[x+1][y]==1:
#             print(x+1,y,'3')
#             downfind(x+1,y)
#         else:
#             return 3
#     else:
#         return 'not find'
# def search(x,y):
#     if k[x][y]==1:
#         while rfind(x,y)!=1:
#             rfind(x,y)
#         while upfind(x,y)!=2 or rfind(x,y)==1 or downfind(x,y)==3:
#             upfind(x,y)
#         while downfind(x,y)!=3 or upfind(x,y)==2 or rfind(x,y)==1:
#             downfind(x,y)
#         if rfind(x,y)==1 and upfind(x,y)==2 and downfind(x,y)==3:
#             return 'break'
#         if x==size-1 or y==size-1:
#             return 'find'
#     else:
#         return '不满足条件'






