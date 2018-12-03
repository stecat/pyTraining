# Author：Steve

# 列表list
name = ["zy", "ste", "ruby", "ste", "kobe"]
print("1",name[0], name[1], name[3])

# 切片的使用： 一起取出名字ste, ruby
print("2",name[1:2])
print("3",name[1:3])   # 切片：取的规则是，取开头不取结尾

print("4",name[-1])   # 切片：-1取的是列表最后一个
print("5",name[-2])   # 切片：-2取的是列表倒数第二个

print("6",name[-1:-3])  # 这样写取不到值，只能用下句
print("7",name[-3:-1])  # 这样会导致-1永远取不到，请看下句
print("8",name[-2:])  # 想取第一个位置都可以不写
print("9",name[:3])

print("10",name[0:-1:2])  # 分开切片, 这个意思就是从首0到尾-1隔着2取，
print("11",name[::2])  # 上句相当于此句，0和-1可以省略


# 列表循环打印
for i in name:
    print(i)
    #print(name[i])  这样用错误


'''
# 追加append
name.append("ivan")
print(name)
'''

'''
# insert:插入列表固定位置
name.insert(1, "mark")
print(name)
'''

# 更改列表
'''
name[0] = "Mary"
print(name)
'''

# 删除列表中某个内容
'''
name.remove("Mary")
print(name)

del name[1]
print(name)

name.pop()  # 默认删列表最后一个，如果要删列表第二个就写 pop(1)
print(name)
'''
'''
# 找具体内容在列表中的位置
print(name.index("ste"))
print(name[name.index("ste")])  # 用查出的索引去取内容


# 查找列表重复数据
print(name.count("ste"))

# reverse 反转列表
name.reverse()
print(name)

# sort 排序
name.sort()
print(name)

# extend 扩展
name2 = [1, 2, 3]
name.extend(name2)
print(name, name2)
'''
# copy
'''
name3 = name.copy()
print(name3)
print(name)

name[0] = "goody"
print(name)
print(name3)
'''

'''
# 列表里嵌套列表,以及浅copy
list1 = ["1", "2", ["11", "22"], "3"]   # 第二层["11"，["22"]]copy是直接指针指向地址，所以改list1和list2的第二层都会改变
list2 = list1.copy()      # if 用list2=list1，就是直接关联地址
list1[1] = "mac"
list1[2][0] = "ste"
print(list2)
print(list1)

list2[2][1] = "**"
print(list1)
print(list2)

# 接上面，要完全copy，使用copy库
import copy
list3 = copy.copy(list1)  # 这个也是浅copy
list4 = copy.deepcopy(list1)  # 完全copy
'''

