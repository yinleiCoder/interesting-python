import cv2
import numpy as np
"""
特征匹配：暴力特征匹配法
    使用第一组中的每个特征的描述子与第二组中的所有特征描述子进行匹配。
    计算他们之间的差距，然后将最接近一个匹配返回。
    
特征匹配方法：
    BF(Brute-Force)暴力特征匹配方法
    FLANN最快邻近区特征匹配方法
    
OpenCV特征匹配步骤：
    创建匹配器，BFMatcher(normType, crossCheck)
        normType: NORM_L1, NORM_L2, HAMMING1...
        crossCheck: 进行交叉匹配，默认false
    进行特征匹配, bf.match(des1, des2)
        参数为SIFT、SURF、OBR等计算的描述子，对2幅图的描述子进行计算
    绘制匹配点，cv2.drawMatches(img1, kp1, img2, kp2..)
"""
img1 = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
img2 = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao2.png')
#灰度化
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray_img1, None)
kp2, des2 = sift.detectAndCompute(gray_img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1,)
match = bf.match(des1, des2)
result = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('bf_match', result)
cv2.waitKey(0)