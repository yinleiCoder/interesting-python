import cv2
import numpy as np

"""
特征检测的应用场景：
    图像搜索。如百度搜图
    拼图游戏。
    图像拼接，将2长有关联的图拼接到一起。【全景图像】

拼图方法：
    寻找特征
    特征是唯一的
    可追踪的
    能比较的
平坦部分很难找到它在原图中的位置，
边缘相比平坦要好找一些，但也不能一下确定，
角点可以一下就找到其在原图的位置。

特征：
图像特征就是指有意义的图像区域，具有独特性、易于识别性，比如角点、斑点以及高密度区。

角点：
在特征中最重要的是角点，灰度梯度的最大值对应的像素，两条线的交点，极值点(一阶导数最大值，但二阶导数为0)
"""