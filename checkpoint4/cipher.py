def main():                                                    #This is the main function
    message = input("Enter a message: ").lower()             #We ask the user for a message and we want it in lowercase
    encode_message(message)                                    #We execute the function
    


def encode_message(text):                                      #This executes the other function
    alphabet = "abcdefghijklmnopqrstuvwxyz"                     #We create a variable for the alphabet
    cipher = "zyxwvutsrqponmlkjihgfedcba"                      #The other variable for the alphabet backwards 
    new_message = ""                                                #We set the new message variable as nothing so it can rescribe it
    i = 0                                                         #The index is the position of the character and we set it to start from the 0

    while i < len(text):                                          #Now we start the loop while the index is less than text, the message we ask the user 
        char = text[i]                                          #we want the variable char to keep the letter of the text and start in the position of the alphabet 0

        if char in alphabet:
            cipher_index = alphabet.find(char)
            new_message += cipher[cipher_index]
        else:
            new_message += char
        i += 1
    print(new_message)

main()





