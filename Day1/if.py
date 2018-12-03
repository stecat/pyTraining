# Author：Steve

# if循环，判断输入合法

name = input("name:")
password = input("password:")

_name = "steve"
_password = "12"

if _name == name and _password == password:
    print("welcome {user} ".format(user=name))
else:
    print("invalid")
