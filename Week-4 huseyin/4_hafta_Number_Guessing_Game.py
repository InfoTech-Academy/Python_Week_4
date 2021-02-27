# Number Guessing Game
#As a player, I want to play a game which I can guess a number the computer chooses 
#in the range I chose. So that I can try to find the correct number which was selected by computer.

import time

from random import randint

number1=int(input("Please enter first number :"))
number2=int(input("Please enter second number :"))
random_number=randint(number1,number2)
print(random_number)
count=1
start_time=time.time()

while True:
    target_number=int(input("Please guess the number: "))
    range_to_num=abs(random_number - target_number)
    if target_number==random_number:
        stop_time=time.time()
        print(f"Congratulations, you tried {count} times and your total time is : {round(stop_time-start_time,2)} seconds")
        break
    elif range_to_num <= 10:
        print("You approached")
    elif range_to_num>= 10:
        print ("you moved away from the number")
        
    count+=1
    

