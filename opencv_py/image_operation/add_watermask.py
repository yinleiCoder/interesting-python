import cv2
import numpy as np
"""
给图片添加水印
"""
unicom_person = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\unicom_person.jpg')
# unicom_logo = cv2.imread(r'E:\PycharmProjects\funnyPython\opencv_py\data\imgs\china_unicom.png')
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]
mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

m = cv2.bitwise_not(mask)

roi = unicom_person[0:200, 0:200]
tmp = cv2.bitwise_and(roi, roi, mask=m)

dst = cv2.add(tmp, logo)

unicom_person[0:200, 0:200] = dst

cv2.imshow('unicom', unicom_person)
cv2.imshow('dst', dst)
cv2.imshow('tmp', tmp)
cv2.imshow('mask', mask)
cv2.imshow('mask', m)
cv2.imshow('logo', logo)
cv2.waitKey(0)
