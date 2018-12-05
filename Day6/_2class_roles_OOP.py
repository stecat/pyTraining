# Author：Steve
# 面向对象编程OOP
'''
以下面向对象编程代码的优点：
1.代码量少了一半
2.角色和它具有的功能一目了然
'''
'''
Points：
析构函数，
实例化
类变量，实例变量(静态属性)
类的方法(动态属性)
私有方法，私有属性
'''

class Role(object):
    # 类变量的用途：大家共用的属性
    n = 123  # 类变量，不需要实例化就可以用
    name = "I am class name"
    n_list = []

    # 构造函数[__init__()]:在实例化时做一些类的初始化工作
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name  # 实例变量(静态属性)，作用域为实例本身  # 赋值给了实例
        self.role = role
        self.weapon = weapon

        # self.life_value = life_value
        # 对life_value的优化，变成私有属性--> __life_value
        self.__life_value = life_value  # 这样就变成私有属性了，以实现_2class_roles.py中的不足第3点
        self.money = money

    # 析构函数__del__()：在实例释放、销毁时自动执行，通常是收尾工作：如释放内存，关闭打开的临时文件，关闭数据库链接
    # 不需要传参，是函数执行完后自动执行
    def __del__(self):
        print("%s dead...." % self.name)

    def shot(self):  # 类的方法(即功能)(动态属性)
        print("shooting....")

    def got_shot(self):
        self.__life_value -= 50  # 此处就实现了对life_value内部访问，防止外部篡改，实现_2class_roles.py中的不足第3点
        print("%s ah....I got shot...." % self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))  # 直接调用类里的name

    # 定义一个方法访问私有属性
    def show_status(self):
        print("name:%s weapon:%s life_val:%s" % (self.name, self.weapon, self.__life_value))

    def __privateFunc(self):
        print("private func cannot call from outside!!")
    # 所以私有方法和私有属性只要在name前加__， 其实也算是封装：不想让别人看到的实现进行封装


print(Role)  # Role没有调用但其实在内存里

# 把一个类变成具体对象的过程叫实例化
'''
过程是  调用函数Role--执行---返回结果：
以为是这种方式：r1 =Role.__init__()  --->  return x342423(内存地址)
其实是这种方式：Role(r1, 'steve', 'police', 'AK47')---> r1.name="steve",r1.role="police",r1.weapon="AK47"...
如果Role.__init__(self, name, role, weapon, life_value=100, money=15000)传参需要接收r1，其实是用self来接收r1
以上的步骤就实例化完成了
'''
# 此为实例化：即初始化一个类，造了一个对象，生成一个角色
# r1实例化完即为对象，r1即成为Role这个类的实例
r1 = Role('steve', 'police', 'AK47')

r2 = Role('ivan', 'police', 'B22')  # 此为实例化：即初始化一个类，造了一个对象，生成一个角色

''' 
下面其实不是r1.buy_gun()  而是role.buy_gun(self)，因为buy_gun(self)是在role的内存里，但类要知道谁在调用
所以内部传其实转成了role.buy_gun(r1)进行处理
所有每个方法传参里面都会带一个self，如buy_gun(self)
'''
r1.buy_gun("AK47")

print(Role.n)  # 类变量，不需要实例化就可以调用,存在Role()的内存里

# 类里存在类变量name，实例化也存在实例变量name，所以调用顺序是先找实例变量，如果实例里没有的话再找类变量
print(r1.n, r1.name)

# 给实例更新属性
r1.name = "jobs"
# 给实例加新属性
r1.bullet_prove = True

print(r1.name, r1.bullet_prove, r1.role, r1.weapon)

# 通过实例改类变量，但实际是把类变量n在实例r1里面创建了一个实例变量n，所以实际类变量n是不会被更改，输出如下
r1.n = "r1改类变量"
print(r1.n)  # 此处输出为'r1改类变量'
print(r2.n)  # 此处输出为 123
print(Role.n)  # 此处输出为 123

Role.n = "Role更改类变量"
print(r1.n, r2.n, Role.n)

# 通过2个实例改成n_list列表的情况,看列表会包含各自实例添加的
r1.n_list.append("from r1")
r2.n_list.append("from r2")
print(Role.n_list, r1.n_list, r2.n_list)
'''
 访问私有属性 __life_value,通过方法show_status(),
 这样外部就无法直接通过【实例.静态属性】的方式调用更改，而只能通过方法调用
 print(r1.__life_value)  # 私有属性无法直接通过实例调用
 这样就实现_2class_roles.py中的不足第3点-->3. 应ß只有通过got_shot的方法才能减血，目前没有限制life_value的减血限制
'''
r1.show_status()
r1.got_shot()
r1.show_status()
# r1.__privateFunc()  私有方法无法访问到
