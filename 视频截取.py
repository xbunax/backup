import cv2
import os
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"
    else:
        print
        "---  There is this folder!  ---"
file = "/Users/xbunax/Desktop/资料/创新实验/sanquan1"
mkdir(file)
vc = cv2.VideoCapture('/Users/xbunax/Desktop/资料/创新实验/2019 11 21/sanquan4.mp4')  # 读入视频文件
c = 1
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
timeF = 20  # 视频帧计数间隔频率
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite('/Users/xbunax/Desktop/资料/创新实验/sanquan1' + str(c) + '.jpg', frame)  # 存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()
