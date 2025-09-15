def main():
    print(lenght(values()))                               #here we put a function inside the function lenght
    mean(values())
    range_of_list(values())

def values():
    value_list = []                                               #this is the list
    while True:
        value = int(input("Enter a value: "))               #we are going to keep this number the user enters
        if (value != 0):                                           
            value_list.append(value)                                 #then we are going to add it to the list
            print(value_list)
            ordered_list = sorted(value_list)                         #sort is to put the list in order, we needed to create a new list ordered
            print(ordered_list)
            continue                                                   #continue doing the loop
        else:
            break
    return value_list

def lenght(list):
    return len(list)

def mean(list):
    print(sum(list) / len(list))

def range_of_list(list):
    print(max(list) - min(list))

     



main()