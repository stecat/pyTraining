# Author：Steve

# 集合set以及关系测试
list1 = [4, 9, 1, 5, 7, 3, 6, 7, 9]
list1 = set(list1)            # 集合自动去重, 且是无序的
print(list1, type(list1))

list2 = set([2, 6, 0, 66, 22, 8, 4])
print(list1, list2)

# 取2集合的交集intersection
print(list1.intersection(list2))
print(list1 & list2)  # 交集运算符为&

# 取2集合的并集union，去掉重复的内容
print(list1.union(list2))
print(list1 | list2)  # 并集运算符为 |

# 取2集合的差集difference，在一方有另一方没有的：如，list_1里有但list2里没有的取出来
print(list1.difference(list2))
print(list1 - list2)  # 差集运算符为-


# 判断是否是子集subset：下面的意思是list1是否是list2的子集
print(list1.issubset(list2))

# 判读是否是父集upset
print(list1.issuperset(list2))

# 对称差集symmetric_difference：去掉重复的
print(list1.symmetric_difference(list2))
print(list1 ^ list2)  # 对称差集运算符为^


print("_____________________________")
list3=set([1])
# 没有交集返回为true
print(list1.isdisjoint(list3))


list4 = set([1, 2, 3, 4])
list4.add(999)     # 添加,一次只能添加一个
list4.add(1)
print(list4)

list4.update([1, 9, 8])   # 添加多项
print(list4)

# print(list4.remove()) 如果要打印删除后的list结果，不用全部打印remove，如果打印只会告诉你删除的结果
list4.remove(1)
print(list4)

list4.discard(999)
print(list4)

# 计算长度
print(len(list4))

# 判断是否在集合里，字典、列表、字符串都是这么判断
print(1 in list4)
print(1 not in list4)