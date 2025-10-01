def character_counter(message,dictionary,):                   #defining a function
    for character in message:
        dictionary.setdefault(character, 0)                          #with setdefualt if it doesn't exist it will add the value of the key that is the letter of the message to the dictionary
        dictionary[character] += 1                                         # el setdefault es para agregar keys and values that does not exixt in the dictionary
    print(dictionary)
    print(len(dictionary))


message = input("Enter a message: ")
dictionary = {}
character_counter(message,dictionary,)








    