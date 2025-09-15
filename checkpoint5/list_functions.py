my_list = [5, 2, 3, 1, 4]
my_list2 = ["a", "b", "c"]
greatest = max(my_list)     #max is to find the greatest value element in a list
print("The greatest number in the list is: ",greatest)

smallest = min(my_list)
print("The smallest number in the list is: ",smallest)

list_sum = sum(my_list)
print("The sum of all numbers in my list is: ",list_sum)

list_lenght = len(my_list)
print("This list has ", list_lenght, "elements.")

in_order = sorted(my_list)       #we copy the same list but changing the order 
print(in_order)                     #functions()     .methods

def filter_price(price):                        #we are defining a function to the filter function
    if(price >= 400):                              #with this function we set the conditions to the filter function
        return True
    else:
        return False


item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price)                         #this content a loop, is another way to set a loop.  We use filter to take out the numbers of the list less than or equal 400
print(list(filtered_price))                                                    #list is a function to convert the filter to lists
