"""
作图法解方程:
    解三次方程, 但是你可能会怀疑，x^3应该出现3个解，蛮力法找到这样一个解，
    无法确定是否存在其他的解，也无法找到他们的值。此时，可以通过作图法看到一个函数所有可能的输入及其对应的输出。

    Processing是一个编程环境和图形库，可以轻松将你的代码可视化, 可以将它看作自己编程想法的速写本。
    创建的每个processing程序都被称作一个草图sketch

    方程的解(根)就是图像和x轴的交点。

    原理：不论要解的方程多复杂，只需要画出它的图像，然后近似求出它穿过x轴时的坐标即可，然后不断缩小坐标的可能范围，就可以得到精确到任何程度的答案。
"""
# processing画完图后再用猜测检验法求根
def f(x):
    return 6*x**3+31*x**2+3*x-10

def average(a, b):
    return (a + b) / 2.0

def guess():
    lower = -1
    upper = 0
    for i in range(40):
        midpt = average(lower, upper)
        if f(midpt) == 0:
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt


if __name__ == '__main__':
    x = guess()
    print(x, f(x))

# # grid size
# xmin = -10
# xmax = 10
# ymin = -10
# ymax = 10
#
# # calculate range
# rangex = xmax - xmin
# rangey = ymax - ymin
#
#
# def setup():
#     global xscale, yscale
#     # scale the axis to fit the coordinate
#     size(600, 600)
#     xscale = width / rangex  # 600 / 20 = 30
#     yscale = -height / rangey  # 600 / 20 = 30
#
#
# def grid(xscale, yscale):
#     """draw the coordinate grid"""
#     strokeWeight(1)
#     stroke(0, 255, 255)  # cyan color
#     # like (-10,-10) to (-10, 10), (-9, -10) to (-9, 10)...
#     for i in range(xmin, xmax + 1):
#         line(i * xscale, ymin * yscale, i * xscale, ymax * yscale)
#     # like (-10, -10) to (10, -10), (-10, -9) to (10, -9)...
#     for i in range(ymin, ymax + 1):
#         line(xmin * xscale, i * yscale, xmax * xscale, i * yscale)
#     stroke(0)
#     line(0, ymin * yscale, 0, ymax * yscale)
#     line(xmin * xscale, 0, xmax * xscale, 0)
#
#
# def f(x):
#     """origin function"""
#     return 6 * x ** 3 + 31 * x ** 2 + 3 * x - 10
#
#
# def graphFunc():
#     """connect all dot which look like a continuous curve"""
#     stroke(255, 0, 0)
#     x = xmin
#     while x <= xmax:
#         fill(0)
#         line(x * xscale, f(x) * yscale, (x + 0.1) * xscale, f(x + 0.1) * yscale)
#         x += 0.1  # iter factor
#
#
# def draw():
#     # draw grid
#     global xscale, yscale
#     background(255)
#     translate(width / 2, height / 2)  # move the origin coordinate to screen center
#     grid(xscale, yscale)
#     graphFunc()