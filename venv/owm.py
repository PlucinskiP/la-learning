import requests
import sys
import time


city = sys.argv[1]
interval = int(sys.argv[2])

print(city)
print(interval)

def get_weather(loc):
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=23a8e5b6d7a5c5e91b7c93a703c196bb" % (loc)
    weather = requests.get(url)
    return weather.json()


full = get_weather(city)

print(full)
#time.sleep(interval)