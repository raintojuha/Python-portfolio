# A simple calculator app
# Done by following a Codemy.com course
# Refinements made by me

from tkinter import *

class Calculator:
    def __init__(self) -> None:
        pass

    def start(self):
        self.root = Tk()
        self.root.title('Calculator')

        # Calculator display
        self.display = Entry(self.root, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # BUTTONS
        # math operators
        self.btn_divide = Button(self.root, text='/', padx=39, pady=20, command=lambda:mathOperation(self, 'divide')).grid(row=1, column=4)
        self.btn_multiply = Button(self.root, text='*', padx=39, pady=20, command=lambda:mathOperation(self, 'multiply')).grid(row=2, column=4)
        self.btn_subtract = Button(self.root, text='-', padx=39, pady=20, command=lambda:mathOperation(self, 'subtract')).grid(row=3, column=4)
        self.btd_add = Button(self.root, text='+', padx=39, pady=20, command=lambda:mathOperation(self, 'add')).grid(row=4, column=4)
        

        # utilities
        self.btn_clear = Button(self.root, text='CLR', padx=32, pady=20, command=lambda:clearDisplay(self)).grid(row=1, column=0)
        self.btn_equals = Button(self.root, text='=', padx=39, pady=20, command=lambda:equals(self)).grid(row=5, column=4)

        # numpad
        self.btn1 = Button(self.root, text='1', padx=40, pady=20, command=lambda: addNumber(self, 1)).grid(row=4, column=0)
        self.btn2 = Button(self.root, text='2', padx=40, pady=20, command=lambda: addNumber(self, 2)).grid(row=4, column=1)
        self.btn3 = Button(self.root, text='3', padx=40, pady=20, command=lambda: addNumber(self, 3)).grid(row=4, column=2)

        self.btn4 = Button(self.root, text='4', padx=40, pady=20, command=lambda: addNumber(self, 4)).grid(row=3, column=0)
        self.btn5 = Button(self.root, text='5', padx=40, pady=20, command=lambda: addNumber(self, 5)).grid(row=3, column=1)
        self.btn6 = Button(self.root, text='6', padx=40, pady=20, command=lambda: addNumber(self, 6)).grid(row=3, column=2)

        self.btn7 = Button(self.root, text='7', padx=40, pady=20, command=lambda: addNumber(self, 7)).grid(row=2, column=0)
        self.btn8 = Button(self.root, text='8', padx=40, pady=20, command=lambda: addNumber(self, 8)).grid(row=2, column=1)
        self.btn9 = Button(self.root, text='9', padx=40, pady=20, command=lambda: addNumber(self, 9)).grid(row=2, column=2)

        self.btn0 = Button(self.root, text='0', padx=90, pady=20, command=lambda: addNumber(self, 0)).grid(row=5, column=0, columnspan=2)
        # END OF BUTTONS

        # Tkinter main loop
        self.root.mainloop()

# Adds a number on the display via on screen buttons
def addNumber(self, number):
    # Variable containing previously entered numbers
    currentNumber = self.display.get()
    # Clearing the screen
    self.display.delete(0, END)
    # Adding new number to previous as a string
    self.display.insert(0, str(currentNumber) + str(number))

# Clears calculator display
def clearDisplay(self):
    # Clearing the screen
    self.display.delete(0, END)

def mathOperation(self, op):
    # Read the number currently on display
    firstNumber = self.display.get()
    # Global variable for the first number
    global f_num
    # Store the first number to the variable as an int
    f_num = int(firstNumber)
    # Global variable for the math operation
    global operation
    # Storing the operation
    if op == 'add':
        operation = 'addition'
    if op == 'subtract':
        operation = 'subtraction'
    if op == 'multiply':
        operation = 'multiplication'
    if op == 'divide':
        operation = 'division'
    # Clear the display for the second number
    clearDisplay(self)

# When the '=' button is clicked
def equals(self):
    # Get the second number on the display
    secondNumber = self.display.get()
    clearDisplay(self)

    if operation == 'addition':
        self.display.insert(0, f_num + int(secondNumber))
    elif operation == 'subtraction':
        self.display.insert(0, f_num - int(secondNumber))
    elif operation == 'multiplication':
        self.display.insert(0, f_num * int(secondNumber))
    elif operation == 'division':
        self.display.insert(0, f_num / int(secondNumber))
    else:
        self.display.insert(0, 'ERR!')


# Create new calculator instance
c = Calculator()
# Invoke start() function
c.start()