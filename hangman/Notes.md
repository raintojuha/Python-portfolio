Hangman
===
A simple game programming exercise

I started learning Python earlier today and have familiarized myself with variables, lists and operators. No user input yet but I'll look into it along the way.

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
