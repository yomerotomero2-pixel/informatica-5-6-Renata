def main():
    integer = int(input("Enter an integer number: "))
    if integer % 5 == 0 and integer % 3 == 0:
        print("FizzBuzz")
    elif integer % 3 == 0:
        print("Fizz")
      
    elif integer % 5 == 0:
        print("Buzz")
    
   

main()