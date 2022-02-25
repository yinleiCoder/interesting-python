"""
一个经典的参数错误：
    尤其注意class中传递list
"""

def add(a, b):
    a += b
    return a

if __name__ == '__main__':
    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a)
    print(b)

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)
    print(a, b)

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(c)
    print(a, b)
