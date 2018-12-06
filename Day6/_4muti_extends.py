# Author：Steve

# 多继承
# class People:  经典类
class People(object):  # 新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 朋友列表friends
        # 在Relation()里面有append friends的操作，通过子类调用父类Relation()的方法，在父类People()里新增friends关联
        self.friends = []

    def eat(self):
        print("%s is eating...." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


class Relation(object):
    def make_friends(self, obj):  # 传参一个是自己，一个是另一个实例
        print("%s is making friend with %s" % (self.name, obj.name))
        # 调用make_friends后就会在People类的列表friends里面添加
        # 得添加obj，因为只添加对应name的话万一改了name这个关联就没有了
        self.friends.append(obj)


# class Man(People, Relation)这样Man就直接多继承了People，Relation
class Man(People, Relation):

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
        # 用super语法也可以父类的构造函数，
        # 用super以后更改父类名就不需要在子类重构中去改父类名，或者多继承的情况下也用super方便
        # People.__init__(self, name, age)  # 需先把父类的构造方法执行一遍
        super(Man, self).__init__(name, age)
        self.money = money
        print("%s once born with %s money" % (self.name, self.money))


class Women(People, Relation):

    def get_birth(self):
        print("%s is giving birth..." % self.name)


m1 = Man("steve", 22, 10)
w1 = Women("ivan", 25)

# 得添加obj，因为只添加对应name的话万一改了name这个关联就没有了,如下改名例子：
m1.make_friends(w1)  # 这里传的w1就是方法里的传参obj
print(m1.friends[0].name)
w1.name = "cat"   # 因为传了整个对象obj，所以改名后，friends列表会随着最新的对象name联动
print(m1.friends[0].name)
