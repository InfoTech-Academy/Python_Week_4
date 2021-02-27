import addition as add, subtution as subb
import multiply as multi, division as div

control=True
while control:
    print("\n\t 1 for addition\n\t 2 for subtution\n\t 3 for multiply\n\t 4 for division ")
    
    try:
       your_action=input("Please select an action: ")
       number1=input("please enter first number: " )
       number2=input("please enter second number: " )
       if number1=="" or number2=="":
           raise Exception("You can not input nothing")
       elif int(number1)<=0 or int(number2)<=0:
           raise Exception("Your numbers should be greater than 1 ")
               
    
    except ValueError:
        print("It should be an integer")
    except Exception as exc:
        print(exc)
        
    else:
        number1, number2=int(number1), int(number2) 
        
        if your_action=="1":
            add.addition(number1,number2)
        elif your_action=="2":
            subb.subtution(number1,number2)
        elif your_action=="3":
            multi.multiply(number1,number2)
        elif your_action=="4":
            div.division(number1,number2)
        else:
            print("Please check your action")
            
           
        while True:
           try:
               your_action1=input("Do you want to continue (Y/N) ?")
               if your_action1=="Y":
                   break
               elif your_action1=="N":
                   print("See you")
                   control=False
                   break
                
               elif your_action1 != "Y" or your_action1 != "N":
                   raise Exception("Please choise only Y or N: ")
            
           except Exception as excp:
               print(excp)