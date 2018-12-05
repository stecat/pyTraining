# Author：Steve

# 继承


#class People:经典类
class People(object):  #新式类
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

    # 如果想在Man()里面多传一个money的参数，这个参数Man()里有而Women()没有，那就要重新写父类里的构造方法
    def __init__(self, name, age, money):
        People.__init__(self, name, age)  # 需先把父类的构造方法执行一遍
        self.money = money
        print("%s once born with %s money" % (self.name, self.money))


class Women(People):

    def __init__(self, name, age, hair):
        # 用super语法也可以父类的构造函数，
        # 用super以后更改父类名就不需要在子类重构中去改父类名，或者多继承的情况下也用super方便
        super(Women, self).__init__(name, age)
        self.hair = hair


    def get_birth(self):
        print("%s is giving birth..." % self.name)


# m1 = Man() 因为继承了People所以得传参
m1 = Man('steve', 22, 1000)
m1.eat()
m1.piao()

w1 = Women("ivan", 25, "blue")
w1.get_birth()
