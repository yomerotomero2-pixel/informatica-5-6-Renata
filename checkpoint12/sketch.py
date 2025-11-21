import requests

print("Welcome to our makeup API, we are going to help you find the perfect makeup for you from the brand Maybelline!!!")
skin_tones = {
    "1" : "Light,pale white", 
    "2" : "White, fair",
    "3" : "Medium, white to olive",
    "4" : "Olive, moderate brown",
    "5" : "Brown, dark brown",
    "6" : "Brown, very dark, brown to black"
}
print("\nSkin tone options:")
for key in skin_tones:
    print(f"{key}. {skin_tones[key]}")


user_tone = input("\nSelect your skin tone number: ")
print(f"\nSelected tone: {skin_tones[user_tone]}\n")
 
product = [
    "eyeshadow",
    "lipstick",
    "lip_liner",
    "blush",
    "foundation"
]

print("Available products:")
for p in product:
    print(f"- {p}")

product_choice = input("\nEnter the product you want: ").lower()


web = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"
response = requests.get(web)
products = response.json()

recommendation_rules = {
    "1": ["ivory", "rose", "pink", "light", "soft", "nude"],
    "2": ["nude", "fair", "rosewood", "coral", "light pink", "peach"],
    "3": ["warm", "natural", "honey", "mauve", "peach"],
    "4": ["tan", "caramel", "warm brown", "berry"],
    "5": ["deep", "mocha", "plum", "rich berry"],
    "6": ["espresso", "chocolate", "burgundy", "dark"]
}

makeup= recommendation_rules[user_tone]

recommended_colors = []

for item in products:
    if item["product_type"] == product_choice:
        if item["product_colors"]:
            for color in item["product_colors"]:
                color_name = color["colour_name"].lower()
                if any(k in color_name for k in makeup):
                    recommended_colors.append(color["colour_name"])

print(f"Recommendations for {product_choice} ({skin_tones[user_tone]}):\n")

if recommended_colors:
    for c in set(recommended_colors):
        print(f"- {c}")
else:
    print("No recommended shades found for this product based on your skin tone.")