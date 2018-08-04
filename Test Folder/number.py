#imports the ability to get a random number
from random import *

#Generates a random integer
aRandomNumber = randint (1, 5)
#For testing: print(aRandomNumber)

guessestaken=0

while True:
    guess = input("Guess a number between 1 and 5 (inclusive): ")

    if not guess.isnumeric(): #checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) #converts a string to an integer

    if guessestaken < 3 & guess > aRandomNumber:
        guessestaken += 1
        print("Close enough, it's lower.")

    if guessestaken < 3 & guess < aRandomNumber:
        guessestaken += 1
        print("Close enough, it's higher.")

    if guessestaken < 3 & guess == aRandomNumber:
        print("You win!")
        break
