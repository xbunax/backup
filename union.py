import numpy as np
import xlrd
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import copy
def diction(data_list):
    result = {}
    num = 1
    for i in data_list:
        result[i] = num
        num += 1
    return result
def weight(dict,key4):
    m=[]
    for i in dict.keys():
        m.append(dict.get(i))
    return m.count(key4)
def union(dict,key1,key2):
    if weight(dict,key1)>=weight(dict,key2):
        for i in dict:
            if dict[i]==dict[key2]:
                dict[i]=key1
    elif weight(dict,key1)<weight(dict,key2):
        for i in dict:
            if dict[i]==dict[key1]:
                dict[i]=key2
    return dict
def in_the_same_set(dict,key1,key2):
    if dict[key1]==dict[key2]:
        return True
# def import_excel_matrix(path):
#     table = xlrd.open_workbook(path).sheets()[0] # 获取第一个sheet表
#     row = table.nrows # 行数
#     col = table.ncols # 列数
#     k= np.zeros((row, col)) # 生成一个nrows行*ncols列的初始矩阵
#     for i in range(col): # 对列进行遍历
#         k[:,i]=table.col_values(i)
#     return k
# data_file = '/Users/xbunax/PycharmProjects/SHIYAN/percolation.xls' # Excel文件存储位置
# perdata=import_excel_matrix(data_file)
size=20
p=0.4
perdata=np.zeros((size+1,size+1))
location=[]
while np.sum(perdata==1)<=p*size**2:
    x=random.randint(1,size-1)
    y=random.randint(1,size-1)
    if perdata[x][y]!=1:
        perdata[x][y]=1
        location.append((x,y))
colors=['white','black']
cmap=mpl.colors.ListedColormap(colors)
plt.imshow(perdata,cmap=cmap)
plt.show()
a=diction(location)
for i in a:
    if (i[0]+1,i[0]) in a.keys():
        union(a,(i[0]+1,i[0]),i)
    if (i[0],i[0]+1) in a.keys():
        union(a,(i[0],i[0]+1),i)
    if (i[0]-1,i[0]) in a.keys():
        union(a,(i[0]-1,i[0]),i)
    if (i[0],i[0]-1) in a.keys():
        union(a,(i[0],i[0]-1),i)
father=[]
Child=[]
for i in a:
    if a[i]==i:
        father.append(i)
perdata1=copy.deepcopy(perdata)
for i in father:
    for j in a:
        if a[j]==i:
            perdata[j[0]][j[1]]=father.index(i)+2
    plt.imshow(perdata)
    perdata=perdata1
    plt.show()













