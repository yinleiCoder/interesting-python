import cv2
import numpy as np
"""
多边形逼近apporx与凸包hull：
    多边形逼近：
        approxPolyDP(curve, epsilon, closed)
        epsilon: 精度
        
    凸包:
        convexHull(points, clockwise)
        clockwise: 顺时针绘制
"""
def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == len(points)-1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        else:
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        i += 1

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\hand.png')
print(img.shape)

# 转变为单通道
gary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gary_img.shape)

# 二值化
ret, binary = cv2.threshold(gary_img, 150, 255, cv2.THRESH_BINARY)
print(binary.shape)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# 绘制轮廓
# cv2.drawContours(img, contours, 0, (0, 0, 255), 1)

# 多边形逼近
approx = cv2.approxPolyDP(contours[0], 20, True)
drawShape(img, approx)

# 凸包
hull = cv2.convexHull(contours[0])
drawShape(img, hull)

cv2.imshow('img', img)
# cv2.imshow('bin', binary)
cv2.waitKey(0)