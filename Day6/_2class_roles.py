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

# 思考以上代码有没有对应可以改进的地方？
