# Author：Steve
import configparser

conf = configparser.ConfigParser()
conf.read("_9ConfigParser_mode.ini")

sec = conf.remove_section('bitbucket.org')
conf.write(open('_9ConfigParser_mode_ModiDel.cfg', "w"))

# ########## 改写 ##########
# sec = config.remove_section('group1')
# config.write(open('i.cfg', "w"))

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))
