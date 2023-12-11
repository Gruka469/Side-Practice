from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Simple calculator")
root.geometry('600x500')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def devision(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Devision by zero is impossible"
    
def button_add():
    return


button_1 = tk.Button(root, text='1', padx=40, pady=20, command=button_add)
button_2 = tk.Button(root, text='2', padx=40, pady=20, command=button_add)
button_3 = tk.Button(root, text='3', padx=40, pady=20, command=button_add)
button_4 = tk.Button(root, text='4', padx=40, pady=20, command=button_add)
button_5 = tk.Button(root, text='5', padx=40, pady=20, command=button_add)
button_6 = tk.Button(root, text='6', padx=40, pady=20, command=button_add)
button_7 = tk.Button(root, text='7', padx=40, pady=20, command=button_add)
button_8 = tk.Button(root, text='8', padx=40, pady=20, command=button_add)
button_9 = tk.Button(root, text='9', padx=40, pady=20, command=button_add)
button_0 = tk.Button(root, text='0', padx=40, pady=20, command=button_add)


#Adding button grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


root.mainloop()