"""
contextlib简化上下文管理器：
    __enter__ __exit__每次需要定义class，还是略显麻烦。
    可以用contextlib简化
"""
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    yield {}
    print('file end')

with file_open('test.txt') as f:
    print('file processing')

