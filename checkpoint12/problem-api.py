import requests
print("Welcome to our makeup API, we are going to help you find the perfect makeup for you!!!")
skin_tones = [
    "Type I: Light,pale white", 
    "Type II: White, fair",
    "Type III: Medium, white to olive",
    "Type IV: Olive, moderate brown",
    "Type V: Brown, dark brown",
    "Type VI: Brown, very dark, brown to black"
]
clean_list = "\n".join(skin_tones)
print(f"Skin tones:{clean_list}")
tone = input("Selct your type of skintone: ")
 
product = [
    "eyeshadow",
    "lipstick",
    "eyeliner",
    "mascara",
    "lip_liner"
]
