# Author：Steve

# setattr(obj,'y',z) is equivalent to 'x,y = v'



class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating...." % self.name, food)


d = Dog("ivan")
choice = input(">>:").strip()


def bulk(self):
    print("%s shouting!!" % self.name)


# if choice=="eat":  这样的判断调用可以用反射
#     d.eat()
# print(hasattr(d, choice))  # hasattr(实例，字符串) 查类里是否有对应方法/属性
# print(getattr(d, choice))  # getattr()进行调用

if hasattr(d, choice):
    #func = getattr(d, choice)
    #func("steve")  如果是调用属性就不能直接调用
    attr = getattr(d, choice)
    setattr(d, choice, "改名")
    print(d.name)   # 输入数据为name，类属性name就会输出"改名"

else:  # 如果属性不存在就赋值22
    setattr(d, choice, 22)  # None这个值其实就动态装配了一个类的属性
    # 如果getattr()是一个方法则返回内存地址，这边是类的静态属性就直接返回值，所以不能用d.的操作
    print(getattr(d, choice))
