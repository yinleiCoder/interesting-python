import cv2
import numpy as np
"""
Harris角点检测：
    光滑地区，无论向哪里移动，衡量系数不变
    边缘地址，垂直边缘移动时，衡量系数变化剧烈
    在交点处，往哪个方向移动，衡量系数都变化剧烈
    cornerHarris(img, dst, blockSize, ksize, k)
    blockSize:  检测窗口大小
    ksize: Sobel的卷积核
    k：权重系数，经验值，一般取0.02~0.04之间
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')
#灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blockSize = 2
ksize = 3
k = 0.04
dst = cv2.cornerHarris(gray_img, blockSize, ksize, k)
# harris角点展示
img[dst > 0.01*dst.max()] = [0, 0, 255]

cv2.imshow('harris', img)
cv2.waitKey(0)
