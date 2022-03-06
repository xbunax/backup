import cv2
path='/Users/xbunax/Downloads/IMG_0388.jpg'
data=cv2.imread(path,0)
ret,thresh1 = cv2.threshold(data,127,255,cv2.THRESH_BINARY)
cv2.imshow('1',thresh1)
cv2.waitKey(0)

