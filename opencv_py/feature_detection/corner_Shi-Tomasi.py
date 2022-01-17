import cv2
import numpy as np
"""
Shi-Tomasi角点检测：
    Harris角点检测算的稳定性和K有关，而K是个经验值，不好设定最佳值。
    而Shi-Tomasi是Harris角点检测的改进。
    goodFeaturesToTrack(img, maxCorners, ..)
    maxCorners:  角点的最大数，值为0表示无限制
    qualityLevel: <1.0的正数，一般在0.01~0.1之间
    minDistance：角之间最小欧式距离，忽略小于此距离的点
    mask: 感兴趣的区域
    blockSize: 检测窗口
    useHarrisDetector: 是否使用Harris算法
    k: 默认是0.04
"""
img = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\chess.png')
#灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_img, 0, 0.01, 10)
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel() # 一维
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('shi-tomasi', img)
cv2.waitKey(0)
