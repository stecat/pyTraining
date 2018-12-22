# 反射
# hasattr(obj,name_str)判断一个对象obj是否有对应的name_str字符串的方法
# getattr(obj,name_str)根据name_str字符串去获取obj对象里的对应方法的内存地址
# setattr(obj,'y',z) is equivalent to 'x,y = v'
# delattr


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating...." % self.name, food)


d = Dog("ivan")
choice = input(">>:").strip()


def bulk(self):
    print("%s shouting!!" %self.name)


# if choice=="eat":  这样的判断调用可以用反射
#     d.eat()
# print(hasattr(d, choice))  # hasattr(实例，字符串) 查类里是否有对应方法/属性
# print(getattr(d, choice))  # getattr()进行调用

if hasattr(d, choice):
    # getattr(d,choice)()
    func = getattr(d, choice)
    func("steve")

else:  # 如果没有对应的方法是否可以加一个，如下
    # print("no %s func in Dog" % choice)
    setattr(d, choice, bulk)
    # talk是在input时输入的字符，其实就通过上句setattr与方法bulk进行了关联，但调用需用talk
    # d.talk(d)  # 调用的时候需要把实例d传入  #相当于 d.talk = bulk
    # 这个用法记住！！--> 以下是上面d.talk()的优化，就不需要考虑输入的参数是什么都可以进行调用
    func2 = getattr(d, choice)
    func2(d)