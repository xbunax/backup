import cv2
import csv
img = cv2.imread('/Users/xbunax/Desktop/资料/创新实验/最后第四次测量/半圈1.png', cv2.IMREAD_GRAYSCALE)
f = open('实验1.csv','w',encoding='utf-8')
scv_write=csv.writer(f)
for i in range(len(img)):
    scv_write.writerow(img[i])
f.close()