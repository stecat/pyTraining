# Author：Steve
# 异常处理exception
class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating...." % self.name, food)


# d = Dog("ivan")
# choice = input(">>:").strip()
#
# getattr(d,choice)    #---> 会报AttributeError: 'Dog' object has no attribute '1'

name = ['alex', 'jack']
# name[3]  #---->会报IndexError: list index out of range

data = {}
try:
    data['key']  # ----> KeyError: 'key'
except KeyError:
    print("no this kind of key")

try:
    data['name']
    name[3]
except KeyError as e:
    print("no this kind of key", e)
except IndexError as e:
    print("list operation error", e)

# 采用统一的处理error办法的场景就能写在一起：
try:
    data['name']
    name[3]
except (KeyError, IndexError) as e:
    print("有错误")

# 抓住所有的错误,一般不建议一开始就用，因为很多时候是需要调试的，但一般如果是未知错误的话可以这么写：：
try:
    data['name']
    name[3]
except FileNotFoundError as e:
    print("文件未找到",e)
except Exception as e:
    print("就知道出错了！")

# 如果都正常可以执行这个
else:
    print("一切正常")

# finally不管有没有错都执行
finally:
    print("不管有没有错，都执行")
