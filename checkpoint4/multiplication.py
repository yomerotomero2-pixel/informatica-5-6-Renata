def main():
    number = int(input("Please enter a positive integer number: "))
    multiplication(number)
    
    
def multiplication(number):
    n = 1

    while n <= 10:
        if number > 0:

            table = number * n
            print(f"{number} x {n} = {table}")
            n += 1
        else:
            print("Follow the instructions and write a positive integer number!🤬")
            number = int(input("Please enter a positive integer number: "))
            
            
        
    

        

        
    
        
main()



    
    
    
     