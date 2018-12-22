# Author：Steve

# 自定义异常
class SteException(Exception):  # 继承Exception
    def __init__(self, msg):
        self.message = msg

        def __str__(self):  # 定义打印异常返回的格式
            return self.message


try:
    raise SteException('数据库连不上')  # 触发自定义的异常需要用raise来触发，'数据库连不上'会直接传到msg里
except SteException as e:
    print(e)  # 打印e就是返回的实例


# 基类里存在IndexError，那自定义IndexError会覆盖吗？自己写的重名的IndexError会有影响，所以尽量不要重名
class IndexError(Exception):
    def __init__(self, msg):
        self.message = msg

try:
    name= []
    name[3]
   # raise IndexError("IndexError数据库连不上")
except IndexError as e:
    print(e)

