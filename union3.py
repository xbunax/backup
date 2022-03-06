class UnionFindSet(object):
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        """使用递归的方式来查找父节点

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if(node != father):
            if father != self.father_dict[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
size=20
for p in np.arange(0.5,0.62,0.01):
    perdata=np.zeros((size+1,size+1))
    location=[]
    lista=[]
    for x in range(size):
        for y in range(size):
            lista.append((x,y))
    percolate=UnionFindSet(lista)
    while np.sum(perdata==1)<=p*size**2:
        x=random.randint(1,size-1)
        y=random.randint(1,size-1)
        if perdata[x][y]!=1:
            perdata[x][y]=1
            if perdata[x][y+1]==1:
                percolate.union((x,y),(x,y+1))
            if perdata[x][y-1]==1:
                percolate.union((x,y),(x,y-1))
            if perdata[x-1][y]==1:
                percolate.union((x,y),(x-1,y))
            if perdata[x+1][y]==1:
                percolate.union((x,y),(x+1,y))
    colors=['white','black','red']
    keys1=[]
    values1=[]
    a=[]
    for i in percolate.size_dict:
        if percolate.size_dict[i]>=3:
            values1.append(i)
    for i in percolate.father_dict:
        if percolate.father_dict[i] in values1:
            location.append(i)
    for j in location:
        perdata[j[0]][j[1]]=2
    if abs(len(location)/(size-1)**2-0.59)<=0.02:
        print('p',p)
        print(len(location)/(size-1)**2)
        cmap=mpl.colors.ListedColormap(colors)
        plt.imshow(perdata,cmap=cmap)
        plt.show()