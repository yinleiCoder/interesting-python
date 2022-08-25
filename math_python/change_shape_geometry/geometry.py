"""
变换函数：
    平移：processing中，平移对象实际移动网格本身，而对象的坐标保持不变。translate(x, y)
            例如平移画布的原点到网格中央
            translate(width/2,height/2)
    旋转: processing中，旋转将网格绕原点(0,0)旋转，rotate(弧度) radians(角度)

使对象动画化：

"""

# t = 0
#
#
# def setup():
#     size(600, 600)
#
#
# def draw():
#     global t
#     background(255)
#     translate(width / 2, height / 2)
#     rotate(radians(t))
#     for i in range(12):
#         rect(200, 0, 50, 50)
#         rotate(radians(360 / 12))
#     t += 0.1
