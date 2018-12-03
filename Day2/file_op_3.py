# Author：Steve

f = open("yesterday", 'r', encoding="utf-8")  # 文件句柄

# 打印文件句柄位置
print(f.tell())     # 按字符来计数
print(f.readline())
print(f.tell())
f.seek(0)   # 把句柄回到开头
print(f.seekable())  # 判断文件句柄是否可以移，如果是字符串和二进制可以，如果是tty文件设备终端就不能移

print(f.read(1))  # 读第几个字符

print(f.encoding)   # 打印文件编码

print(f.fileno())    # 返回文件句柄的编号，文件操作其实是调用操作系统本身给的接口进行操作

print(f.name)   # 打印文件名

print(f.isatty())  # 看是否是终端设备，底层的开发可能会用

# flush强制刷新：以写的模式打开文件，如果写完一行刚好断电，有可能没刷进硬盘，但是是把内容先放内存缓存buffer到达一定大小后再进行一次性写入硬盘
f.flush()

# 使用flush来打印进度条
import sys, time    # 导入sys和time模块
for i in range(20):
    sys.stdout.write("#")  # sys.stdout为标准输出，屏幕就是对应的标准输出
    sys.stdout.flush()
    time.sleep(0.1)
f.close()
print(f.closed)  # 判断文件是否关闭


# truncate截取
'''f2 = open("yesterday2", 'a')
print(f2.closed)
f2.seek(5)      # 先把文件句柄移到5，但是truncate不会看句柄位置
f.truncate(10)   # 从句柄第0位开始截取10位
f2.close()'''

# r+以读写的方式打开，最多用
f3 = open("yesterday2", 'r+', encoding="utf-8")   #文件句柄  r+读写
print(f3.readline())
print(f3.tell())
f3.write("---------r+ writing---------")
f3.close()

# w+以写读的方式打开：写读是先创建文件再读，如果是已存在文件会被清空
f4 = open("yesterday3", 'w+', encoding="utf-8")   # 文件句柄  w+写读
print(f4.readline())
print(f4.tell())
f4.write("---------w+ writing---------\n")
f4.write("---------w+ writing---------\n")
f4.write("---------w+ writing---------\n")
print(f4.tell())
f4.seek(10)
print(f4.tell())
print(f4.readline())
f4.write("hahahhahahha")    # python3中不允许seek到对应位置进行写入，他只会在最后一行进行写
f4.close()

# 还有a+以追加读写的方式打开

# rb读模式：以二进制方式读，视频文件，网络传输都用二进制
f5 = open("yesterday3", 'rb')  # 二进制默认不需要encoding = 'utf-8'
print(f5.readline())
f5.close()

# wb写模式：以二进制方式写，视频文件，网络传输都用二进制
f6 = open("yesterday3", 'wb')  # 二进制默认不需要encoding = 'utf-8'
f6.write("hello world\n".encode("utf-8"))    # 把写入的string转换为2进制，但文件里看到的不是二进制1010，而还是对应字符
f6.close()


