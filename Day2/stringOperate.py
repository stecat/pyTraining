# Author：Steve

name = "my name is steve"
name2 = "my name \t is steve"

print(name.capitalize())    # 首字母大写
print(name.count('s'))      # 查数量
print(name.center(50, "-"))  # 总共打印50字符，参数放中间，其余用-补足
print(name.endswith("ve"))  # 判断是否以ve结尾
print(name2)   # \t为tab建
print(name2.expandtabs(tabsize=30))  # 把tab建转换为多少空格

print(name.find("name"))  # 找对应字符的开始位置，这样字符也可以做切片
print(name.find("y"))
print(name[name.find("name"):9])  # 字符串切片
print(name.isalnum())     # 检查是否是a-z+数字，有特殊字符就是false
print('123abc'.isalnum())
print('abA'.isalpha())
print('12A'.isdecimal())  # 是否是十进制
print('A'.isidentifier())  # 是否是合法的标识符，即合法的变量名
print('aa'.islower())
print('aa'.isupper())
print('22'.isnumeric())   # 是否是整数
print('my name is'.istitle())  # 是否是title
print('My Name Is'.istitle())

print('my name is'.join('=='))
print('|'.join(['1', '2', '3', '4']))  # join可以在列表中实现分隔

print(name.ljust(50, '*'))   # 保证长度为50，不够的话用*在右边补足
print(name.rjust(50, '*'))

print('STeve'.lower())
print('STeve'.upper())
print('  Steve\n...    ...    '.lstrip())   # 从左边去空格和回车
print('  Steve\n...    ...    '.rstrip())
print('  Steve\n...    ...    '.strip())    # 左右都去空格

mapping = str.maketrans("abcdefg", '1234567')  # 按前后对应关系进行转换，所以前后length必须保持一致
print("abcdefghijk".translate(mapping))        # 然后拿着"abcdefghijk"去mapping里面查对应关系

print('steve'.replace('e', 'E'))   # 把e替换
print('steve'.replace('e', 'E', 1))   # 替换1个e

print('steve.ie'.rfind('e'))  # 找到最右边匹配值的下标
print('steve.ie.s'.split('.'))  # 按'.'区分
print('steve.ie.\ns'.splitlines())  # 按\n区分,识别换行

print('Steve.iE.s'.swapcase())  # 大小写转换

print('steve.ie.s'.title())  # 转换成title  首字母大写

print('steve.ie.s'.zfill(20))  # 用0补足20位，进制转换可能有用

name3 = "my name is {xm}, {age} years old"
print(name3.format(xm='steve', age='25'))
print(name3.format_map({'xm': 'ivan', 'age': '23'}))   # format_map要传map格式的

