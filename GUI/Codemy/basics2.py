# More Tkinter fundamentals
# 1. Icons, Images and Exit buttons
# 2. Frames
# 3. Radio buttons
# 4. Message box

from tkinter import *

# Python Image Library
from PIL import ImageTk,Image

# Message box
from tkinter import messagebox

root = Tk()
root.title('More Tkinter')

# Adding a program icon
# On a Windows machine this would be displayed
# on the progrgram's top bar
# On a Mac it seems to show an empty file icon
# these aren't common on OS X so I would just leave it out
# root.iconbitmap('images/headphones.ico')

# Exit button
button_quit = Button(root, text='Exit program', command=root.quit)
button_quit.grid(row=0, column=0)

# Images
# define image
my_img = ImageTk.PhotoImage(Image.open('images/scooter.jpg'))
# put image inside label
my_label = Label(image=my_img)
# put label on screen
my_label.grid(row=0, column=1)


# Frame
# Frame allows a grid system and pack() to exist at the same time
# i.e. You can pack() a frame and have a grid inside it
frame = LabelFrame(root, text='Frames and radio buttons', padx=5, pady=5)
frame.grid(row=1, column=0, padx=10, pady=10)

b = Button(frame,text='Not doing much!')
b.pack()


# Radio buttons
# unlike check boxes radio buttons need to be linked
# since only one can be select at a time
# this is done with the variable parameter

# Declare variables for radio buttons
r = IntVar()
a = IntVar()

# You can set a starting value for a radio button variable
r.set('5')

# Radio buttons
# ('value shown to user', 'actual value')

MODES = [
    ('Pepperoni','Pepperoni'),
    ('Cheese','Cheese'),
    ('Mushroom','Mushroom'),
    ('Onion','Onion'),
]


pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(frame, text=text, variable=pizza, value=mode, command=lambda:update(pizza.get())).pack()


# Print initial value
label = Label(frame, text=pizza.get()).pack()

# Function to update value
def update(value):
    label = Label(frame, text=value).pack()

# Radio buttons
#Radiobutton(root, text='Option 1', variable=r, value=1, command=update).pack()
#Radiobutton(root, text='Option 2', variable=r, value=2, command=update).pack()
#Radiobutton(root, text='Option 1', variable=a, value=1).pack()
#Radiobutton(root, text='Option 2', variable=a, value=2).pack()

# Print the values
#label1 = Label(root, text=r.get()).pack()
#label2 = Label(root, text=a.get()).pack()


frame2 = LabelFrame(root, text='Message boxes', padx=5, pady=5)
frame2.grid(row=1, column=1, padx=10, pady=10)

# Message box
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup(type):
    if type == 'info':
        messagebox.showinfo('This is a popup', 'Information')
    if type == 'warning':
        messagebox.showwarning('This is a popup', 'Warning')
    if type == 'error':
        messagebox.showerror('This is a popup', 'Error')
    if type == 'question':
        response = messagebox.askquestion('This is a popup', 'Question')
        Label(frame2, text=response).pack()
    # Response from question message box will be stored to 'response' variable
    # yes -> 'yes'
    # no -> 'no'
    if type == 'okcancel':
        response = messagebox.askokcancel('This is a popup', 'OK / Cancel')
        Label(frame2, text=response).pack()
    # Response from ok/cancel message box will be stored to 'response' variable
    # ok -> 1
    # cancel -> 0
    if type == 'yesno':
        response = messagebox.askyesno('This is a popup', 'Yes / No')
        Label(frame2, text=response).pack()
    # Response from yes/no message box will be stored to 'response' variable
    # yes -> 1
    # no -> 0

Button(frame2, text='Pop up : info', command=lambda:popup('info')).pack()
Button(frame2, text='Pop up : warning', command=lambda:popup('warning')).pack()
Button(frame2, text='Pop up : error', command=lambda:popup('error')).pack()
Button(frame2, text='Pop up : question', command=lambda:popup('question')).pack()
Button(frame2, text='Pop up : okcancel', command=lambda:popup('okcancel')).pack()
Button(frame2, text='Pop up : yesno', command=lambda:popup('yesno')).pack()



root.mainloop()