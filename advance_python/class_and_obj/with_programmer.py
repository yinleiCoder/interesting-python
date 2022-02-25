"""
python中的with语句：
    简化try finally写法，即上下文管理器
    这里就是上下文管理器协议配合with语句
"""
def exe_try():
    try:
        # f_read = open('test.txt')
        print('code started')
        raise KeyError
        return 1
    except KeyError as e:
        print('Key Error')
        return 2
    else:
        print('no error')
        return 3
    finally:
        print('finally')
        # f_read.close()
        return 4

# 上下文管理器协议
class Sample:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print('do something')

if __name__ == '__main__':
    result = exe_try()
    print(result)# 4

    with Sample() as sample:
        sample.do_something()

