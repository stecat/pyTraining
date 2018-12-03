# Author：Steve

def func1(x, y):
    print(x,y)
# 位置参数调用，与形参一一对应
func1(1, 2)
# 关键字调用，与形参顺序无关，关键字参数是不能写在位置参数前面的
func1(y=2, x=1)

a = 1
b = 2
func1(x=a, y=b)
