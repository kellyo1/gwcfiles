
#formally name
questions = {}

survey = ['name' : 'What is your name? ',
        'age' : 'How old are you? ',
        'food' : 'What is your favorite food?',
        'color' : 'What is your favorite color?']
key = [,"age","food","color"]

# This is what the terminal will run.

print("This is a survey" "\n")

# for answers in survey:
#     print(survey)

for item in range(len(survey)):
    answer = input(survey[item])
    questions[key[item]] = answer

    print("You said " +answer)

print(questions)
