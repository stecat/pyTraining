# Author：Steve


# 局部变量
def change_name(name):
    global school         # 使用global定义可以把局部变量变为全局，不建议函数里定义全局变量
    school = 'Education'
    print("b4 changed", name)
    name = 'Ivan'     # 这个函数就是这个变量的作用域
    print("after changed", name)

name = 'steve'
change_name(name)
print(name, school)


# 稍复杂的数据类型：列表，字典，集合都能在函数内里改全局，元组不能
list = ["ste", "jack", "rose"]
def list_func():
    list[0]="steve"
    print("函数体:", list)

list_func()
print("全局:", list)

# 如果全局变量和局部变量重名，那重名的局部变量只在函数体内有效，出了函数体则全局变量起效
duplicate = '全局'
def func():
    duplicate = '局部'
    print(duplicate)
func()
print(duplicate)
