import cv2
import numpy as np
"""
OpenCV实现鼠标绘制基本图形
"""

curshape = 0
start_pos = (0, 0)
def mouse_callback(event, x, y, flags, userdata):
    global start_pos
    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        start_pos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if curshape == 0:
            cv2.line(img, start_pos, (x, y), (0, 0, 255))
        elif curshape == 1:
            cv2.rectangle(img, start_pos, (x, y), (0, 0, 255))
        elif curshape == 2:
            a = (x - start_pos[0])
            b = (y - start_pos[1])
            r = int((a**2 + b**2)**0.5)
            cv2.circle(img, start_pos, r, (0, 0, 255))


cv2.namedWindow("drawshape", cv2.WINDOW_NORMAL)

cv2.setMouseCallback("drawshape", mouse_callback, "123")

img = np.zeros((480, 640, 3), np.uint8)
while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    elif key == ord('l'):# line
        curshape = 0
    elif key == ord('r'):# rectangle
        curshape = 1
    elif key == ord('c'):  # circle
        curshape = 2
