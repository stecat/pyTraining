# Author：Steve

age_ste = 25

count = 0
while True:
    if count == 3:
        break
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")

    count += 1

# 优化1：
count1 = 0
while count1 < 3:
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1

if count == 3:
    print("tried too many times, get out!")

# 优化1改进：
count1 = 0
while count1 < 3:
    guess_age = int(input("guess age="))

    if guess_age == age_ste:
        print("bingo!")
        break
    elif guess_age > age_ste:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1

else:      # python里有while...else的语法
    print("tried too many times, get out!")

# 变化，输入3次后可选择继续输入：
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
        continue_confirm = input("继续吗？若不继续请输入n")
        if continue_confirm != 'n':
            count2 == 0
