import random
ezra = input("Who does Ezra prefer: Fer, Ximena, Moy, or Magaly? ")
words = ["Fer", "Ximena", "Moy", "Magaly"]

random_word = random.choice(words)
print("His favorite cousin is: ",random_word)
  
while True:
    if random_word == ezra:
        print("Congratulations you guessed his favorite cousin!")
        
    else:
        print("Try again :(")
        break

