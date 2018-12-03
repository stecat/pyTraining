# Author：Steve
# Generator生成器
# 生成器一定是个iterator迭代器

a = [1, 2, 3]

List = [i*2 for i in range(10)]   # 列表生成式,也可以传函数[func(i) for i in range(10)]，但其实[]则是一个list
print(List)
# 相当于： a=[]
#         for i in range(10):
#            a.append(i*2)


# 生成器无法直接用下标调用，生成器只有在调用(用next方法)时才会生成相应的数据
# 生成器只记当前位置所以很省内存，只有一个——__next__()方法可以调用
gen = (y*2 for y in range(10))   # ()此为生成器，数据量大的情况下用这个方式数据是马上返回，调用访问的时候才会生成，不访问的情况下只是存了一个算法
print(gen)      # 打印的是generator的地址
print(gen.__next__())   # 打印的是generator的对应序列的内容
print(gen.__next__())

# 每次调用next()太麻烦了， 用for循环打印
for n in gen:
    print(n)

