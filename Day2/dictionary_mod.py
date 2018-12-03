# Author：Steve

# 字典：key-value, 字典是无序的，取值靠key来唯一对应，天生去重
info = {
    'stu1101': "Steve",
    'stu1102': "Ate",
    'stu1103': "Ivan",
    'stu1104': "aaa",
    'stu1105': "bbb",

}
print(info)

print(info['stu1101'])     # 查

info['stu1102'] = "fffff"  # 修改
print(info)

info['stu1110'] = "just"   # 增加
print(info)

# 确保打印的字典有内容，用.get获取， 取不到是none
print(info.get('stu1103'))
print(info.get('stu1111'))

print('stu1111' in info)  # 直接判断stu1111是否在字典info里面，输出true或者， python2.7里写info.has_key("stu1111")



# 删除
'''
del info['stu1110']
print(info)

info.pop('stu1102')
print(info)

info.popitem()       # 随机删除
print(info)
'''

# 把字符转换成字典用 eval（string）
