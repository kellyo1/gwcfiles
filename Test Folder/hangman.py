word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
correctguesses = [] #stores correct guesses
usedLetters = [] #all the letters used
lives = 7 #lives
points = 0

for letters in word:
    correctguesses.append("_")

while True:
	match = False
	used = False
	print("Lives: " +str(lives))
	print("Letters Used: " +str(usedLetters))
	print("Guess: "+ str(correctguesses))

	print(" ")

	guess = input("Guess a letter: ")

	if guess not in usedLetters:
		usedLetters.append(guess)


	for i in range(len(word)):
		if word[i] == guess:
			correctguesses[i:i+1] = guess
			points += 1
			match = True

	if match == False:
		print("Incorrect, please guess again!")
		lives -= 1

	print(correctguesses)

	if points == len(word):
		print("You win!")
		break

	if lives == 0:
		print("You lose!")
		break








    # if (True):
    #     print("That letter is part of the word!")
    #     elif:
    # print("That is not part of the word!")
    # print(guess)
