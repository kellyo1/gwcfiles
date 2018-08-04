#prints hello world
#print("Hello world!")

answer = input("Who inspires you? ")
print(answer, "inspires you!")

value = True
anothervalue = False
yetanothervalue = True

print("& ", value & anothervalue)
print("^ ", value ^ anothervalue)
print("== ", value == yetanothervalue)


i = 0
while i < 5:
    print(i)
    i += 1

for i in range(5):
    print(i)

i = -1
while True: # While the following is true
        i += 1 # Increment i by 1
        if(i >20): #If i > 20 then
            break #Stop the loop

        # i is odd
        if(i % 2 == 1): # if i is odd then
            continue #ignore the rest of the loop and start the loop over

        print(i)
