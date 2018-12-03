# Author：Steve

# 嵌套函数，在函数内用def继续定义一个函数
def foo():
    print("in the foo")
    def bar():           # bar()为嵌套函数
        print("in the bar")

    bar()  # 嵌套函数的调用要再函数同位置进行调用
foo()

#函数调用，以下方式为函数调用
# def fun1():
#     fun2()

#局部作用域和全局作用域的影响范围
x = 0
def grandpa():
    x=1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()


# 函数嵌套，高阶函数叠加装饰器不改函数而增加函数功能形成装饰器
import time


def timer(func):   # timer(func1)  func=func1
    def deco():
        start_time=time.time()
        func()
        # return func     # 直接返回地址，但无法继续执行下面的函数
        end_time=time.time()
        print("the func run time is %s" %(end_time-start_time))
    return deco



def func1():
    time.sleep(3)
    print("in the func1")

@timer
def func2():
    time.sleep(3)
    print("in the func2")


print(timer(func1))
func1 = timer(func1)      # 运用语法糖 @timer 来代替func1 = timer(func1)此语句
func1()   # -->run deco() in fact

func2()    # 因为func2()上方有语法糖@timer，所以就直接用就会调用timer函数



def timer2(func):
    def deco(arg1):    # 带参的情况使用
                       # 如果想通用带参的个数可以写成 def deco(*arg1,**kargs):
        start_time=time.time()
        func(arg1)
        # return func     # 直接返回地址，但无法继续执行下面的函数
        end_time=time.time()
        print("the func run time is %s" %(end_time-start_time))
    return deco

@timer2     # func3 = timer2(func3) = deco ;  func3(name)=deco(name)
def func3(name):
    time.sleep(3)
    print("in the func3 name:",name)

func3("f3")