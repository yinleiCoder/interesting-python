import cv2
import numpy as np
"""
图像的仿射变换：图像旋转、缩放、平移的总称
    warpAffine(src, M, dsize, flags, mode, value)
    M: 变换矩阵 getRotationMatrix2D(center, angle, scale)
               getAffineTransform(src[], dst[]) 根据3个点确定变换的位置
    dsize: 输出尺寸
    flag: 与resize中的插值算法一致
    mode: 边界外推法标志
    value:填充边界的值
    
平移矩阵：
    矩阵中的每个像素由(x,y)组成
    因此，其变换矩阵是2*2的矩阵
    平移向量为2x1的向量，所在平移矩阵为2x3矩阵
"""
brother = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
h, w, ch = brother.shape

# M = np.float32([[1, 0, 100], [0, 1, 100]])# 手动构建变换矩阵(单位矩阵+x,y平移距离)
# M = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.5)
src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
M = cv2.getAffineTransform(src, dst)
new = cv2.warpAffine(brother, M, (w, h))

cv2.imshow('brother', brother)
cv2.imshow('new', new)
cv2.waitKey(0)

