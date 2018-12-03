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
   这个flags的参数: 忽略大小写flags=re.I
'''
print(re.match('^.\d', "ste12"))  # ^为匹配字符开头，.匹配一个字符即匹配到s，\d是后面的数字，可是s后面没有数字
print(re.match('.+\d', "ste123").group())  # + 是匹配多个，.+就是匹配多个字符，所以此处\d就没什么用
print("having FlagsI：", re.search("[a-z]+", "steveAB", flags=re.I))  # 忽略大小写
print("having FlagsMULTILINE：", re.search(r"^a", "\nabc\neee", flags=re.MULTILINE))  # 换行也能匹配到
print("having FlagsS：", re.search(r".+", "\nabc\neee", flags=re.S))  # 点任意匹配模式，改变'.'的行为，匹配任意字符
'''
'$'匹配字符结尾，只作用在最后，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'''
print(re.match("^R.+a$", "Chen321Ronghua123"))
print(re.match("C.+a", "Chen321Ronghua123"))

# 所以要匹配查所有的话就要用serach()：
print(re.search("R.+", "Chen321Ronghua123"))
print(re.search("R.+a", "Chen321Rong1hua123a"))  # 匹配字符串R到最后一个a中的所有

# 场景：只匹配字符Ronghua
print(re.search("R[a-z]+a", "Chen321Ronghua123a"))  # [a-z]指的是只匹配a-z的字符
print(re.search("R[a-zA-Z]+a", "Chen321RongAAhua123a"))  # [a-zA-Z]指的是只匹配a-z以及A-Z的字符

'''
'+' 匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'''
# 场景： 匹配#号中间的字母
print(re.search("#.+#", "123#hello#world"))

'''
'?'  匹配前一个字符1次或0次
'''
print(re.search("aal?", "aalexaaa"))
print(re.search("aal?", "aaexaaa"))

'''
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'''
print(re.search("[0-9]{3}", "aa1x2a3456aa"))
print(re.search("[0-9]{1,3}", "aa1x2a345aa"))
# search()只能返回一个，想返回所有怎么办？  用findall()
print(re.findall("ab{1,3}", "abb abc abbcbbb"))

'''
'|'  匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'''
print(re.search("abc|ABC", "ABCBabcCD"))
print(re.findall("abc|ABC", "ABCBabcCD"))
'''
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
'''
print(re.search("(abc){2}a(123|456)c", "abcabca456c").group())
print(re.search("(abc)", "abclexcc"))  # 匹配abc
print(re.search("abc{2}", "abclexabcc"))  # 匹配c 2次
print(re.search("(abc){2}\|", "abclexcabcabc||"))
print(re.search("(abc){2}\|\|", "abclexcabcabc||"))  # 匹配abc 2次，\|为匹配管道符|，加\是转译

'''
'\A'  只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'  匹配字符结尾，同$
'''
print(re.search("\A[0-9]+[a-z]\Z", "A123a"))  # \A[0-9]开头匹配数字[0-9], [a-z]\Z是匹配字符[a-z]结尾
print(re.search("\A[0-9]+[a-z]\Z", "111aa"))  # \A[0-9]开头匹配数字[0-9], [a-z]\Z是匹配字符[a-z]结尾
print(re.search("\A[0-9]+[a-z]+\Z", "111aa"))  # \A[0-9]开头匹配数字[0-9], [a-z]\Z是匹配字符[a-z]结尾

'''
'\d'    匹配数字0-9
'\D'    匹配非数字,包括特殊字符
'''
print(re.search("\D+", "123$-q\n"))

'''
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
'''
print(re.search("\w", "123$-q\n"))
print(re.search("\w+", "123$-q\n"))
print(re.search("\W+", "123$-\nq"))
print(re.search("\W+", "123$-q\n"))

'''
'\s'  匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''
print(re.search("\s", "123$-\n\rq"))
print(re.search("\s+", "123$-\n\r    q"))

'''
'(?P<name>...)' 分组匹配 
re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 
结果{'province': '3714', 'city': '81', 'birthday': '1993'}
'''

print(re.search("(?P<id>[0-9]+)", "abcd1234daf@34").group())
print(re.search("(?P<id>[0-9]+)", "abcd1234daf@34").groupdict())
print(re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)", "abcd1234daf@34").groupdict())
print(re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)", "abcd1234daf@34").groupdict())
b = re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)", "abcd1234daf@34").groupdict()
print(b["id"])
a = re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)", "abcd1234daf@34").group('id')
print(a)
# 场景：取身份证
print(
    re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict("city")
)

'''
re.split() 以匹配到的字符当做列表分隔符
'''
print(re.split("[0-9]", "abc12de3f45GH"))
print(re.split("[0-9]+", "abc12de3f45GH"))

'''
re.sub("匹配模式"，"替换值","需要被替换的"，"替换次数")      匹配字符并替换
'''
print(re.sub("[0-9]+", "|", "abc12de3f45GH"))
print(re.sub("[0-9]+", "|", "abc12de3f45GH", 1))  # 在abc12de3f45GH中匹配所有数字替换为管道符|碰到字数只替换1次

# 场景： 匹配\   ?得继续看一看
print(re.search(r"\\", "abc12de\\3f45GH"))
