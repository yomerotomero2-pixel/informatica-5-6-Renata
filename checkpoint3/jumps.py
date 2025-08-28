def main():
    number = int(input("Enter an even number: "))
    start = 2
    
    while True:
        print (start)
        start += 2
        if start == number:
            print(number)
            break
main()