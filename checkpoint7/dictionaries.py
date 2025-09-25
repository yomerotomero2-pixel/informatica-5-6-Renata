#dictionary:   word: meaning 
            #  key:value

capitals = {                                             #we are making a dictionary
    "Mexico": "Mexico City",                             #Mexico is the key and the capital mexico city is the value
    "Canada":  "Ottawa",                          #the commas are important
    "Brazil":  "Brasilia",                                   #in the matrix we needed the index to acces one specific element, in the dictionaries instead of indexes we are just going to put the name
    #"Canda":   "Montreal"  use unique keys
}     

capitals["Italy"]  = "Rome"                               #this is to add a new element to the dictionary
del capitals["Brazil"]                                            #this is to delete an element
capitals.pop("Canada")                           #this is another way to delete using the method .pop
capitals.clear()                        #this is to erease everything in the dictionary


# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

student = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for element in student:
    print(f"{element["name"]}, {element["house"]},{element["patronus"]}")

# for key in students:
    #print(f"{key}: {students[key]}")                 #print the key and the value of the key

#print(capitals["Canada"])                    #in the square brackets instead of index we put what we want it to return