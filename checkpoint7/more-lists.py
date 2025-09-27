#lists with strings
# names = ["Bob", "Alex", "Kevin"]
# names.append("Joseph")

# for name in sorted(names):                     sorted is to put the names in alphabetical order
#     print(name)

#Lists with floats
# measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
# mean = sum(measurements) / len(measurements)
# print("The mean is: ", mean)


#Lists within lists
# super_list = [[5,2,3],[4,1],[2,2,5,1]]
# print(super_list[1][0])                            #if i want to get the first number of the second list i use another index annotation

# grades = [["Shakira", 8, "D"], ["Melissa", 12, "C"], ["Shensi", 10, "A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} from group {group} got a {grade}.")


#Matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Print rows
#print(matrix[0][0])

for column in range(3):
    col = [matrix[row][column] for row in range(3)]
    print(col)
        