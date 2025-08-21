import getpass

def main():

    password = getpass.getpass("Set a password: ")
    input("Press enter to continue")
    check_password(password)

def check_password(p):
    guess = input("Guess the password: ")
    if p == guess:
        print("You knew the password! CONGRATULATIONS")
    
    if guess != p:
        print("You are dumb because you don't know your own password")
    print("The program has ended")

main()

