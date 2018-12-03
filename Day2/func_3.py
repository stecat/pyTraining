# Author：Steve

# 函数返回值
def func1():
    pass

def func2():
    return 0

def func3():
    return 0, 10, 'hello', ['ste', 'ivan'], {'key': 'value'}

f1 = func1()
f2 = func2()
f3 = func3()

print('func1() return %s' %type(f1),f1)
print('func2() return %s' %type(f2),f2)
print('func3() return %s' %type(f3),f3)