import requests
import json

song = input("What song are you looking for? ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term="+song)
#print(json.dumps(response.json(), indent=2))     #indent 2 because we want space between words

search = response.json()
for result in search["results"]:
    print(result["trackName"],result["artistName"])

city = input("City: ")
response2 = requests.get("https://goweather.xyz/weather/"+city)
print(response2.json())