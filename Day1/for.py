# Author：Steve

for i in range(10):
    print("loop:", i)

# 用for跳着输出0，2，4，6，8
for i in range(0, 10, 2):   # 0:从0开始， 10：循环10次， 2：步长，间隔执行语句
    print("loop:", i)

# for代替while
age_ste = 25
for i in range(3):
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")
else:      # python里也有for...else的语法
    print("tried too many times, get out!")


for i in range(3):
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")
    if i == 2:
        continue_confirm = input("继续for吗？若不继续请输入n")
        if continue_confirm != 'n':
            i = 0

count2 = 0
while count2 < 3:
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")
    count2 += 1
    if count2 == 3:
        continue_confirm = input("继续while吗？若不继续请输入n")
        if continue_confirm != 'n':
            count2 = 0


# continue
for i in range(0, 10):
    if i < 5:
        print("loop",i)
    else:
        continue
    print("check loop...")

# 循环套循环,以下会打印60次
for i in range(10):
    print('---------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break
