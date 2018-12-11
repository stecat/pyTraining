# Author：Steve
# classmethod类方法

class Dog(object):
    # n=333  类变量可以调用
    def __init__(self, name):
        self.name = name
        self.n = 333

    @classmethod
    def eat(self):
        print("eating %s" % (self.n))


d = Dog("steve")
d.eat()
