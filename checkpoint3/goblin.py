import random
print(" Welcome to the goblin game")
print(" The best game ever")
player_name = input("Write your name ")
print(player_name, "Can you find the goblin?")
print("|_||_||_||_||_|")
goblin_position = random.randint(1,5)
keep_trying = True
while keep_trying:
 guessed_position = int(input("Can you gess where the goblin is? "))

 if goblin_position == guessed_position:
    print("You found the goblin!!")
    keep_trying = False
 else: print("The goblin is still hidden")
