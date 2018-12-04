# Author：Steve
# 面向对象编程简单例子：
# class

class dog:
    def __init__(self, name):
        self.name = name  # 传名字

    def bulk(self):
        print("%s：汪汪汪" % self.name)


# 造了3只狗
d1 = dog("steve")
d2 = dog("cat")
d3 = dog("ivan")

d1.bulk()
d2.bulk()
d3.bulk()
