import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mlp
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







