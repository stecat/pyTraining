# Author：Steve

def func1():
    print("in the func1")

def func2():
    print("in the func2")
    return 0

def func3():
    print("in the func3")
    return 0, 10, 'hello', ['ste', 'ivan'], {'key': 'value'}

x = func1()
print(x)
y = func2()
print(y)
z = func3()
print(z)
