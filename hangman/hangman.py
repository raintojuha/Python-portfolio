import random


# Main function
def main():
    print(randomWord())


def randomWord():
    # List of words
    wordList = ['juice box',
                'water bottle',
                'keyboard',
                'car keys',
                'laptop',
                'object-oriented',
                'coffee cup'
                ]
    
    return(wordList[random.randrange(0, 6)])


# Execute main() function
if __name__ == '__main__':
    main()
    