def main():
    food_dictionary = {
        "Whole milk": 73,
        "Almond milk": 30,
        "Yogurt plain low fat ": 77,
        "Sour Cream cultured": 26,
        "Egg": 75,
        "Egg white": 16,
        "Cream cheese": 51,
        "American Pasteurized": 79,
        "Almonds, dry roasted": 170,
        "Peanuts, roasted": 166,
        "Black beans, boiled": 113,
        "Lentils, boiled": 115,
        "Chicken Deli": 20,
        "Catfish, baked": 89,
        "Broccoli": 7,
        "Tomato": 8,
        "Watermellon": 11,
        "Apple": 14,
        "Oatmeal, instant": 77,
        "Quinoa, cooked": 56
    }
    food = input("Type the name of two foods: ").split(",")
    total_calories = 0
    for f in food:
        f = f.capitalize()
        print(food_dictionary[f])
        total_calories += (food_dictionary[f])
        
    print(f"Total of calories:{total_calories}")
    if food[0] == "Watermellon" and food[1] == "Whole milk":
        print("For your own sake milk and watermellon cannot be mixed")
    

main()

