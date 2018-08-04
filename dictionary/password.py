def main():
    #Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
    # file = open("dictionary.txt","w")

    print("Can your password survive a dictionary attack?")

    # name = input("What is your name?")
    # file.append(name)
    #
    # bday = input("What year were you born in?")
    # file.append(bday)
    #
    # file.close()

    file = open("dictionary.txt","r")
    #Take input from the keyboard, storing in the variable test_password
    # NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")

    for strings in file:
        if  strings.strip() == test_password.strip():
            print("That is a strong password.")
            continue
        elif strings.strip() != test_password.strip():
            while strings.strip() != test_password.strip():
                print("That is a weak password.")
                break

#Write logic to see if the password is in the dictionary file below here:

if __name__ == "__main__":
    main()
