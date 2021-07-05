# Image Viewer application
# Again, made by following a Codemy class
# This time I'll make the viewer into a Class from the start


from tkinter import *
from PIL import Image,ImageTk

class imageViewer:
    def __init__(self) -> None:
        pass

    def begin(self):
        # Main window
        self.root = Tk()
        # Window title
        self.root.title('Image Viewer')
        # List of images
        self.imageList = self.getImages()
        # Current image index
        self.currentImage = 0
        # Label element for the image
        self.imageLabel = Label()
        
        # Show images
        self.displayImage(0)
        # Display toolbar
        self.toolbar()
        # Display progress bar
        self.progressBar()
        

        # Program main loop
        self.root.mainloop()

    # Make a list of given images
    def getImages(self):
        # Variables for individual images
        img1 = ImageTk.PhotoImage(Image.open('images/scooter.jpg'))
        img2 = ImageTk.PhotoImage(Image.open('images/safari.jpg'))
        img3 = ImageTk.PhotoImage(Image.open('images/town.jpg'))
        img4 = ImageTk.PhotoImage(Image.open('images/fjord.jpg'))
        img5 = ImageTk.PhotoImage(Image.open('images/dragonfly.jpg'))
        # Compile the list
        imageList = [img1, img2, img3, img4, img5]
        # Return the list
        return imageList

    # Display given image
    def displayImage(self, index):
        # Clear old image from screen
        self.imageLabel.grid_forget()
        # Define a image to be displayed
        self.imageLabel = Label(image=self.imageList[index])
        # Put image on screen
        self.imageLabel.grid(row=0, column=0, columnspan=3)
        # Update progress bar
        self.progressBar()
        

    # Toolbar with previous, quit and next buttons
    def toolbar(self):
        backButton = Button(self.root, text='<<', command=self.previousImage).grid(row=1, column=0)
        quitButton = Button(self.root, text='Quit Program', command=self.root.quit).grid(row=1, column=1)
        fwdButton = Button(self.root, text='>>', command=self.nextImage).grid(row=1, column=2)
    
    # A status bar to inform how many images there are
    def progressBar(self):
        txt = 'Image {} out of {}'
        #print(txt.format(self.currentImage + 1, len(self.imageList)))
        progress = Label(self.root, text=txt.format(self.currentImage + 1, len(self.imageList)))
        progress.grid(row=2, column=1)

    # Move to previous image
    def previousImage(self):
        # Check that this isn't the first image in the list
        if self.currentImage > 0:
            # subtract 1 from index
            self.currentImage -= 1
        else: # move to the last image in the list
            self.currentImage = len(self.imageList) - 1
        # Display new image
        self.displayImage(self.currentImage)

    # Move to next image
    def nextImage(self):
        # Check that this isn't the last image in the list
        if self.currentImage < len(self.imageList) - 1:
            # add 1 to index
            self.currentImage += 1
        else: # move to the first image in the list
            self.currentImage = 0
        # Display new image
        self.displayImage(self.currentImage)
        print(self.currentImage)

viewer = imageViewer()
viewer.begin()