university_fair = {
     "UT PAQUIME":{"cost":1800, "location":16.8 ,"num_majors":4, "official_name": "Universidad Tecnológica de Paquimé"},
     "TEC DE MONTERREY":{"cost":135000,"location":305,"num_majors":45, "official_name": "Tecnológico de Monterrey"},
     "UACJ":{"cost":3800,"location":35.4,"num_majors":8, "official_name": "Universidad Autónoma de Ciudad Juárez"},
     "TEC DE MILENIO":{"cost":1200,"location":300,"num_majors":9, "official_name": "Universidad Tecmilenio"},
     "URN":{"cost":2755,"location":374,"num_majors":3, "official_name": "Universidad Regional del Norte"}
}

def main():
     uni = input("Please type the name of a university: ").upper()
     while uni not in university_fair:
           uni = input("Not found, please try again: ")

import requests
api = requests.get("http://universities.hipolabs.com/search?name=middle&country=turkey")
print(api)
           
                 
          
               
          
          
main()