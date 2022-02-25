import cv2
import numpy as np

"""
图像拼接：
    准备的素材需要有相关性。
    
图片合并的步骤：
    读文件并重置尺寸
    根据特征点和计算描述子，得到单应性矩阵
    图像变换
    图像拼接并输出图像
"""
def get_homo(img1, img2):
    # 创建特征转换对象
    sift = cv2.xfeatures2d.SIFT_create()
    # 通过特征转换对象获得特征点和描述子
    k1, d1 = sift.detectAndCompute(img1, None)
    k2, d2 = sift.detectAndCompute(img2, None)
    # 创建特征匹配器
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(d1, d2, k=2)
    # 进行特征匹配
    verify_matches = []
    # 过滤特征，找出有效的特征匹配点
    for m1, m2 in matches:
        if m1.distance < 0.8 * m2.distance:
            verify_matches.append(m1)
    if len(verify_matches) >= 4:
        img1_pts = []
        img2_pts = []
        for m in verify_matches:
            img1_pts.append(k1[m.queryIdx].pt)
            img2_pts.append(k2[m.trainIdx].pt)
        img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 5.0)
        return H
    else:
        print('Not enough matches')
        exit()

def stitch_image(img1, img2, H):
    # 获取每张图片的4个角点
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    # 对图片进行变换(单应性矩阵使图进行旋转，然后平移)
    img1_transform = cv2.perspectiveTransform(img1_dims, H)
    # print(img1_dims)
    # print(img1_transform)
    # 创建一张大图，将2张图拼接
    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)
    # print(result_dims)
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    # 平移的距离
    transform_dist = [-x_min, -y_min]
    transform_array = np.array([[1, 0, transform_dist[0]],
                                [0, 1, transform_dist[1]],
                                [0, 0, 1]])
    # 投影变换
    result_img = cv2.warpPerspective(img1, transform_array.dot(H), (x_max-x_min, y_max-y_min))
    # 拼接
    result_img[transform_dist[1]:transform_dist[1]+h2,
                transform_dist[0]:transform_dist[0]+w2] = img2
    return result_img

# 将素材设置为固定的大小
right_img = cv2.imread(r"E:\PycharmProjects\funnyPython\opencv_py\data\imgs\connect_left.jpg")
left_img = cv2.imread(r"E:\PycharmProjects\funnyPython\opencv_py\data\imgs\connect_right.jpg")
right_img = cv2.resize(right_img, (640, 480))
left_img = cv2.resize(left_img, (640, 480))
inputs = np.hstack((left_img, right_img))
cv2.imshow('input img', inputs)
cv2.waitKey(0)
# 寻找特征点、描述子，计算单应性矩阵
H = get_homo(left_img, right_img)
# 根据单应性矩阵对图像进行变换，然后平移, 拼接
result = stitch_image(left_img, right_img, H)

cv2.imshow('result', result)
cv2.waitKey(0)