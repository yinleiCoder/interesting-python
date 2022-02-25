"""
python中的生成器原理：
    python中函数的工作原理——python解释器是用C写的，会用PyEval_EvalFramEx(C函数)去执行foo()
    首先会创建一个栈帧。python中一切皆对象，栈帧也是对象，将代码变为字节码对象。在栈帧对象上下文中
    去运行字节码。当foo()调用bar()，又会创建一个栈帧类似运行。
    所有栈帧都是分配在堆内存上，这决定了栈帧可以独立于调用者存在。

    CPython's C stack                         Heap memory

    PyEval_EvalFrameEx(PyFrameObject *f)----->PyFrameObject(f_back f_code)----PyCodeObject(foo's bytecode)
    |                                           |
    | recurse                                   |
    |                                           |
    PyEval_EvalFrameEx(PyFrameObject *f)----->PyFrameObject(f_back f_code)
                                                |
                                                |
                                                PyCodeObject(bar's bytecode)
    生成器正是利用了栈帧对象分配在堆内存上。

                                    /PyFrameObject(f_lasti f_locals)
    PyGenObject(gi_frame gi_code) /
                                  \
                                   \PyCodeObject(gen_fn's bytecode)
    在UserList中，可以看到生成器的影子
"""
import inspect
frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()


# import dis
# print(dis.dis(foo))# 字节码
foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

def gen_func():
    yield 23
    name = "yinlei"
    yield 24
    age = 6
    return "yinzihao"

import dis
gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

