import cv2
import numpy as np

"""
SURF(Speeded-Up Robust Features)特征检测:
    SIFT特征点检测的准确，描述子也描述的很详细，但其最大的问题是速度慢，因此才有SURF

使用SURF的步骤：
    surf = cv2.xfeatures2d.SURF_create()
    kp, des = surf.detectAndCompute(img, mask)
surf需要windows编译的时候勾选，因为它是有版权保护的。
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')
#灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
kp, des = surf.detectAndCompute(gray_img, None)
# print(des)
cv2.drawKeypoints(gray_img, kp, img)

cv2.imshow('surf', img)
cv2.waitKey(0)