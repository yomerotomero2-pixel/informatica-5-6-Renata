def main():
    list_lenght = int(input("List lenght: "))
    number_list = []
    for i in range(list_lenght):
        list_element = int(input("Enter element: "))
        number_list.append(list_element)

    print(number_list)
    print(max(number_list))
    file = open("largest.txt","a")
    file.write(f"{number_list}\n")
    file.close()
    
main()