# Author：Steve

# 使用函数的好处：可复用的逻辑一定要定义成def函数的形式
import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("a.txt", 'a+') as f:
        f.write('%s end action\n' %time_current)   # 日志可以直接打印时间

def call1():
    print("call1 starting action...")
    logger()


def call2():
    print("call2 starting action...")
    logger()


def call3():
    print("call3 starting action...")
    logger()

call1()
call2()
call3()
