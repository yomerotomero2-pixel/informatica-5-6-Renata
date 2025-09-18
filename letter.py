def main():
    guests_list = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]    #we created a list 
    for receiver in guests_list:                     #a for loop with the variable receiver will look in the list guests_list index 0,1 and so on
        if receiver != "Princess Peach":                  #so if the sender is not princess peach 
            print_letter("Princess Peach",receiver)                 # we create a function to print the letter including Princess Peach and receiver from the guests_list

def print_letter(sender,receiver):                      #we define the function to print the letter
        print(f"""                                                  
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},                                            
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
""")                                                           #f is when we print variables inside the string
                                                                   #curly brackets are for variables inside a string
    
main()