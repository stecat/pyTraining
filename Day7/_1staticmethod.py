# Author：Steve

# staticmethod静态方法

class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod  # 实际上和类Dog()没关系，只是调用的时候需要通过类的实例进行方法调用
    #os模块这个工具包调用如mkdir()就是静态的
    def eat(food):  # 不加静态方法会出现报错AttributeError: 'Dog' object has no attribute 'eat'
        print("eating %s" % (food))


d = Dog("steve")
d.eat("fruit")
