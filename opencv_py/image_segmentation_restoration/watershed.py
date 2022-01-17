import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
分水岭法：
    缺点：图像存在过多的极小区域而产生许多小的积水盆

步骤：
    标记背景
    标记前景
    标记未知域
    进行分割
        watershed(img, masker)
        masker：前景、背景设置不同的值用以区分他们

矩离变换:非0值到最近的0值之间的距离
    distanceTransform(img, distanceType, maskSize)
    distanceType: DIST_L1, DIST_L2
    maskSize: L1用3， L2用5
连通域：非0图像的连通域
    connectedComponents(img, connectivity...)
    connectivity: 4, 8(默认)上下左右等几个方向
"""
# 获取背景
# 1. 通过二值法获得黑白图片
# 2. 通过形态学获取背景
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\water_coins.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 开运算
kernel = np.ones((3, 3), np.int8)
open1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 膨胀
bg = cv2.dilate(open1, kernel, iterations=1)

# 获取前景物体
dist = cv2.distanceTransform(open1, cv2.DIST_L2, 5)
ret, fg = cv2.threshold(dist, 0.7*dist.max(), 255, cv2.THRESH_BINARY)

plt.imshow(fg, cmap='gray')
plt.show()

# 获取未知区域(图像相减)
fg = np.uint8(fg)
unknow = cv2.subtract(bg, fg)

# 创建连通域
ret, marker = cv2.connectedComponents(fg)

marker = marker + 1
marker[unknow==255] = 0

# 图像分割
result = cv2.watershed(img, marker)
img[result == -1] = (0, 0, 255)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('unknow', unknow)
cv2.imshow('bg', bg)
cv2.waitKey(0)