# Author：Steve
import configparser
conf = configparser.ConfigParser()

conf.read("_9ConfigParser_mode.ini")

print(conf.sections())  #  default的节点不会打印
print(conf.default_section)  # default节点名
print(conf.defaults())   # default节点内容

print(conf['bitbucket.org'])
print(conf['bitbucket.org']['User'])

# 循环打印,DEFAULT的节点中的内容都会在其他节点中打印
for key in conf['topsecret.server.com']:
    print(key)

options = conf.options('bitbucket.org')
print(options)

item_list = conf.items('bitbucket.org')
print(item_list)

# 取出来string
val = conf.get('bitbucket.org','user')
print(val)
# 取出来int
val_int = conf.getint('bitbucket.org','num')
print(val_int)