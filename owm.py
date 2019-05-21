import requests
import time
import os
import sys

city = sys.argv[1]
interval = int(sys.argv[2])

def get_weather(loc):
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=23a8e5b6d7a5c5e91b7c93a703c196bb" % (loc)
    weather = requests.get(url)
    return weather.json()

while(True):
    full = get_weather(city)
    if full['main']['humidity'] < 80:
        print(full['main']['humidity'])
        os.system("echo Air humidity below 80% | wall")
    time.sleep(interval)