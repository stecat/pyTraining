# Author：Steve

# 元组tuple只能查不能改，是指指向不变: 2种方法 count以及index

# 使用情况，数据不能被更改的情况，如数据库链接配置


name = ('ste', 'steve')
count_func = name.count("ste")
index_func = name.index("steve")
print(count_func)
print(index_func)

# 元组含列表的情况
tuple_ = ('ste', '1', ['1', '2'])   # 指向不变的意思是元组指向元组内的列表不能改变，而元组内部的列表是可变的
tuple_[2][0] = 'ste'                # 指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的
tuple_[2][1] = 'steve'
print(tuple_)
print(tuple_.count('1'))
