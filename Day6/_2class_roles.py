# Author：Steve

roles = {
    1: {'name': "Alex",
        'role': "terrorist",
        'weapon': "B1",
        'life_value': 100,
        'money': 15000
        },
    2: {'name': "Steve",
        'role': "police",
        'weapon': "B2",
        'life_value': 100,
        'money': 15000
        },
    3: {'name': "Cat",
        'role': "terrorist",
        'weapon': "B3",
        'life_value': 100,
        'money': 15000
        },
    4: {'name': "Ivan",
        'role': "police",
        'weapon': "B4",
        'life_value': 100,
        'money': 15000
        },
}

# 有了上面的字典后，调用角色只需要用role[1],role[2]...就可以了
print(roles[1])
print(roles[2])


# 开始写功能
def shot(by_who):
    # 开枪后减子弹数
    pass


def got_shot(who):
    # 中枪后减血
    who['life_value'] -= 10
    pass


def buy_gun(who, gun_name):
    # 检查钱够不够， 买了枪后要扣钱
    pass
'''
# 思考以上代码有没有不足的地方？
1. 属性添加时合法检查没有，weapon写成了wepon，也能进行添加
2. terrorist和police这2种角色有特定的角色操作限制，如不能杀队友
3. 处了通过got_shot的方法才能减血，目前没有限制life_value的减血限制
4. 如果要添加属性的时候，就会需要在每个角色里面一一添加属性，不符合代码可复用的原则
见_2class_roles_OOP.py
'''