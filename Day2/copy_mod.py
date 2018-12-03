# Author：Steve

import copy

person = ['name', ['存款', '1000']]
# 浅copy的3种方式
p1 = copy.copy(person)
p2 = person[:]     # 完全切片也可作为浅copy
p3 = list(person)  # 工厂函数list作为浅copy

# 浅copy的使用场景：创建联合账户中的存取钱,第二层列表的账户会同时变动，如下实现也可以通过数据库外键
p4 = person[:]
p5 = person[:]
print(p4)
print(p5)
p4[0] = 'ste'
p5[0] = 'ivan'

p4[1][1] = '50'    # 只需要改person列表第2层一次，对象p4、p5中的存款额就同时改变
print(p4)
print(p5)
