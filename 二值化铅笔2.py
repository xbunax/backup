import numpy as np
from PIL import Image
import skimage.io
import cv2
import os
import matplotlib.pyplot as plt
path1='/Users/xbunax/Desktop/cupt/20年/10石墨导线/导线表征/3layer.jpg'
b=cv2.imread(path1)
#print(b[365])
m=np.arange(0,len(b[365]))
# plt.figure()
# plt.plot(m,b[365])
# #v=sum(b[365])/len(b[365])
# plt.show()
v=123
#ret1,th1 = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret1,th1 = cv2.threshold(b,v,255,cv2.THRESH_BINARY)
a=th1.flatten()
n=0
cv2.imshow('img',th1)
for i in range(len(a)):
    if a[i]==0:
        n+=1
print((len(a)-n)/len(a),n,len(a),b.shape)
cv2.waitKey(0)







