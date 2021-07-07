# A hangman game based on previous hangman game
# GUI made using TKinter

# Import TKinter
from os import read, wait
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time

# Enables program to read one character at a time
import readchar


class hangman ():
    def __init__(self, word, window) -> None:
        # Store received word
        self.word = word
        # Store received game window
        self.root = window


    def start(self):
        # Label for hangman image
        hangmanLabel = Label()

        # List of spent, wrong letters
        wrongLetters = []
        # Define penalty limit
        penaltyLimit = 7
        # Start counting penalties
        penalty = 0
        # Win status
        hasWon = False
    
        # Format word to underscores
        self.formattedWord = self.formatWord(self.word)


        self.keyboard()
        '''
        while penalty < penaltyLimit and hasWon == False:

            self.drawHangmanGraphic(penalty, hangmanLabel)
            # Print formatted word
            formattedWordLabel = Label(self.root, text=self.formattedWord, font=('Helvetica Bold', 40))
            formattedWordLabel.grid(row=1, column=1)

            wrongLettersLabel = Label(self.root, text=wrongLetters)
            wrongLettersLabel.grid(row=2, column=1)

            self.root.update()

            #self.userInput = ''
            #self.userInput = readchar.readchar()

            
            #Button(text='A', command=lambda:self.userInput('a')).grid(row=3, column=1)

            #self.root.mainloop()
        '''
            
        self.root.mainloop()

    def keyboard(self):
        frame2 = LabelFrame(self.root, text='Choose a letter', padx=5, pady=5)
        frame2.grid(row=4, column=1, padx=10, pady=10)

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
                        
        for x in alphabet:
            Button(frame2, text=x.capitalize(), command=lambda x=x:self.userInput(x), padx=5, pady=5).pack(side=LEFT)

        # SOMETHING YOU ONLY LEARN BY DOING
        # my command=lambda:self.userINput(x) kept returning only ö
        # by placing x=x after lambda the value is taken at the point of function definition


        
    def userInput(self, userInput):
        print(userInput)
        #if userInput not in wrongLetters:
           # if self.checkWord(self.word, self.formattedWord, userInput) == False:
                #penalty += 1
                #wrongLetters.append(self.userInput)
               #print('a')

    

    # 
    # def formatWord(self, word)
    # 
    # Description: Hides letters in a given word.
    # 
    # Parameters:   String      - word of the game
    # 
    # Return:       String      - letters replaced with underscores 
    #
    def formatWord(self, word):
        mystring = ''
        for c in word:
            if c == ' ':
                mystring += ' '
            elif c == '-':
                mystring += '-'
            else:
                mystring += ' _ '

        return(mystring)

    def checkWord(self, word, formWord, letter):
        i = 0
        answer = False
        for x in word:
            if x == letter:
                answer = True
                self.replaceLetter(i, letter)
            i += 1
        return(answer)

    def replaceLetter(self, index, letter):
        self.formattedWord = "".join((self.formattedWord[:index], letter, self.formattedWord[index + 1:]))
    

        
    def drawHangmanGraphic(self, penalty, label):
        # Empty old image
        label.grid_forget()

        # Get new image
        path = 'Projects/minigames/hangmanGUI/images/{}.png'
        self.img1 = ImageTk.PhotoImage(Image.open(path.format(penalty)))

        # Display new image
        label = Label(image=self.img1)
        label.grid(row=0, column=0, columnspan=3)

        
window = Tk()
window.title('Hangman')
#window.update_idletasks
#window.update

game = hangman('object-oriented', window)

game.start()
