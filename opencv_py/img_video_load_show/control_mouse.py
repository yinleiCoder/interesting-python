import cv2
import numpy as np
"""
OpenCV控制鼠标：
    setMouseCallback(winname, callback, userdata) 
    callback(event, x, y, flags, userdata)   
    flags: 鼠标键及组合键
"""
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)

cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 360)

#设置鼠标回调
cv2.setMouseCallback('mouse', mouse_callback, '123')
img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)
    if key & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
