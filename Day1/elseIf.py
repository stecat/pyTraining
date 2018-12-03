# Author：Steve

# else if: guess age

age_ste = 25

guess_age = int(input("guess age="))

if guess_age == age_ste:
    print("bingo!")
elif guess_age > age_ste:
    print("think smaller...")
else:
    print("think bigger...")
