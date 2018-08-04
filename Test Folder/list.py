food = ["eggs", "banana", "strawberry", "oatmeal", "blueberry"]
#index numer
#         0        1           2           3           4

print(food) #print elements in list

print("Each element in my string:")

for element in food:
    print(element)


last_element = len(food)-1 #4
print(food)
print(food[last_element])


print("The second element in my list is:")
print(food[1]) #how to show what place it is

print("This is the second letter of the third item in the list:")
print(food[2][1]) #you add a second number to get a specific letter from an item

print(len(food))#print length of the list #len = length

print("tacos" in food) #check if tacos is in the list #in = if in the list
print("strawberry" in food) #check if strawberry is in the list

#multiple line comment highlight the text and click command and /

for num in food: #num can be anything, doesn't exactly have to be a number
    print(num)

#the len
for num in range(len(food)): #gives you the same thing as the other for loop
    print(food[num])

anExample = "Lit!"

print("Each character in my string:")

for character in anExample: #this prints out each character like L i t !
    print(character)

print("The third and fourth letter in my string is: ")
print(anExample[2] + anExample[3])

print("The number of characters in my string: ")
print(len(anExample)) #outputs as 4, showing you that the length is 4 characters
#doesn't matter what it is, it just counts the number of characters

print("The number of elements in my list: ")
print(len(food))
print("strawberry" in food)


aExample = "Dorothy"
print("Is rothy in my string:")
print("rothy" in aExample)

print("Is rhty in my string:")
print("rhty" in aExample)
