# Author：Steve

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print("%s is eating...." % self.name, food)


d = Dog("ivan", 22)
choice = input(">>:").strip()


def bulk(self):
    print("%s shouting!!" % self.name)


if hasattr(d, choice):
    delattr(d, choice)  # choice输入为name(即类属性name)，删除属性name后进行打印会报错属性已经不存在

else:  # 如果属性不存在就赋值22
    setattr(d, choice, 22)  # None这个值其实就动态装配了一个类的属性
    print(getattr(d, choice))  # 如果getattr()是一个方法则返回内存地址，这边是类的静态属性就直接返回值

print(d.name)
