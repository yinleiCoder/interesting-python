import cv2
"""
OpenCV加载显示图片:
    im == image
    imread(path, flag)
"""

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(r"E:\PycharmProjects\funnyPython\opencv_py\data\imgs\yinzihao.png")
cv2.imshow('img', img)

key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()