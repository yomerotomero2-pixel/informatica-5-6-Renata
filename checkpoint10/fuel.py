def main():
    fuel()

def fuel():
    condition =True
    while condition:            #while true means the loop is going to be infinite, because if the user put an error we want it to repeat again and again
        try:
            fuel = input("Write in fraction how much fuel is in your tank? ").split("/")
            print(fuel)
            num = int(fuel[0])
            den = int(fuel[1])
            percentage = round((num / den)*100)
            if percentage > 100:
                print("Invalid input. Fuel capacity cannot be larger than 100%")
            elif percentage >= 99:
                print("F")
                condition = False      #this is to break the while loop
            elif percentage <= 1:
                print("E")
                condition = False
            else:
                print(f"{percentage}%")
                condition = False
        except (ZeroDivisionError,IndexError):
            #pass    #pass means nothing but except cannot be empty thats why we use pass
            print("invalid fraction")
        except ValueError:
            print("Please type numbers instead of words")
        

            

main()