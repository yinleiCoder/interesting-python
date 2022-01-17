import cv2
import numpy as np

"""
ORB(Oriented FAST and Rotated BRIEF)特征检测:
    ORB可以做到实时检测。
    ORB = Oriented FAST + Rotated BRIEF
    FAST: 可以做到特征点的实时检测
    BRIEF: 对已检测到的特征点进行描述，加快了特征描述符建立的速度，同时也极大的降低了特征匹配的时间。
    
使用ORB的步骤：
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(img, mask)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')
#灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(gray_img, None)
# print(des)
cv2.drawKeypoints(gray_img, kp, img)

cv2.imshow('orb', img)
cv2.waitKey(0)