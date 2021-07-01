import random
import os
import readchar


formattedWord = ''
penaltylimit = 10

# Main function
def main():
    penalty = 0

    # Get a random word for the game
    wordOfTheGame = str(randomWord()) # cast it as a str

    # Format the word to be printed
    global formattedWord
    formattedWord = formatWord(wordOfTheGame)




    while penalty < penaltylimit:
        printGUI(penalty)  

        # USER INPUT
        #userInput = input("Select a letter")
        print('Select a letter:')
        userInput = ''
        userInput = readchar.readchar()
        #userInput = str(userInput[1])




        if checkWord(wordOfTheGame, formattedWord, userInput) == False:
            penalty += 1


        #END LOOP


        '''
        Global variable - won - true when palyer has won
        while 
        penalty <= penalty limit
        won != true
        
        after loop
        Do you want to continue?
        Y/N
        readchar
        main()'''



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


def replaceLetter(index, letter):
    global formattedWord
    formattedWord = "".join((formattedWord[:index], letter, formattedWord[index + 1:]))
# ENDOF replaceLetter

def printGUI(penalty):
    clearConsole()
    print('HANGMAN GAME')
    print('\n\n')
    printPenaltyBar(penalty)
    print(formattedWord)
#ENDOF printGUI



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
    