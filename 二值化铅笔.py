import numpy as np
from PIL import Image
import skimage.io
import cv2
import os
import matplotlib.pyplot as plt
path1='/Users/xbunax/Desktop/cupt/20年/10石墨导线/表征/IMG_5433的副本.JPG'
b=cv2.imread(path1)
#print(b[365])
m=np.arange(0,len(b[365]))
# plt.figure()
# plt.plot(m,b[365])
# #v=sum(b[365])/len(b[365])
# plt.show()
v=124
#ret1,th1 = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
def func(v,b):
    ret1,th1 = cv2.threshold(b,v,255,cv2.THRESH_BINARY)
    a=th1.flatten()
    n=0
#cv2.imshow('img',th1)
    for i in range(len(a)):
        if a[i]==0:
            n+=1
    #print(ret1)
    return (len(a)-n)/len(a)
for v in range(110,170):
    if func(v,b)<0.59:
        print(func(v,b),v)
    print(v)
#print((len(a)-n)/len(a),n,len(a),b.shape)
#cv2.waitKey(0)







