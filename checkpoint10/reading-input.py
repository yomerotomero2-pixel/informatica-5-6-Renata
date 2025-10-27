def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)

def read_input(prompt,small,large): # Inserting parameters
    try:
        x = int(input(prompt))
        if 5 < x < 10:
           return x
        else:
           print("Please type a number BETWEEN",small,"and",large) # this is when the numbers the user type are not between 5 and 10
    except ValueError:
       print("Please type a NUMBER between",small, "and",large) # , sings are for concatanate the numbers

  

main()