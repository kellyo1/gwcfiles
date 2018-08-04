#imports the ability to get a random number
from random import *
aRandomNumber = randint(0,100)

print("This will generate a random number from 0 to 100")
print(aRandomNumber)


#create the list of wods you want to choose from
#this will be a random generator for food (menu)
dinnermenu = ["burgers and fries", "pasta", "soup", "rice and sides"]
dinnersides = ["side salad", "potato fries", "sweet potato fries", "tortilla chips and sauces"]
dessertmenu = ["ice cream", "mochi ice cream", "cake", "nutella crepe"]

aRandomNumber = randint(0,len(dinnermenu)-1)

print("What are you going to eat for dinner today?")
print(dinnermenu[aRandomNumber])

aRandomNumber = randint(0,len(dinnersides)-1)
print("What side should go along with that?")
print(dinnersides[aRandomNumber])

aRandomNumber = randint(0,len(dessertmenu)-1)
print("What dessert are you going to have?")
print(dessertmenu[aRandomNumber])

#Generates a random number
aList = ["flowers", "cherry", "chamomile", "peach-colored", "blowing", "tearing"]
bList = ["begin", "seedling", "flowing", "living", "coffee", "teabag", "latte", "loving", "ending"]
cList = ["sun", "bench", "life", "pass", "end", "breeze", "wind", "side", "like", "sing", "out"]

print("Let's make a haiku :)")

aRandomIndex1 = randint(0, len(aList)-1)
aRandomIndex2 = randint(0, len(aList)-1)
aRandomIndex3 = randint(0, len(bList)-1)
aRandomIndex4 = randint(0, len(bList)-1)
aRandomIndex5 = randint(0, len(bList)-1)
aRandomIndex6 = randint(0, len(cList)-1)
aRandomIndex7 = randint(0, len(cList)-1)
aRandomIndex8 = randint(0, len(cList)-1)
aRandomIndex9 = randint(0, len(cList)-1)
aRandomIndex10 = randint(0, len(cList)-1)
print(aList[aRandomIndex1], aList[aRandomIndex2], cList[aRandomIndex6])
print(bList[aRandomIndex3], bList[aRandomIndex4], bList[aRandomIndex5], cList[aRandomIndex6])
print(cList[aRandomIndex6], cList[aRandomIndex7], cList[aRandomIndex8], cList[aRandomIndex9], cList[aRandomIndex10])
