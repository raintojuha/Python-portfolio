import random
import os

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




    #START LOOP
    
    printGUI(penalty)  

    # USER INPUT


    if checkWord(wordOfTheGame, formattedWord, 'a') != False:
        print (formattedWord)

    else:
        #ADD penalty
        penalty += 1
        print(penalty)

    #END LOOP



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
    