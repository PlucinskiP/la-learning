import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=23a8e5b6d7a5c5e91b7c93a703c196bb"
json_data = requests.get(url).json()
print(json_data)
