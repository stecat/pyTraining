# Author：Steve

# 函数需要在运行之前定义好


def foo():
    print('in the foo')
    bar()


def bar():
    print("in the bar")


foo()

import time


# 高阶函数：可以在不修改被装饰函数源代码的情况下为其添加功能

def ha():
    time.sleep(3)
    print("in the ha")


def func1(func):
    start_time = time.time()
    func()  # run ha()
    end_time = time.time()
    print("the function ha() run time %s" % (end_time - start_time))
    print(func)  # function内存地址


func1(ha)


def ha2():
    time.sleep(3)
    print("in the ha2()")


def func2(func):
    print(func)
    return func


func2(ha2)  # 直接写是把ha2内存地址传给func2()
func2(ha2())  # 这样是把ha2()的返回结果传入func2()
print(func2(ha2))

# 高阶函数可以不用改变函数的调用方式
ha2 = func2(ha2)  # python解释器可以有个符号解决=号的步骤，从而让调用方式不改变
ha2()  # run ha2()
