# Author：Steve

# 如果要导入命名规则不能用数字开头

import _1module
# 如果要导入所有模块里面的方法可以用, 但不建议这样用
# from _1module import *
'''
import 与 from...import...的区别

from _1module import *：其实本质就是将_1module的代码在被导入处全部复制一遍，所以方法调用在被导入处就直接【方法名()】调用即可
                        可能会和被导入处方法重名，但会按顺序进行执行（把方法名指向一个内存地址）
                import：就是【导入模块名.方法名】运用，但遇到重名还是会碰到一样的问题
                
要解决这个问题可以用关键字as： from _1module import say_hello as say_hello_1module, 调用的时候就用say_hello_1module()
                
'''
'''
import _1module
本质就是解释了一遍_1module，并将_1module里面所有的代码赋值给了变量_1module
所以就可以直接进行调用_1module.name

from _1module import say_hello
就是把say_hello()这个方法解释了一遍成为一个变量，就可以用say_hello()直接调用

所以单独import就需要用变量名.方法名进行调用，而from...import...则直接调用方法名即可
'''
print(_1module.name)
_1module.say_hello()