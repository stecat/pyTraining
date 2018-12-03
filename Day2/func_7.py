# Author：Steve

# 参数组 函数名（*变量名）:当传参不确定时，使用参数组； 参数组一定要放在最后
# 转换成元组参数组的方式：
def func1(*args):
    print(args)

func1(1,1,2,2,3,3)
func1(*[1, 2, 3, 4])  # args = tuple([1, 2, 3, 4])
func1()


def func2(x, *args):
    print(x)
    print(args)

func2(1, 1, 1, 1, 2, 3, 4)

# **kwargs是把n个关键字形参使用字典方式: 使用**来表示
def func3(**kwargs):
    print(kwargs)
    print(kwargs['age'])  # 通过字典的key进行打印

func3(name='alex', age=8)
func3(**{'sex':'M', 'age':20})

def logger(source):
    print("from %s" %source)

def func4(name, age=19, *args ,**kwargs):
    print(name,age,args,kwargs)
    logger("func4")          # 必须把logger函数定义在调用前面，向前引用

func4("ste")
func4("iv", 4, 4, 4, lover='steve', sex='M')
func4("iv", 1, 2, 3, lover='ivan', sex='M')
