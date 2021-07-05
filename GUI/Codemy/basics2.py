# More Tkinter fundamentals
# 1. Icons, Images and Exit buttons

from tkinter import *

# Python Image Library
from PIL import ImageTk,Image

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
button_quit.pack()

# Images
# define image
my_img = ImageTk.PhotoImage(Image.open('images/scooter.jpg'))
# put image inside label
my_label = Label(image=my_img)
# put label on screen
my_label.pack()



root.mainloop()