# A simple calculator app made by following a Codemy course and with TKinter

from tkinter import *

root = Tk()
root.title('Calculator')

# Calculator display
display = Entry(root, width=30, justify='right')
display.grid(row=0, column=0, columnspan=3)

# Adds a number on the display via on screen buttons
def addNumber(number):
    # Variable containing previously entered numbers
    currentNumber = display.get()
    # Clearing the screen
    display.delete(0, END)
    # Adding new number to previous as a string
    display.insert(0, str(currentNumber) + str(number))

# Clears calculator display
def clearDisplay():
    # Clearing the screen
    display.delete(0, END)

btn_clear = Button(root, text='CLR', padx=32, pady=20, command=clearDisplay).grid(row=1, column=0)
btd_add = Button(root, text='+', padx=39, pady=20).grid(row=1, column=4)

btn_equals = Button(root, text='=', padx=39, pady=20).grid(row=5, column=4)

btn1 = Button(root, text='1', padx=40, pady=20, command=lambda: addNumber(1)).grid(row=4, column=0)
btn2 = Button(root, text='2', padx=40, pady=20, command=lambda: addNumber(2)).grid(row=4, column=1)
btn3 = Button(root, text='3', padx=40, pady=20, command=lambda: addNumber(3)).grid(row=4, column=2)

btn4 = Button(root, text='4', padx=40, pady=20, command=lambda: addNumber(4)).grid(row=3, column=0)
btn5 = Button(root, text='5', padx=40, pady=20, command=lambda: addNumber(5)).grid(row=3, column=1)
btn6 = Button(root, text='6', padx=40, pady=20, command=lambda: addNumber(6)).grid(row=3, column=2)

btn7 = Button(root, text='7', padx=40, pady=20, command=lambda: addNumber(7)).grid(row=2, column=0)
btn8 = Button(root, text='8', padx=40, pady=20, command=lambda: addNumber(8)).grid(row=2, column=1)
btn9 = Button(root, text='9', padx=40, pady=20, command=lambda: addNumber(9)).grid(row=2, column=2)

btn0 = Button(root, text='0', padx=90, pady=20, command=lambda: addNumber(0)).grid(row=5, column=0, columnspan=2)



root.mainloop()