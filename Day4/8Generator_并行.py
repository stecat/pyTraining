# Author：Steve


#使用Generator实现生成者消费者并行例子
import time

def consumer(name):
    print("%s 准备吃包子！" %name)
    while True:
        while True:
            baozi = yield  #保存当前状态并返回

            print("包子[%s]来了，被[%s]吃了"%(baozi,name))
c=consumer("steve")
c.__next__()
baozi1="韭菜馅"
c.send(baozi1)  # send()是直接调用yield并赋值， 所以consumer里面的baozi=yield传入

def producer(name):
    c=consumer("A")
    c2=consumer("B")
    c.__next__()
    c2.__next__()
    print("开始做包子咯。。。。")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c.send(i)
        c2.send(i)

producer("ivan")