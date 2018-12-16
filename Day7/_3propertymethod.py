# Author：Steve
# 属性方法@property:把一个方法变成一个静态属性


class Dog(object):
    '''this class for dog'''

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))


d = Dog("steve")
# d.eat()
d.eat  # 使用@property把方法变成了静态属性，调用就直接d.eat，这样就不能传参赋值了


# 采用这种方法可以赋值 再写一个eat的方法
class Dog2(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter  # 需要传参的方法名必须保持一致，如都为eat，并且得写在原方法下面
    def eat(self, food):
        print("set to food", food)
        self.__food = food


d2 = Dog2("ivan")
d2.eat = "包子"
d2.eat


# 如果想删私有属性用下面的方法
class Dog3(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print("set to food", food)
        self.__food = food

    @eat.deleter  # 删除了私有属性
    def eat(self):
        del self.__food
        print("删除了私有属性")


d3 = Dog3("cat")
d3.eat = "包子"
d3.eat
del d3.eat  # 使用这个调用了@eat.deleter
# d3.eat

# __doc__　　表示类的描述信息
print(Dog.__doc__)

# __module__ 和  __class__
# __module__ 表示当前操作的对象在那个模块
# __class__     表示当前操作的对象的类是什么

from Day7._3propertymethod_FlightSample import Flight

obj = Flight("steve")
print(obj.__module__)
print(obj.__class__)


# __call__ 对象后面加括号，触发执行。
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
class Dog4(object):
    '''this class for dog'''

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))

    def __call__(self, *args, **kwargs):
        print("running call...", args, kwargs)


d4 = Dog4("steve")
d4(1, 2, 3, name=33)

# __dict__ 查看类或对象中的所有成员
print(Dog4.__dict__)  # 通过类调用就可以看类属性，不包括实例属性
print(d4.__dict__)  # 通过实例调用就可以看实例属性，不包括类属性


# __str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
class Dog5(object):
    '''this class for dog'''

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))

    def __str__(self):
        return "<obj:%s>" % self.name


d5 = Dog5("steve5")
print(d4)
print(d5)


# __getitem__、__setitem__、__delitem__
# 用于索引操作，如字典。以上分别表示获取、设置、删除数据
class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'alex'  # 自动触发执行 __setitem__
del obj['k1']


class Foo_practice(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)


obj_practice = Foo_practice()
obj_practice['name'] = "steveFoo"
print(obj_practice['name'])
print(obj_practice.data)


# __new__ \ __metaclass__
class Foo1(object):  # 追溯一下类的类是谁

    def __init__(self, name):
        self.name = name


f = Foo1("alex")
print(type(f))  # 输出说明f这个对象是来自Foo1这个类
print(type(Foo1))  # Foo1就是来自type


# 所以来看一下type是怎么创建Foo1的， 以上是普通方式，下面是特殊方式
def func(self):
    print("func out of class")


def func2(self):
    print("func2 out of class name %s" % self.name)  # 这样就可以直接调用__init__函数的参数name


def __init__(self, name, age):
    self.name = name
    self.age = age


# Foo2=type(类名,(继承谁),方法名)
# #type第一个参数：类名
# #type第二个参数：当前类的基类
# #type第三个参数：类的成员
Foo2 = type('Foo2', (), {'funcname': func})
f2 = Foo2()
f2.funcname()  # 直接调用func这个方法
print(type(Foo2))

# 通过type 把方法func2和__init__装配进Foo3这个类，方法中的属性就可以相互调用
Foo3 = type('Foo3', (), {'funcname': func2, '__init__': __init__})
f3 = Foo3("chen", 22)
f3.funcname()


# 下面来考虑 type是哪里来：
# __new__ \ __metaclass__
class MyType(type):
    # 第一阶段：Foo4类初始化init
    def __init__(self, what, bases=None, dict=None):
        print("MyType>>__init__")
        super(MyType, self).__init__(what, bases, dict)

    # call方法给对象加一个括号就可以调用
    # 第二阶段1：实例化调用call
    def __call__(self, *args, **kwargs):
        print("MyType>>__call__")
        # 第二阶段2：调用Foo4的call
        obj = self.__new__(self, *args, **kwargs)
        # 第二阶段3：调用Foo4的init
        self.__init__(obj, *args, **kwargs)


class Foo4(object):
    # 定义我的类如何被创建
    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print("Foo4>>__init__")

    # new 在实例化的时候会执行，并先于init执行
    # 如果需要实例化的时候有一些定制则会用到new，下面其实就算重构了new
    def __new__(cls, *args, **kwargs):
        print("Foo4>>__new__")
        # 如果下句return不执行，那init则不执行
        # 所以是通过new来实例化，new会触发init
        return object.__new__(cls)  # 把Foo4传给cls，cls就类似于self，此处是去继承父亲的new方法


# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo4("steve")
print(obj.name)
