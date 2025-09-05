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

        if char in alphabet:                                        #check if the character is in the alphabet
            cipher_index = alphabet.find(char)                         #This finds the position of the letter in the alphabet 
            new_message += cipher[cipher_index]                     #This replace the letter with the correspnding letter in the cipher alphabet
        else:                                                      #This is to decide what to do if the condition is false
            new_message += char                                              #It leaves the character as it is if it is not a letter
        i += 1                                                    #Tells the index to move to the next character by incrementing it
    print(new_message)                                                      #This is to print the encode message

main()                                                             #this is to run the function





