import cv2
import numpy as np
"""
外接矩形：
    最小外接矩形：
        RotatedRect = minAreaRect(points)
        RotatedRect: 包括x,y,width,height,angle
    最大外接矩形:
        Rect = boundingRect(array)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\hello.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)