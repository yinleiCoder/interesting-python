import cv2
import numpy as np

"""
图像的透视变换：将一种坐标系变换为另一种坐标系
    OCR识别发票，手机拍的不一定方向水平，通过透视变换，将图片沿着水平变换然后再提取信息
    warpPerspective(img, M, dsize....)
    M: 变换矩阵 getPersectiveTransform(src, dst) 根据4个点确定变换的位置(图形的4个角)
    dsize: 目标图像大小
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\prespective_test.jpg')
print(img.shape)

# 图片的4个顶点(角)需要自己去猜
src = np.float32([[100, 1100], [3024, 1100], [0, 4000], [2500, 3900]])
dst = np.float32([[0, 0], [3024, 0], [0, 4032], [4032, 3024]])
M = cv2.getPerspectiveTransform(src, dst)
new = cv2.warpPerspective(img, M, (4032, 3024))

cv2.imshow('brother', img)
cv2.waitKey(0)

