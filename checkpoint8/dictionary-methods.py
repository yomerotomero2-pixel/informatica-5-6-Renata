dictionary = {
    "Color": "Yellow",
    "age": 17
}

#Values
print(dictionary.values())
for v in dictionary.values():
    print (v)

#Keys
print(dictionary.keys())
for k in dictionary.keys():
    print (k)

#items
print(dictionary.items())
for i in dictionary.items():
    print(i)

#Print key and value using methods
# to do



#Get 
picnic_items = {"apples": 5, "cups": 2}
print(f"I'm bringing {picnic_items.get("cups")} cups.")

print(f"I'm bringing {picnic_items.get("eggs",2)} eggs.")            #with that 2 it can tell how much you need to bring of eggs


#Setting Default Values
pet_info = {
    "name": "Puka",
    "age": 5
}

pet_info.setdefault("color": "black")                    #this is like append
print(pet_info)