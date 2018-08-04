# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions.
def intro():
    print("My name is Chatbot and I would love to chat with you!")
    print(" ")
    print("So how do you feel today?")
    print(" ")


# --- Put your main program below! ---
def is_valid_input(user_input,valid_responses):
    for responses in valid_responses:
        if user_input == responses:
            return True
    return False

# Choose a response based on the user's input.
def process_input(answer):
    good_list = ["ok , good, great, awesome, ok, okay, fine, so far so good, happy"]

    bad_list = ["bad, horrible, sad, down, unhappy"]

    if is_valid_input(answer,good_list):
        answer1()
    elif is_valid_input(answer,bad_list):
        answer2()
    else:
        answer3()

def answer1():
    print("Me too! :)))")

def answer2():
    print("Aw that too bad! Hope you feel better .~.")

def answer3():
    print("I see, I can totally understand that.")
    print(" ")
    print("Also, I have always wondered if people preferred candy or popcorn at movies.")
    print(" ")
    print("What do you think? Do you like candy or popcorn more?")
    print(" ")

    valid_responses = ["candy", "popcorn"]

    print("I totally agree with you. I love eating that while watching a movie! Fun times")


def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
    print("That's cool!")
    print(" ")
    print(" ")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
