#import random

#num = random.randint(0,10)
#ans = 0

#while ans != num:
    #ans = int(input("num:"))
    #if ans < num:
        #print("Greater")
    #elif ans > num:
        #print("Less")

#print("Correct")
    
#for number in range(100):
    #if number % 5 == 0 and number % 3 == 0:
        #print("Fizz Buzz")
    #elif number % 5 == 0:
        #print("Buzz")
    #elif number % 3 == 0:
        #print("Fizz")
    #else:
        #print(number)

number = 0
while number <= 100:
    if number % 5 == 0 and number % 3 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    number += 1

