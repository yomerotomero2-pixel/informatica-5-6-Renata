# import random                      #we are adding a new library

# coin = random.choice(["heads","tails"])                #aqui llamamos a la libreria y estamos usando el metodo choice que va a escoger entre las opciones que estan en los ""
# print(coin)

# number = random.randint(1,10)          #llamamos la libreria y el metodo randint es para escoger un numero random de 1 al 10
# print(number)

# cards = ["jack","queen","king","Ace"]
# random.shuffle(cards)                       #llamamos la libreria y el metodo shuffle cambia el orden de los elementos
# for card in cards:
#     print(card)


# import statistics
# print(statistics.mean([100,90]))    #vamos a imprimir de la libreria de statistics, con el metodo mean el promedio de 100 y 99


import sys        #sys es system es la terminal
import cowsay
try:
    cowsay.cow("Hello, my name is", sys.argv[1]) #un argumento es lo que usa una funcion para hacer que funcione
except IndexError:
    #print("Two few arguments")
    sys.exit()