# Author：Steve

import time

def deco(func):
    start_time=time.time()
    #func()
    return func     #直接返回地址，但无法继续执行下面的函数
    end_time=time.time()
    print("the func run time is %s" %(end_time-start_time))

def func1():
    time.sleep(3)
    print("in the func1")

def func2():
    time.sleep(3)
    print("in the func2")

# func1()
# func2()
func1=deco(func1)
func1()
fun2=deco(func2)
func2()