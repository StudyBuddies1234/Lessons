import random

target = random.randint(0,100)
guess = 0

while guess != target:
    guess = int(input("guess: "))
    if target > guess:
        print("Too Small")
    elif target < guess:
        print("Too Large")
                              
print("Correct")
