import requests
import json
city = input("Enter the name of city: ")



url = f"https://api.weatherapi.com/v1/current.json?key=7e4830ab06ae4510b9e170735232405&q={city}"


r = requests.get(url)
# print(r.text)

dictt = json.loads(r.text)
print(dictt["current"]["temp_c"],["location"]["region"])