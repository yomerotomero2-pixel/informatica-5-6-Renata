import random
def main():
    assign_letters()
    alphabet = {
    "a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10
}

def assign_letters():
    print("welcome to scrabble!")
    letters = []
    for letter in range(13):
        letters.append((random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])))
    print(f"Your letters are", end=" ")
    for item in letters:
        print(item, end=", ")
    print()
    for attepmt in letters:
       guess1 = input("Type your word (blank to finish the game): ")
       
main()