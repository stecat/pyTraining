# Author：Steve

# 斐波那契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b  # 此语句不是a=b  b=a+b，而是类似t=(b,a+b), a=t[0]=b, b=t[1]=a+b
        n = n+1
    return 'done'

fib(10)

# a, b = b, a+b 的实现：
a=1
b=2
t=(b,a+b)
print(t)

# fib中把print(b)改成yield b即为生成器generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b  # 此语句不是a=b  b=a+b，而是类似t=(b,a+b), a=t[0]=b, b=t[1]=a+b
        n = n+1
    return 'fib_generator func return done'   #用next会打印done，用for循环则不会

fg= fib_generator(10)
while True:       #抓异常，此异常为StopIteration，然后会返回函数return值
    try:
        x=next(fg)
        print("fg:",x)
    except StopIteration as e:
        print('generator return value:', e.value)
        break
# print(fg.__next__())
# print("干点别的事，再进生成器fib_generator(）")
# print(fg.__next__())
# print("-------for循环开始---------")
# for i in fg:
#     print(i)
#
# print(fg.__next__())   # 再用next打印就会出错，这时候需要抓住异常