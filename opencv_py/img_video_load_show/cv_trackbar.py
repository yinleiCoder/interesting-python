import cv2
import numpy as np
"""
OpenCV中的TrackBar控件：
    createTrackbar(trackbarname, winname, value, count, callback, userdata)
    getTrackbarPos(trackbarname, winname)
"""

cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

def callback():
    pass

# 创建trackbar
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

img = np.zeros((480, 460, 3), np.uint8) # 纯黑图片
while True:
    cv2.imshow('trackbar', img)
    key = cv2.waitKey(10)
    # 读取trackbar的值
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    # 改变背景图片颜色
    img[:] = [b, g, r]
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
