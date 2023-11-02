## Dice Rolling

This Python code simulates rolling one or more six-sided dice and then calculates and displays the total of the rolled dice.

Importing the random module:
```
import random
```
This line imports the random module, which provides functions for generating random numbers. In this code, it will be used to simulate the rolling of dice.

Defining a dictionary `dice_code`:
```
dice_code = {
    1: ("⚀"),
    2: ("⚁"),
    3: ("⚂"),
    4: ("⚃"),
    5: ("⚄"),
    6: ("⚅")
}
```
This dictionary associates each possible outcome of rolling a six-sided die (1 through 6) with a corresponding Unicode character representing the face of the die. These Unicode characters are visually similar to the dots on a standard six-sided die.

Initializing empty lists and variables:
```
dice = []
total = 0
```
`dice` is an empty list that will store the results of rolling the dice.

`total` is initialized to 0 and will be used to keep track of the total sum of the dice rolls.

Prompting the user for the number of dice to roll:
```
num_of_dice = int(input("How many dice?: "))
```
This line asks the user to enter the number of dice they want to roll, and the input is converted to an integer and stored in the `num_of_dice` variable.

Rolling the dice and storing the results in the dice list:
```
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
```
This loop rolls the specified number of dice by generating random integers between 1 and 6 (inclusive) and appends the results to the dice list.

Printing the results of rolling the dice:
```
for die in dice:
    print(dice_code.get(die), end="")
```
This loop iterates through the dice list and uses the `dice_code` dictionary to print the corresponding Unicode character for each roll. The `end=""` argument in the print function ensures that the characters are printed on the same line.

Printing the total sum of the dice rolls:
```
for die in dice:
    total += die
print(f"total: {total}")
```
This loop calculates the total sum of the dice rolls by adding up the values in the dice list and stores the result in the total variable. Finally, it prints the total sum using an f-string.

In summary, this code allows the user to simulate rolling one or more six-sided dice, displays the results of the individual rolls in a visually appealing format, and provides the total sum of the rolled dice.
