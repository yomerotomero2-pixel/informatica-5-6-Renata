birthdays = {
    "Melissa": "March 15",
    "Alyssa": "June 21",
    "Shensi": "March 9"
}

name = input("Enter a name: ")
if name in birthdays:
    print(f"{birthdays[name]} is the birthday of {name}")
else:    
    print(f"We do not have birthday for {name}")
    new_birthday = input("What is their birthday? ")
    birthdays[f"{name}"] = new_birthday
    print("Birthday database updated.")
