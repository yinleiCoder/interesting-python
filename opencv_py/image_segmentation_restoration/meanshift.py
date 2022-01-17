import cv2
import numpy as np
"""
MeanShift分割法：
    严格来说不是用来对图像分割的，而是在色彩层面的平滑滤波
    它会中和色彩分布相近的颜色，平滑色彩细节，侵蚀掉面积较小的颜色区域
    它以图像上任一点P为圆心，半径为sp,色彩幅值为sr进行不断的迭代
    pyrMeanShiftFiltering(img, double sp, double sr, maxLevel=1, termcrit=TermCriteria...)
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\flower.png')
mean_img = cv2.pyrMeanShiftFiltering(img, 20, 30)

# canny找到边缘
img_canny = cv2.Canny(mean_img, 150, 300)
contours, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)


cv2.imshow('img', img)
cv2.imshow('img_canny', img_canny)
cv2.imshow('mean_img', mean_img)
cv2.waitKey()
