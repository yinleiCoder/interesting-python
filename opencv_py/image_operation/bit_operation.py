import cv2
import numpy as np
"""
图像位运算：
非操作
    bitwise_not(img)
与操作：
    bitwise_and(img1, img2)
或操作：
    bitwise_or(img1, img2)
异或操作：
    bitwise_xor(img1, img2)
"""

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)
img[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

# 非操作
new_img = cv2.bitwise_not(img)

# 与操作
new_img = cv2.bitwise_and(img, img2)

# 或操作
new_img = cv2.bitwise_or(img, img2)

# 异或操作
new_img = cv2.bitwise_xor(img, img2)

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('not', new_img)
cv2.waitKey(0)
