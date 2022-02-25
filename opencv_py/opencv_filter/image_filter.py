import cv2
import numpy as np
"""
OpenCV: 图像滤波

滤波的作用：一幅图像通过滤波器得到另一幅图像。
其中滤波器又称为卷积核，滤波的过程称为卷积。
实际就是小矩阵与原始图像的乘积。

卷积核的大小：一般为奇数，如3x3、5x5、7x7等
为奇数，一方面是增加padding的原因，另一方面保证锚点在中间，防止位置发生偏移。
深度学习中，卷积核越大，看到的信息（感受野）越多，提取的特征越好，同时计算量也就越大。

锚点：正中心的点，防止信息的偏差

边界扩充: 当卷积核>1且不进行边界扩充，输出的尺寸将相应缩小。当卷积核以标准方式进行边界扩充，则输出数据的空间尺寸将与输入相等。
N = （W - F + 2P） / S + 1
N: 输出图像大小
W：源图大小
F：卷积核大小
P：扩充尺寸
S：步长大小

低通滤波：某个值低于当前阈值可以通过，可去除噪音或平滑图像。如均值滤波、方盒滤波、高斯滤波、中值滤波、双边滤波
高通滤波：某个值高于当前阈值可以通过，可帮助查找图像的边缘。如Sobel(索贝尔*高斯)、Scharr(沙尔)、Laplacian(拉普拉斯)

图像卷积：
    filter2D(src, ddepth, kernel, anchor, delta, borderType)
"""

img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinlei.jpg')

"""
    1 | 1 1 1 1 1 |
K = ——| 1 1 1 1 1 |
    25| 1 1 1 1 1 |
      | 1 1 1 1 1 |
      | 1 1 1 1 1 |
"""
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel=kernel,)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)