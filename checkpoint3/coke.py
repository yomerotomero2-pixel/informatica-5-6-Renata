def main():
    price = 50 
    total_paid = 0
    vending_machine(price, total_paid) 

def vending_machine(price, total_paid):
    while price > 0:
        print(f"Ammount due: {price}")
        pay = int(input("Insert coin: "))

        if pay == 25 or pay == 10 or pay == 5:
            price = price - pay
            total_paid = total_paid + pay
        else:
            print("Not a coin.")

    if total_paid >= 50:
        print("Thanks! Here is your Coke")
        print(f"Here is your change: {total_paid - 50}")

main()








