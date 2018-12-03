# Author：Steve

# 装饰器Decorator Pattern:为了给某程序增添功能，但该程序已经上线或已经被使用，那么就不能大批量的修改源代码:
# 原则: 1.不能修改被装饰的函数的源代码; 2. 不能修改被装饰的函数的调用方式
# 实现装饰器的知识储备：1.函数即"变量"：内存里的存放是和变量一样的原理  2.高阶函数  3.嵌套函数
# <函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖 = 装饰器>
import time


def timer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper


@timer
def func1():
    time.sleep(3)
    print('in the func1')


func1()