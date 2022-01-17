import cv2
"""
OpenCV创建显示窗口:
    namedWindow()
    imshow()
    destroyAllWindows()
    resizeWindow()
"""

cv2.namedWindow('new', cv2.WINDOW_NORMAL)
cv2.resizeWindow('new', 640, 480)
cv2.imshow('new', 0)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()




