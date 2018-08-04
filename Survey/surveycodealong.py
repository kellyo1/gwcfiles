import json


questions = [
    "What is your name?",
    "How old are you?" ,
]

keys = ["name", "age"]

list_of_answers= []


done = "No"
while done == "No":
    answers = {}
    for items in range(len(questions)):
        user_answer = input(questions[items])
        answers[keys[items]] = user_answer
    list_of_answers.append(answers)
    finish = input("Are you done? (Yes or No) : ")
    if finish == "Yes":
        done =  "Yes"
    elif finish == "No":
        done = "No"

print(list_of_answers)

#Load data from Json to Python
# file = open("survey.json","r") #open json file for reading
# old_data = json.load(file) #save data frmo file in variable
# # list_of_answers.extend(old_data) #add to my current list
# file.close() #close file

#Write data to Json
file = open("survey.json", "a")

#for look to loop through the list_of_answers and add
#its dictionaries to survey.Json

ans = json.dumps(list_of_answers)
file.write(ans)

file.close()

# data = json.dumps(answers)
#
# print(type(data))
# print(data)
#
#
# answers = json.loads(answers)
# json.dump()
# file.close()
# file.extend()
#
# # file.write("[
# #
# # ]")
# answersToJson = json.dumps(answers)
# print(answersToJson)
