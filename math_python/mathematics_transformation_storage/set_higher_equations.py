from math import sqrt
"""
解更高次的方程:
    二次方程，方程中包含了一个二次方项.通用表达式为ax^2+bx+c=0(a、b、c可以是任意常数，a不等于0), 可以有2个解。
    二次方程求解公式求出二次方程的解：x1=(-b+√(b^2-4ac))/2a, x2=(-b-√(b^2-4ac))/2a
"""

def quad(a, b, c):
    """
    二次方程求解公式解2x^2+7x-15=0的解
    :return:
    """
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

def g(x):
    return 6*x**3+31*x**2+3*x-10

def plug():
    """
    蛮力法：解三次方程, 但是你可能会怀疑，x^3应该出现3个解，蛮力法找到这样一个解，
            无法确定是否存在其他的解，也无法找到他们的值。此时，可以通过作图法看到一个函数所有可能的输入及其对应的输出。
    :return:
    """
    x = -100
    while x < 100:
        if g(x) == 0:
            print(f'x={x}')
        x += 1
    print('done.')

if __name__ == '__main__':
    print(quad(2, 7, -15))
    plug()