# Author：Steve

# 函数
def func1():
    ''' function definition: '''
    print("func1")
    return 0

# 过程
def func2():
    '''function definition: '''
    print("func2")

x = func1()
y = func2()

print("func1 return is %s" %x)
print("func2 return is %s" %y)    # python中隐式返回了none
