def main():
    word_list = [
  "banana", "milk", "soda", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "soda", "sourmilk", "sourmilk", "butter", "soda", "chocolate"
]
    count(word_list)

def count(w_list):
    word_dictionary = {}
    for word in w_list:                        #we can name word_list shorter because we can put it as an argument in the () 
        if word not in word_dictionary:
            word_dictionary[word] = 0

        word_dictionary[word] += 1 
    
    print(word_dictionary)
main()