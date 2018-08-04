start = '''
You're in the forest right now and someone is chasing you.
Earlier in the day you had witnessed a murder and now he's after you.
You see a light shining from what looks to be a house.
You run towards it, hoping to hide in there.
In the house there seems to be a bedroom to the left, the kitchen to the right.
Where do you go?
'''

print(start)

print("Type 'bedroom' to go to the bedroom and 'kitchen' to go the kitchen.")

user_input = input()
if(user_input == "bedroom"):
    print("You decide to go to the bedroom to find a hiding place.")
    print("You see an open window! You could possibly climb out. You also see a guitar that you could fight the murderer with. What do you do?")
    print("Type 'open window' to climb out the window. Type 'guitar' to grab the weapon to fight the killer.")
    user_input = input()
    if(user_input == "open window"):
        print("The window is very far from the ground. As you try climbing out, you slip and fall to your death. The end.")
    elif(user_input == "guitar"):
        print("You grab the guitar and as you're observing it, the killer finds you in the bedroom. You use the guitar to defend yourself, knocking out the killer, giving you enough time to escape. The end :D.")
elif(user_input == "kitchen"):
    print("You decide to go to the kitchen to find a hiding place.")
    print("There isn't a hiding place in the kitchen at all! You can either run away out of the house or go to the bedroom.")
    print("What do you want to do? If you would like to run away, type 'run away', if you would like to go to the bedroom, type 'bedroom'.")
    user_input = input()
    if user_input == "run away":
        print("As you run to the front door, you hear the floorboards creak. You know the killer is right behind you. You get stabbed to death by a knife. The end.")
    elif user_input == "bedroom":
        print("You decide to go to the bedroom to find a hiding place.")
        print("You see an open window! You could possibly climb out. You also see a guitar that you could fight the murderer with. What do you do?")
        print("Type 'open window' to climb out the window. Type 'guitar' to grab the weapon to fight the killer.")
        user_input = input()
        if user_input == "open window":
            print("The window is very far from the ground. As you try climbing out, you slip and fall to your death. The end.")
        elif user_input == "guitar":
            print("You grab the guitar and as you're observing it, the killer finds you in the bedroom. You use the guitar to defend yourself, knocking out the killer, giving you enough time to escape. The end :D.")
