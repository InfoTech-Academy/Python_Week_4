#The Least Common Multiple
#As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
#So that I can find the least common multiple (L.C.M.) of my inputs.

from math import gcd

user_numbers=[]

while len(user_numbers)<=3:
    try:
        values=(input("Please enter your number : "))
        if values=='':
           raise Exception("You have to enter a number")
        
        elif int(values)<=0:
            raise Exception("You have to enter a pozitif number")
        
    except ValueError:
        print("Your input`s type should be integer")
    except Exception as exc:
        print(exc)
    else:
        user_numbers.append(int(values))
        
lcm = user_numbers[0]

for i in user_numbers[1:]:
    lcm = lcm * i // gcd(lcm, i)

print("LCM of",user_numbers, "is:", lcm)            