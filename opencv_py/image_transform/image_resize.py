import cv2
import numpy as np
"""
OpenCV图像基本变换: 图像缩放
    resize(src, dst, dsize, fx, fy, interpolation)
    fx: x轴的缩放因子
    fy: y轴的缩放因子
    interpolation: 插值算法
        INTER_NEAREST: 邻近插值，速度块，效果差
        INTER_LINEAR: 双线性插值，原图中的4个点
        INTER_CUBIC: 三次插值，原图中的16个点
        INTER_AREA: 效果最好
"""
unicom = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')

# new = cv2.resize(unicom, (181, 320))
new = cv2.resize(unicom, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

print(unicom.shape)

cv2.imshow('unicom', unicom)
cv2.imshow('unicom new', new)
cv2.waitKey(0)