#---------------------------------------------------------
# Name   : Islam Mohamed Mohamed 
# SW     : Calculator App Using GUI Tkinter + Exception Handling + File Handling by storing the Calculations history 
# Date   : 26 Dec 2021
# Version: V 1.0
#------------------------------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter as tk


window = Tk()
window.geometry('500x500+500+150')
window.title('Calculator')
e = Entry(window, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


def buttonClick(number):
    
    # To get the first digit and store it 
    current = e.get() 
    
    # Deleting the command history
    e.delete(0,END) 
    
    # combining multiple digits
    e.insert(0,str(current)+ str(number)) 

def buttonAddition():
    
    f_num = e.get()
    e.delete(0,END)
    global first_number
    global operation
    operation = "+"
    try:
        first_number = int(f_num)
    except ValueError:
        print("Please Enter a Number")
    

def buttonSubtraction():
    f_num = e.get()
    e.delete(0,END)
    global first_number
    global operation
    operation = "-"
    try:
        first_number = int(f_num)
    except ValueError:
        print("Please Enter a Number")
    

def buttonMultiply():
    f_num = e.get()
    e.delete(0,END)
    global first_number
    global operation
    operation = "*"
    try:
        first_number = int(f_num)
    except ValueError:
        print("Please Enter a Number")
    

def buttonDivision():
    f_num = e.get()
    e.delete(0,END)
    
    global first_number
    global operation
    operation = "/"
    try:
        first_number = int(f_num)
    except ValueError:
        print("Please Enter a Number")
    



def buttonEqual():
    second_num = e.get()
    e.delete(0,END)
    
    try:
        second_number = int(second_num)
    
    except ValueError:
        print("Please Enter a Number")
    
    except:
        print("random Error Happened")
    
    if operation == "+":
        e.insert(0,first_number + second_number)
        file=open('calculations_history.txt','a')
        file.write(f"\nThe result of {first_number} + {second_number} is {e.get()}")
        file.close()
    
    if operation == "-":
        e.insert(0,first_number - second_number)
        file=open('calculations_history.txt','a')
        file.write(f"\nThe result of {first_number} - {second_number} is {e.get()}")
        file.close()
    if operation == "*":
        e.insert(0,first_number * second_number)
        file=open('calculations_history.txt','a')
        file.write(f"\nThe result of {first_number} * {second_number} is {e.get()}")
        file.close()
    if operation == "/":
        try:
            e.insert(0,first_number / second_number)
            file=open('calculations_history.txt','a')
            file.write(f"\nThe result of {first_number} / {second_number} is {e.get()}")
            file.close()
        except ZeroDivisionError:
            e.insert(0,'Can not divide by zero')
            print("Here is Zero Division Error")

def buttonClear():
    
    # Deleting the command history "Clearing"
    e.delete(0,END) 


# Number Buttons Definition
button_0 = Button(text='0', padx=30, pady=10,command= lambda: buttonClick(0))
button_1 = Button(text='1', padx=30, pady=10,command= lambda: buttonClick(1))
button_2 = Button(text='2', padx=30, pady=10,command= lambda: buttonClick(2))
button_3 = Button(text='3', padx=30, pady=10,command= lambda: buttonClick(3))
button_4 = Button(text='4', padx=30, pady=10,command= lambda: buttonClick(4))
button_5 = Button(text='5', padx=30, pady=10,command= lambda: buttonClick(5))
button_6 = Button(text='6', padx=30, pady=10,command= lambda: buttonClick(6))
button_7 = Button(text='7', padx=30, pady=10,command= lambda: buttonClick(7))
button_8 = Button(text='8', padx=30, pady=10,command= lambda: buttonClick(8))
button_9 = Button(text='9', padx=30, pady=10,command= lambda: buttonClick(9))

# Operation Buttons Deifinition
button_add = Button(text='+',padx=30,pady=10 ,command=buttonAddition, fg='red')
button_subtract = Button(text='-',padx=30,pady=10 , command=buttonSubtraction, fg='red')
button_multiply = Button(text='*',padx=30,pady=10 , command=buttonMultiply, fg='red')
button_divide = Button(text='/',padx=30,pady=10 , command=buttonDivision, fg='red')
button_equal = Button(text='=',padx=30,pady=10 , command=buttonEqual, fg='red')
button_clear = Button(text='Clear',padx=30,pady=10 , command=buttonClear, fg='red')

# Number Buttons On Screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

# Operations Buttons on screen
button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)

button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)

window.mainloop()
