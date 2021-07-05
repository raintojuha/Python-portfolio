Codemy GUI course
===
These projects have been made by following along Codemy.com YouTube course on Python GUI using TKinter. These are made for the purpose of learning how to make graphical user interfaces with Python. While not fully 'made by me', I aim to understand every line of code and hopefully that will show in the comments.

This course is 183 videos long so we'll see if I'll complete all of these projects.


## Calculator
**Improvement**. The project has all the different math operation in different functions e.g.

```
# When the '+' button is clicked
def addition(self):
    # Read the number currently on display
    firstNumber = self.display.get()
    # Global variable for the first number
    global f_num
    # Global variable for passing the math operator
    global operation
    operation = 'addition'
    # Store the first number to the variable as an int
    f_num = int(firstNumber)
    # Clear the display for the second nuber
    clearDisplay(self)
```
I'll try to unify these into a sungle funtion since the code inside them is the same except the global 'operation' variable. This shoould be easy since this function is called as a lambda from the math buttons.

The calculator is now finished to the point where it needs to be tinkered with but doesn't offer any value in learning. I'll move to the next project on the course. If I end up learning PyQt, I'll propably make a cleaner GUI for the calculator and tweak the code. I won't remember them in the future so here's what I can think of;
- The calculator only takes in integers. If the solution has a desimal point it will encounter an error if you try to do math with it.
    - This needs to be fixed when / if a decimal point button is added.
- The program doesn't check for division by zero.
- You can't chain math operations. e.g. 3+3+3+3 doesn't work, 3 + 3 = 6 + 3 = 9 + 3 = 12 does.
    -  Program need to check if there is a previous solution in memory when usiing math operations.
        - If there is it needs to act like a equals button