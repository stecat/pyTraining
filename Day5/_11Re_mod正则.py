# Author：Steve
# re模块:正则表达式

import re

# macth(需要匹配数据,"原数据"): 是从字符串开头往后匹配
res = re.match("^ste", "steve")  # ^ 是匹配字符开头，但在match()里面没任何用，match本身就是从开头匹配
print(res)  # 有返回就是匹配到
print(res.group())  # 查看匹配到了什么
print(re.match("^q", "steve"))  # 没匹配到返回是none

# 场景1：匹配文字以及后面的数字,'\'是使用正则的语法，d代表匹配数字，\d就是匹配后面一个数字,匹配多个就是\d+
res2 = re.match("steve\d", "steve123happy2019")
print(res2.group())
res3 = re.match("steve\d+", "steve456happy2019")
print(res3.group())

'''
   '.'---->默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
   '^'---->匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
   
'''
print(re.match('^.\d', "ste12"))  # ^为匹配字符开头，.匹配一个字符即匹配到s，\d是后面的数字，可是s后面没有数字
print(re.match('.+\d', "ste123").group())  # + 是匹配多个，.+就是匹配多个字符，所以此处\d就没什么用
'''
'$'匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以

'''
print(re.match("^R.+a$", "Chen321Ronghua123"))
print(re.match("C.+a", "Chen321Ronghua123"))

# 所以要匹配查所有的话就要用serach()：
print(re.search("R.+", "Chen321Ronghua123"))
print(re.search("R.+a", "Chen321Rong1hua123a"))   # 匹配字符串R到最后一个a中的所有

# 场景：只匹配字符Ronghua
print(re.search("R[a-z]+a", "Chen321Ronghua123a"))   # [a-z]指的是只匹配a-z的字符
