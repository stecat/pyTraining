# Author：Steve

# 继承


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating...." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


# class Man(People)这样Man就直接继承了People
class Man(People):
    def piao(self):
        print("%s is piaoing....20s....done" % self.name)

    '''
    # 重构父类People的方法sleep，但只会执行子类重构的这个sleep   
    def sleep(self):
        print("man is sleeping")
    '''

    # 如果父类的sleep()需要调用，然后子类的重构也要调用，则可如下写法：
    def sleep(self):
        People.sleep(self)  # 其实就是self就是m1
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is giving birth..." % self.name)


# m1 = Man() 因为继承了People所以得传参
m1 = Man('steve', 22)
m1.eat()
m1.piao()

w1= Women("ivan", 25)
w1.get_birth()
