# Author：Steve
# 字符串拼接+格式化输出

name = input("name:")
age = input("age:")

# method1： 一般不用这个+拼接，因为会在内存中开辟多个内存空间，效率低下；其他几个方法都是开辟1块空间
info = '''
-----------info of ''' + name + '''-------------
name:'''+name+'''
age:'''+age+'''
'''

print("info="+info)

# method 2
# %s,s=string; %d numbers； %f....

age2= int(input("age2:"))  # force to change Integer

print(type(age))
print("age type=", type(age))
print("age2 type=", type(age2))
info2 = '''
-----------info2 of %s -------------
name:%s
age:%d
''' % (name, name, age2)
print("info2="+info2)


# method 3
# 官方推荐的格式化拼接方法！！
info3 = '''
-----------info3 of {_name}-------------
name:{_name}
age:{_age}
''' .format(_name=name, _age=age)

print("info3="+info3)

# method3的变形写法--但是不清晰
info4 = '''
-----------info3 of {0}-------------
name:{0}
age:{1}
''' .format(name, age)

print("info4="+info4)
