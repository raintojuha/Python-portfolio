# Random number is used to select each word
import random
# OS library enables clearing of the terminal screen
import os
# Enables program to read one character at a time
import readchar


formattedWord = ''
penaltylimit = 10


# Main function
def main():
    # Integer - number of wrong guesses
    penalty = 0

    # Boolean - Has player won
    hasWon = False

    # List of spent, wrong letters
    wrongLetters = []

    # Get a random word for the game
    wordOfTheGame = str(randomWord()) # cast it as a str

    # Format the word to be printed
    global formattedWord
    formattedWord = formatWord(wordOfTheGame)


    while penalty < penaltylimit and hasWon == False:
        # Draw GUI every cycle
        printGUI(penalty, wrongLetters)     
        
        # Take user input
        print('Select a letter:')
        userInput = ''
        userInput = readchar.readchar()

        if checkWord(wordOfTheGame, formattedWord, userInput) == False:
            penalty += 1
            wrongLetters.append(userInput)
        
        hasWon = checkWinStatus()

    printGUI(penalty, wrongLetters)
    printEndMessage(hasWon)



    # for debugging
    #print(wordOfTheGame)


def randomWord():
    # List of words
    wordList = ['juice box',
                'water bottle',
                'keyboard',
                'car keys',
                'laptop',
                'object-oriented',
                'coffee cup',
                'kaara mobiili'
                ]
    
    return(wordList[random.randrange(0, 7)])
    
# ENDOF randomWord

def formatWord(word):
    mystring = ''
    for c in word:
        if c == ' ':
            mystring += ' '
        elif c == '-':
            mystring += '-'
        else:
            mystring += '_'

    return(mystring)
# ENDOF formatWord

def checkWord(word, formWord, letter):
    i = 0
    answer = False
    for x in word:
        if x == letter:
            answer = True
            replaceLetter(i, letter)
        i += 1
    return(answer)
# ENDOF checkWord

def checkWinStatus():
    won = True
    for x in formattedWord:
        if x == '_':
            won = False
    return won


def replaceLetter(index, letter):
    global formattedWord
    formattedWord = "".join((formattedWord[:index], letter, formattedWord[index + 1:]))
# ENDOF replaceLetter

def printGUI(penalty, wrong):
    clearConsole()
    print('HANGMAN GAME')
    print('\n\n')
    printPenaltyBar(penalty)
    print(formattedWord)
    print(wrong)
#ENDOF printGUI

def printEndMessage(won):
    print('\n\n')
    if(won == True):
        clearConsole
        print('*****************')
        print('*You won the game*')
        print('*****************')
    else:
        clearConsole
        print('*****************')
        print('*You lost the game*')
        print('*****************')

    print('\n\n')

    
    input = ''
    while input != 'y' and input != 'n':
        print('Continue? (y/n)')
        input = readchar.readchar()
        print(input)

    if input == 'y':
        main()
    elif input == 'n':
        print('Good bye :D')
    else:
        print('Input not accepted')




def printPenaltyBar(p):
    print('PENALTY:')
    txt = '{} / {}'
    print(txt.format(p, penaltylimit))

    i = 0
    stars = ''
    while i < penaltylimit:
        if i < p:
            stars += '*'
        else:
            stars += ' '
        i += 1
    txt = '[{}]'
    print(txt.format(stars))
# ENDOF printPenaltyBar


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

       


# Execute main() function
if __name__ == '__main__':
    main()
    