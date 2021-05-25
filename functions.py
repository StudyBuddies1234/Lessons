import random

def check_mark(mark):
    if mark > 50:
        return "Pass"
    else:
        return "Fail"

def sum(number):
    number = number ** 2
    number = number / 2
    number = number + 10
    return number

def guess(num):
    ans = 0

    while ans != num:
        ans = int(input("num:"))
        if ans < num:
            print("Greater")
        elif ans > num:
            print("Less")
    


for i in range(100):
    print(check_mark(i))