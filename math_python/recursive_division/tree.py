from turtle import *
import math
"""
分形看起来并不像我们在几何学中认识的规则形状，他们的形状蜿蜒曲折，这使得他们成了模拟自然现象的绝佳模型。
事实上，科学家们用分形来模拟一切：从心脏动脉到地震，再到大脑的神经元。
他们展示了通过一遍遍运用简单的规则，以越来越小的比例反复画出图案，从而得到复杂得令人惊奇的图形。

Coastline Paradox：随着尺子的长度趋近于0，海岸线的长度会趋近于无穷。


https://docs.python.org/zh-cn/3/library/turtle.html?highlight=turtle#module-turtle
"""


def gen_heart_number(start=0, end=0, step=1.0):
    assert start <= end
    index = start
    while index < end:
        yield round(index, 3)
        index += step

def draw_curve():
    for i in range(200):
        right(1)
        forward(1)

def draw_heart():
    pensize(3)
    color('black', 'red')
    begin_fill()
    left(140)
    forward(113)
    draw_curve()
    left(120)
    draw_curve()
    forward(112)
    end_fill()
    hideturtle()
    setheading(270)
    penup()
    forward(50)
    pendown()
    write("I Love You", True, align="center", font=('Arial', 14, 'bold'))
    done()

if __name__ == '__main__':
    title('heart')
    draw_heart()