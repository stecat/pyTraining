# Author：Steve

# buildin function内置方法
# all()判断是否存在0？
print(all([-1,5,0]))
#any()判断是否全是0
print(any([0,0]))

# bin()10进制转2进制，b指的是开头，如bin(2)输出是0b10，2的二进制为0010
print(bin(2))

# bool()判断是否有element，输出true就是存在，输出false就是不存在
print(bool(1))
print(bool([]))

#bytearray可修改的二进制字节格式
a=bytes('abcde', encoding="utf-8")
print(a.capitalize(),a)
b=bytearray('abcde', encoding="utf-8")
print(b[0])
#b[1]="B"   只能输数字，即字符对应的ascci码
b[1]=110
print(b)

# callable判断是否可以调用
def a():pass
print(callable(a))

# chr()   and   ord()
print(chr(98))
print(ord('b'))

# compile()编译，可以把字符串转成代码直接运行
code='''
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
'''
py_obj=compile(code, "err.log", "exec")  # compile(变量, 错误log名， 以什么方式执行一般都是exec)
exec(py_obj)
exec(code)   #exec(变量)也可以直接运行

# dir()  查对象有什么方法
a=[]
print(dir(a))

# filter()  and 匿名函数:一般不会多次调用的函数，用完就删可以使用匿名函数lambda，但只能处理比较简单的运算以及三元运算
res=filter(lambda n:n>5, range(10))    # 过滤你要的数据,过滤出大于5的数据
res1=map(lambda n:n*2, range(10))
for i in res:
    print(i)

def sayhi(n):
    print(n)
sayhi(3)

calc = lambda n:print(n)  #相当于 (lambda n:print(n))(3)
calc(3)

# reduce
import functools
res2 = functools.reduce( lambda x,y:x+y, range(10))  # x,y在range不断取值进行相加
print(res2)

a = frozenset([1, 2, 3, 4, 4, 5])
#a[1]=3

# globals() 返回整个文件中的所有对象的key，value
print(globals())

#locals()只调用函数
def test():
    local_var=333
    print("locals():",locals())
    print("func inner globals()：",globals())
test()
print("globals().get('local_var'):",globals().get('local_var'))

# hash
print(hash("steve"))
print(hash(1))

#hex()转16进制
print(hex(16))

#oct()转8进制
print(oct(8))

# pow()多少次方,3的2次方
print(pow(3,2))


# round()
print(round(1.3333,2))

#slice()切片,其实可以直接用d(2,5)
d=range(10)
print(d[slice(2,5)])

#sorted() 排序
a={6:2, 8:0, 1:4, -5:6, 99:11}
print(a)
print(sorted(a.items()))  #a.items()默认按key来排序，并且转为数组
print(sorted(a.items(),key=lambda x:x[1]))  #这样就是按照value来排序， x指的是数组中每个元素，x[1]取数组中第二个数

#zip()对应组合，其实可以类别joint

b=[1,2,3,4,5,6]
c=['a','b','c','d']
print(zip(c,b))    #3.0后变成了迭代器
for i in zip(c,b):
    print(i)

#  __import__() 只知道字符串的情况下进行导入
__import__('Decorator')
