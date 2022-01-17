import cv2
import numpy as np
"""
特征匹配: FLANN特征匹配法
    在进行批量特征匹配时，FLANN速度更快，由于它使用的是邻近近似值，所以精度较差。        
    
FLANN特征匹配步骤：
    创建匹配器，FlannBasedMatcher(...)
        index_params字典: 匹配算法KDTREE、LSH 
        search_params字典: 指定KDTREE算法中遍历树的次数
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
    进行特征匹配, flann.match/knnMatch(...)
        参数为SIFT、SURF、OBR等计算的描述子，对2幅图的描述子进行计算
        k, 表示取欧式距离最近的前k个关键点
        返回的是匹配的结果DMatch对象(
                        distance, 描述子之间的距离越低越好。
                        queryIdx，第一个图像的描述子索引值。
                        trainIdx, 第二个图的描述子索引值,
                        imgIdx, 第二个图的索引值)
    绘制匹配点，cv2.drawMatches/cv2.drawMatchesKnn(img1, kp1, img2, kp2..)

图像查找：
    特征匹配 + 单应性矩阵（图像自动转正）
"""
img1 = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png')
img2 = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao2.png')
#灰度化
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray_img1, None)
kp2, des2 = sift.detectAndCompute(gray_img2, None)

index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matchs = flann.knnMatch(des1, des2, k=2)
good=[]
for i , (m, n) in enumerate(matchs):
    if m.distance < 0.7 * n.distance:
        good.append(m)

if len(good) > 4:# 必须至少匹配到4个顶点
    # 查找单应性矩阵
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    H, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
    # 计算透视变换
    h, w = img1.shape[:2]
    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)
    cv2.polylines(img2, [np.int32(dst)], True, (0, 0, 255))
else:
    exit()
result = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)

cv2.imshow('flann_match', result)
cv2.waitKey(0)