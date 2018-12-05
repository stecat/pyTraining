# Author：Steve
# 面向对象编程OOP
'''
以下面向对象编程代码的优点：
1.代码量少了一半
2.角色和它具有的功能一目了然
'''


class Role(object):
    # 构造函数[__init__()]:在实例化时做一些类的初始化工作

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting....")

    def got_shot(self):
        print("ah....I got shot....")

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))  # 直接调用类里的name


print(Role)  # Role没有调用但其实在内存里

# 把一个类变成具体对象的过程叫实例化
'''
过程是  调用函数Role--执行---返回结果：
以为是这种方式：r1 =Role.__init__()  --->  return x342423(内存地址)
其实是这种方式：Role(r1, 'steve', 'police', 'AK47')---> r1.name="steve",r1.role="police",r1.weapon="AK47"...
如果Role.__init__(self, name, role, weapon, life_value=100, money=15000)传参需要接收r1，其实是用self来接收r1
以上的步骤就实例化完成了
'''
r1 = Role('steve', 'police', 'AK47')  # 此为实例化：即初始化一个类，造了一个对象，生成一个角色
r2 = Role('ivan', 'police', 'B22')  # 此为实例化：即初始化一个类，造了一个对象，生成一个角色

r1.buy_gun("AK47")