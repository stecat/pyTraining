# Author：Steve
# configparser模块：用于生成和修改常见的配置文档,如mysql，nigix配置等等
import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressioonLeve;': '9'
}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']   # topsecret赋值，方便下面赋值
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes'

with open('_9ConfigParser_mode.ini','w') as configfile:
    config.write(configfile)
