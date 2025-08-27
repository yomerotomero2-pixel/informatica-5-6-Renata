condition = True

while condition:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break
    else:
        print(number ** 2)
print("Bye!")