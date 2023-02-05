import requests
import json
cityName = input('Enter City Name:')
url = 'https://api.openweathermap.org/data/2.5/weather?q='+ cityName +'&appid=492ac9c5809a30780347397e338e8d00&units=metric'
x = requests.get(url)
y = x.json()
if y["cod"]!="404":
    z = y["main"]
    print(z["temp"])
else:
    print('City name not found!')