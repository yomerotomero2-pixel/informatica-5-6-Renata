def sum_of_row(matrix, row_number: int):
    row = matrix[row_number]            #we are trying to create a list of the row 
    row_sum = 0
    for item in row:
        row_sum = row_sum + item 

    return row_sum

def sum_of_column(matrix, column_number: int):                  #we are just defining the function
    column_sum = 0                                                    #the sum of column will start at 0
    for row in matrix:                                            #the foor loop will check the matrix 4 times for each row      #for each row in matrix
        column_sum = column_sum + row[column_number]                        # I want you to add the first element to the column_sum (0+2)
    return column_sum

def change_value(matrix, row_number, column_number, new_value):
    row = matrix[row_number]
    row[column_number] = new_value                                                       #this is selecting the column in the row that we already choose


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
my_sum = sum_of_row(matrix, 1)
print(my_sum)
my_sum = sum_of_column(matrix,2)
print(my_sum)


print(matrix)
change_value(matrix,2,3,1000)                                       #here we are printing the row, the column and the new value we want to change for 
print(matrix)

# def single_element(matrix,new_number: int):
#     for number in matrix:





