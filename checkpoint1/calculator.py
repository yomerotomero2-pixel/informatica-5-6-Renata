x = input("What is the value of x? ")
y = input("What is the value of y? ")

z = round(float(x) + float(y),2)

# z:, is to add the comma to big numbers like 1000 - 1,000
print(f"{z:,}")