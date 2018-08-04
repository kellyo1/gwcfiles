#Functions
#   remove(element) - removes element from the list
#   append(element) - adds an element to the end of the list
#   insert(index, element) - inserts an element in a specific index
#   sort() - sorts the list in ascending order
#   reverse () - reverse the list

list = [7, 16, 81, 40, "fool"]

print(list)

list.remove("fool") #removes fool from list

print(list)

list.append(500)

list.insert(3, "lunchtime")
list.remove("lunchtime")
list.sort()

print(list)

list.reverse()

print(list)
