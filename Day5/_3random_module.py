# Author：Steve

# Random 模块
import random

help(random)
print(random.random())  # random()取随机0~1的数

print(random.randint(1, 4))  # randint()取随机1~4的数, 类似[1，4]

print(random.randrange(0, 3))  # 实际是不含3，比较类似[0,3)

print(random.sample('abcdefgh', 3))  # 从字符串里随机取3个
print(random.choice("study python"))  # 从（"....."）随机取
print(random.choice(["apple", "hello", "lash"]))

print(random.uniform(1, 3))  # 指定区间，包含浮点数

# 洗牌random.shuffle()
items = [1,2,3,4,5,6]
print(items)
random.shuffle(items)
print(items)
