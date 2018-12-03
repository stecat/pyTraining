# Author：Steve

# 文件操作
open("yesterday")   # 打开文件
# 如果是windows打开需要写data = open("yesterday", encoding="utf-8").read()，
# python默认是编码格式是utf-8，而windows系统默认是GBK
'''
data = open("yesterday").read()  # 打开后读文件
print(data)
'''

# 通常需要建一个文件对象,即文件句柄：包含起始位置，大小等

f = open("yesterday")   # 文件句柄，默认从头开始读，读到末尾就把类似一个文件指针的东西（可理解为光标）放在末尾，一遍读完后就没了，要再读就把光标移回到开头
#data1 = f.read()
#print(data1)
print(f.readline())      # 不断读文件内容，读一行
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
# 以上可用for代替
for i in range(5):
    print(f.readline())
print("----------- readline() -----------")

# 循环文件，在第10行不打印, enumerate是取下标
for index, line in enumerate(f.readlines()):
    if index == 9:
        print("---------分隔线----------")
        continue
    print(line.strip())
print("-----------readlines()-----------")

# readlines(),不想有空格和换行可用f.strip()
for line in f.readlines():
    print(line)
f.close()    # 关闭文件



# 写文件,需要加打开文件的模式，
# 默认是读r模式；r+为读写模式既能读又能写，在3.0上只能写在最后面，2.0可以在任意写但会覆盖对应位置的值； rb为字节模式打开
# 写模式为w(w模式会清空文件并创建一个新文件，所以谨慎)；w+为写读；wb为字节模式打开
# a模式（append）为追加写入，不改原文件；  a+为追加读； ab为字节模式打开
f2 = open("yesterday2", 'w')    # 以写的方式默认打开就不能读，以读的方式打开就不能写
f2.write("%%%%%%%%%%%\n")
f2.write("------------")
f2.write("*************")   # 如果没有换行符是打印在一行里面的
f2.close()

# a模式（append）为追加写入，不会改原文件，但不会读
f3 = open("yesterday2", 'a')
f3.write("%%%%%%%%%%%\n")
f3.write("------------")

data3 = f3.readable()   # 判断是否可读
print(data3)
f3.close()
