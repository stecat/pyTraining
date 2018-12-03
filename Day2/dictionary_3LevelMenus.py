# Author：Steve

# 打印3级菜单

data = {
    "北京": {
        "昌平": {
            "沙河-2": ["sh-3", "sh-3"],
            "a-2": ["a-3", "b-3"]
        },
        "朝阳": {
            "cy-a2": ["cy-3", "cy-3"],
            "cy-b2": ["cy-3", "cy-3"]
        }
    },
    "杭州": {
        "西湖": {
            "翠苑-2": ["翠苑-3", "翠苑-3"],
            "a-2": ["a-3", "b-3"]
        },
        "上城": {
            "qj-a2": ["qj-3", "qj-3"],
            "qj-b2": ["qj-3", "qj-3"]
        }
    }
}
'''
while True:
    for i in data:
        print(i)

    choice = input("选择进入1>>:")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>:")
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入>>3:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("最后一层，按b返回>>:")
                        if choice4 == "b":
                            pass         # pass为占位符
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break
'''


# 新方法,设置flag，每层内部输入q都能退出，思考优化
exit_flag = False

# 打印第一层
while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>:")
    # 选择第一层，打印第二层
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>:")
            # 选择第二层，打印第三层
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入>>3:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t", i4)
                        choice4 = input("已到最后一层，按b返回>>:")

                        if choice4 == "b":
                            pass         # pass为占位符
                        elif choice4 == "q" or choice4 != "b":
                            exit_flag = True

                    elif choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
                    else:
                        print("%s 不在选项中,请重新输入\n" % choice3)
            elif choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
            else:   # 以上都要用elif，如果choice2==b用了if，在次一层退出的时候都会打印下一句
                print("%s 不在选项中,请重新输入\n" % choice2)
    elif choice == "q":
        exit_flag = True

    else:
        print("%s 不在选项中,请重新输入\n" % choice)

