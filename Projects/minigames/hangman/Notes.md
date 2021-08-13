Hangman
===
A simple game programming exercise

I started learning Python earlier today and have familiarized myself with variables, lists and operators. No user input yet but I'll look into it along the way.

**Final thoughts and first release**. This project reminded myself of our second course into C++ at Kajaani UAS where we made a rock-paper-scissors game. A fun little project finished in two days. Now it's time to release the 1.0 version of this. I'll be back later in life to clean up the code. *hopefully*

### Game logic
First we need to select a word for the player to quess. A more experienced programmer might do an online search for a random word every time but I think I'm going to start with a simple list of 10 words. _Okay I only got 7_.

I made the randomWord() function return one of the words.
**First milestone** the program returns a random word on each run.

I picked words with spaces and dashes in between. When these words are first printed only the letters need to be obstructed. Spaces and dashes need to be printed.

---

Now I need the program to replace the letters with underscores but keep the spaces and dashes. I'll make a new function for this and pass the random word as an parameter.

**Second milestone** another function runs through the word character by character using a for loop.

Characters are added into an empty string as the program progresses. Letters are added as '_', spaces as spaces and dashes as dashes.

---

Next step is to take a character as user input. I'll be using a static character in early testing.

A function needs to check every character in the string and check if they match. I will take the index of this character and slice the word so that the empty character is replaced with the letter.

**Third milestone** the replacing funtion worked as a surprise. I ran the program to check for errors and the function did it's job. Now to add logic to the penalty of not getting the letter right.

I created an integer for the penalties. Drawing a stick figure to be hanged at this point seemed too time consuming.

---

**GUI** at this point I decided to make a function that prints a user interface and clears the terminal screen every time it does so.

This GUI will include the current word and a penalty progress bar.


**Done for the day** Today I started learning Python. The game has functions to return a random word, format that word, check user input and keep track of score.

Tomorrow I'll look into looping the game mechanics and taking user input.
Should be finished by tomorrow.

The most important thing is that I have gained appreciation for Python. Before this I didn't understand why the syntax didn't use curly brackets and semicolons but this language is growing on me.

Good night for now.

---

I couldn't help myself. I added a while-loop that runs as long as the penalty number is lower than the penalty limit. So if the player loses the loop ends. I still need to take into account the player winning the game.

I also added a rudimentary user input. The program asks the player for a letter but at the current state, doesn't check the player input. The player should be only able to input a single letter. Installing *readchar* using *pip* seems like a good option.

```
Juhas-Air:~ juha$ pip3 install readchar
Collecting readchar
  Downloading readchar-3.0.4-py3-none-any.whl (7.0 kB)
Installing collected packages: readchar
Successfully installed readchar-3.0.4
Juhas-Air:~ juha$ 
```

I also need to check if the letter has already been used once.

---

**A new day** the game now informs you when you have lost and it offers a possibility to play again. One problem I've noticed is that the program comes impossible to terminate with *readchar* as it reads ctrl-c command as 'c' input.

The game can now check if the player has won the game. At the end of each loop a checkWinStatus() function is called. The function runs through the formatted word searhing for an underscore. If an underscore is present there are still letters hidden so the players hasn't won and the function returns a False boolean.

**TO DO** used, wrong letters need to be shown to the player. Currently inputting the same letter over and over adds to the penalty. I'll add a list to keep track of used characters and not accept same characters again.

---

The game now checks if the input is *not in* the list of wrong letters. If it is the program runs through the loop without a change.

Only thing now is to make the printed list of wrong letters prettier and visualize the hangman.

Also a longer list of words would be an improvement.

---

**In the future**
- Make a GUI with TKinter for the game
- Make different states of hangman as .git images
- Continue? popup window with yes / no options


### TKinter version
I have been working on this migration for two days and it's not so straight forward as I thought. I'll push my progress up until now and I'm going to take a little time off Python.

I'm learning Python at the same time I'm doing my thesis and this is consuming me. I need to advance my thesis also. So, no updates for a while.

Things I learned up until now;
- I needed to replace the readchar() command taking user input
  - I think it only reads terminal inputs, no good in TKinter
  - I made a keyboard with Nordic alphabet from Buttons for this version

- I need to rethink my program srtucture
  - I want the buttons to indicate what letters have been wrong
    - Different color, disabled?
  - The 'keyboard' Buttons can call the function to check the letter
  - They should also call the function to update the screen
  - No definitive program loop in code
    - Let's use mainloop() from TKinter and have the Buttons call the necessary functions
      - checkLetter; if correct -> replaceLetter, checkWinStatus, updateScreen