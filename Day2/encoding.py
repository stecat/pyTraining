# -*- coding：gbk -*-
# Author：Steve

# utf-8是可变长的字符编码：所有英文和特殊字符都是按ASCII码占一个字节，中文是按3个字节
# unicode --(encode)--> utf-8 --(decode)--> unicode
# unicode --(encode)--> GBK --(decode)--> unicode
# 所以如果中文的软件是gbk格式要在日本机器上使用，所以首先通过gbk编码[decode]转为unicode，然后再通过解码[encode]转为utf-8就能用了
# 如果不转成unicode的话，系统会默认用ASCII转，则会报错，需要s.decode("gbk").encode("utf-8")
# python3 默认是unicode
import sys
print(sys.getdefaultencoding())
s = "你好"   # 默认是Unicode的，所以没有解码了
print(s)
s_gbk = s.encode("gbk")
print("gbk", s_gbk)     # 得申明按gbk，打印开头的b为bytes
# 这部分.decode("gbk")是告诉计算机我是gbk要decode成unicode，再encode成utf-8
gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("UTF-8", gbk_to_utf8)
