# Author：Steve

# 多级字典嵌套，key尽量不要写中文
catalog = {
     "欧美": {
         "www.facebook.com": ['social', 'social network'],
         "www.google.com": ['search', 'search network'],
         "www.quora.com": ['knowledge sharing', 'knowledge sharing network' ]
     },
     "中国": {
         "www.zhihu.com": ['知识分享', '知识分享网站'],
         "www.baidu.com": ['搜索', '搜索网站'],
         "www.douban.com": ['图书影评', '图书影评网站']
     },
     "日韩": {
         "www.bilibili.com": ['video', 'video network'],
         "www.japan.com": ['nation', 'national network'],
     }
}
# 改
catalog["中国"]["www.baidu.com"][1] = 'rubbish website'
print(catalog)

# 取字典所有key
print(catalog.keys())
# 取字典所有value
print(catalog.values())
# dict.setdefault(key, defaultValue)，如果字段能取到key就不变，如果取不到这个key就set一个default的值
catalog.setdefault("Hz", {"www.taobao.com": ["platform", "buy things"]})
print(catalog)
catalog.setdefault("中国", {"www.taobao.com": ["platform", "buy things"]})
print(catalog)


# update:重叠的数据进行覆盖，没有的内容进行更新
b = {
    'stu2101': "hhhh",
    'stu2111': "lllll"
}

info = {
    'stu2101': "wa",
    'stu2102': "sa",
    'stu2103': "la"
}

info.update(b)
print(info)

# 字典转换为列表
print(info.items())

# fromkeys()初始化一个新字典
print(info.fromkeys([6, 7, 8]))  # 此时其实和info没什么关系，完全可以写成dict.fromkeys([6,7,8])
# fromkeys()初始赋值value
print(dict.fromkeys([6, 7, 8], "test"))

c = dict.fromkeys([6, 7, 8], [8, {"name": "nike"}, 444])
print(c)
c[7][1]['name'] = "adidas"      # [7]对应字典key:7 , [1]对应列表下标为1的内容， 【'name'】对应字典key: name
print(c)                        # 注意：所以fromkeys创建字典的时候如果你有多层，改的话会改所有key对应的值而不是只改你指定的值
