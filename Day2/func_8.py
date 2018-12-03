# Author：Steve

# 高阶函数

def add(x, y, f):      # abs的作用是, 传入的函数
    return f(x)+f(y)

res = add(3, -6, abs)   # abs是取绝对值
print(res)