import cv2
import numpy as np
"""
SIFT(Scale-Invariant Feature Transform)关键点检测：
    Harris角点具有旋转不变的特性，但缩放后，原来的角可能就不是角点了。

使用SIFT步骤：
    创建SIFT对象
    进行检测：kp = sift.detect(img,...)
    绘制关键点：drawKeypoints(gray, kp, img)

关键点和描述子：
    关键点：位置、大小、方向
    关键点描述子： 记录了关键点周围对其有贡献的像素点的一组向量值，其不受仿射变换、光照变换的影响。

计算SIFT描述子：
    kp, des = sift.compute(img, kp)
    描述子的作用就是进行特征匹配。

同时计算关键点和描述：[最常用]
    kp, des = sift.detectAndCompute(img,....)
    mask: 对img中哪个区域进行计算
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')
#灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray_img, None)
print(des)
cv2.drawKeypoints(gray_img, kp, img)

cv2.imshow('sift', img)
cv2.waitKey(0)