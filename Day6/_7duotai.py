# Author：Steve
# 多态：同一个接口，多个实现

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):  # abstract method, defined by convention only
        pass  # raise NotImplementedError("subclass must implement abstract method")  异常抛出

    @staticmethod  # 装饰器
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):
    def talk(self):
        return 'meow!'


class Dog(Animal):
    def talk(self):
        return "woof!woof!"


# def animal_talk(obj):   这样已经是多态了，不过还需要直接把这个接口放入父类
#    obj.talk()


d = Dog("steve")
# d.talk()   #直接使用animal_talk
Animal.animal_talk(d)  # 这个就是一种接口多种实现, 也是接口的重用

c = Cat("ivan")
# c.talk()   #直接使用animal_talk
Animal.animal_talk(c)
