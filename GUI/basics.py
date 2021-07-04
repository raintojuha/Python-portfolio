# TKinter GUI fundamentals
# 1. root window, label, pack()
# 2. Grid system
# 3. Buttons
# 4. Input fields

from tkinter import *

# Function to be called when button is clicked
def buttonClick():
    infoLabel = Label(root, text='Button was pressed')
    infoLabel.grid(row=4, column=0)

def welcomeMessage():
    message = 'Welcome ' + entry.get()
    welcomeLabel = Label(root, text=message)
    welcomeLabel.grid(row=2, column=1)


# Creating the 'root' window
root = Tk()

# Creating a label widget for the root window with some text
myLabel = Label(root, text='I won\'t say Hello World')

# Labels to be placed on a grid
myLabel1 = Label(root, text='My name is')
myLabel2 = Label(root, text='Juha Rainto')

# Button
# fg - foreground color
# bg - background color (doesn't work for me)
# command - function to be executed on click
# padx, pady - button sizing
myButton = Button(root, text='Click this', fg='blue', bg='red', command=buttonClick, padx=10, pady=10)
welcomeButton = Button(root, text='OK', command=welcomeMessage)

# Input field
# bg - background color
# fb - foreground (text) color
# borderwidth - raised border width
entry = Entry(root, width=20)


# Grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)

entry.grid(row=0, column=1)
welcomeButton.grid(row=1, column=1)

# .insert allows you to pre-insert text to an input field
# A bad way to tell the user what they should input
# since the user needs to erase the text before their input.
#entry.insert(0, 'Name')
entry.info('Name')

# Showing the widget on the screen
# pack() also makes the widget as small as possible
# myLabel.pack()

root.mainloop()

