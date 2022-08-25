"""
解一次方程:
    1.蛮力法(猜测检验法)，代入随机的值直到找到使等式成立的那个。
    2.为这类方程的解法找一个通用的公式
        所有的一次方程都符合这个通式：ax+b=cx+d
            => ax - cx = d - b
            => x(a - c) = d - b
            => x = (d - b) / (a - c)
"""


def equation(a, b, c, d):
    """
    解决ax+b=cx+d形式的方程
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    return (d - b) / (a - c)

def plug():
    """
    蛮力法(猜测检验法)：带入数看看哪个使等式2x+5=13成立
    :return:
    """
    x = -100
    while x < 100:
        if 2*x + 5 == 13:
            print(f'x={x}')
        x += 1


if __name__ == '__main__':
    plug()
    print(equation(2, 5, 0, 13))# 解2x+5=13