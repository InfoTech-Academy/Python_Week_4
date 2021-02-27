# Random Password
# Password length must be 10 characters long
#The GUI of program must contain at least a button and a label.


from random import choices as cho, randint as rand, shuffle as shuf
from string import ascii_uppercase as asci
from tkinter import*

symbols=['!','@','#','$','%','^','&','*','.','-']
numbers = ["0","1", "2","3","4","5","6","7","8","9"]

def passw_generator():
    password=[]
    password.extend(cho(symbols,k=3))
    password.extend(cho(asci, k=3))
    password.extend(cho(numbers, k=4))
    shuf(password)
    return ("".join(password))
 

def start():
    message=passw_generator()
    label=Label(text=message)
    label.place(x=75,y=50)
    
window= Tk()
window.title("Password  Generator")
window.configure(background="green")
window.geometry("220x100")

label=Label(window, text="")
label.place(x=90,y=50)

button=Button(window,text="Hit to Generate",command=start)
button.place(x=70,y=10)

window.mainloop()

