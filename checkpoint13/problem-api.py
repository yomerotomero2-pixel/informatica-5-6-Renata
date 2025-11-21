import requests        #It asks the data of the API's makeup

print("Welcome to our makeup API, we are going to help you find the perfect makeup for you from the brand Mabelling!!!") #Prints a message 
skin_tones = {                             #A dictionary where the keys are 1 to 6 and the values are the description of the skin tone
    "1" : "Light,pale white", 
    "2" : "White, fair",
    "3" : "Medium, white to olive",
    "4" : "Olive, moderate brown",
    "5" : "Brown, dark brown",
    "6" : "Brown, very dark, brown to black"
}

print("Skin tone options:")       #Prints the title
for key in skin_tones:           #for each key (1,2,3,4,5,6) inside the skin_tones dictionary, this will happen:
    print(f"{key}. {skin_tones[key]}") #It prints the keys of the dictionary and the values of the keys


user_tone = input("Select your skin tone number: ")  #It asks the user to select a number from the skin_tones dictionary
print(f"Selected tone: {skin_tones[user_tone]}")     #This prints the selected tone accesing to the skin_tone dictionary
 
product = [                                  #Defines a list of the products
    "eyeshadow",
    "lipstick",
    "lip_liner",
    "blush",
    "foundation"
]

print("Available products: ")  #It prints another title or subtitle
for p in product:      #This does through each item inside the product
    print(f"- {p}")    #It prints the value of that is a product from the product list

product_choice = input("Enter the product you want: ").lower() #Asks the user for the wanted product and stores it in the product_ choice variable


web = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"   #Products from the maybelline brand
response = requests.get(web)     #It will get the answer from the web variable
products = response.json()      

recommendation = {                #It defines another dictionary and for each number or skin tone it will send color recommendations and it will compare the color from the API and see if it it matches  
    "1": ["ivory", "rose", "pink", "light", "soft", "nude"],
    "2": ["nude", "fair", "rosewood", "coral", "light pink", "peach"],
    "3": ["warm", "natural", "honey", "mauve", "peach"],
    "4": ["tan", "caramel", "warm brown", "berry"],
    "5": ["deep", "mocha", "plum", "rich berry"],
    "6": ["espresso", "chocolate", "burgundy", "dark"]
}

makeup= recommendation[user_tone]      #

recommended_colors = []    #This creates an empty list that will be used to store the names of the matching colors

for item in products:        #It goes through each product that the API sends
    if item["product_type"] == product_choice: #It checks if the product is the same as the user chose
        for color in item.get("product_colors", []): #It takes each color of the product and...
            name = color["colour_name"].lower()  #it takes the name of the color in the API and it store it in the variable name 
            for k in makeup:      #this is the color of product recommended for our skin tone
                if k in name:  #we are checking if the word is inside the color name
                    recommended_colors.append(color["colour_name"])     #if it is found, it is added to the final color list
                    break
# all this is to get the best color in the API for our skin tone

print(f"Recommendations for {product_choice} ({skin_tones[user_tone]}): ")   #It prints the title that shows the product and its description.

if recommended_colors:         #If we find recommended colors
    for color in recommended_colors:     #Then it goes through each color of the final list and...
        print("-", color)     #Prints it
else:
    print("No shades found.")
    