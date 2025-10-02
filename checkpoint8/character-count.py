def character_counter(message,dictionary,):                   #defining a function
    for character in message:
        dictionary.setdefault(character, 0)                          #with setdefualt if it doesn't exist it will add the value of the key that is the letter of the message to the dictionary
        dictionary[character] += 1                                         # el setdefault es para agregar keys and values that does not exixt in the dictionary
    print(dictionary)
    #print(len(message))
    print(f"Total of characters: {sum(dictionary.values())}")                    #this is adding the values of the dictionary 


message = input("Enter a message: ")
dictionary = {}
character_counter(message,dictionary,)


#Alternative 1 to know which character is more repeated
values_list = list(dictionary.values())             #this is going to create a list with the values of the dictionary(the numbers)
print(values_list)
largest_number_index = values_list.index(max(values_list))                     #el index nos da un integer con el elemnto que le preguntemos
repeated_character = list(dictionary.keys())[largest_number_index]      #we now create a list with the keys(letters) with [] is to look an element
print(f"The most repeated character is {repeated_character},repeating {dictionary[repeated_character]} times.")


#Alternative 2
largest_number2 = max(dictionary, key=dictionary.get)    #get is going through the dictionary, and the values, el max del value y el key de ese value.
print(f"The most repeated character is {largest_number2}, repeating {dictionary[largest_number2]} times.")






    