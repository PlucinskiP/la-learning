#!/home/pawel/PycharmProjects/openweathermap/venv/bin/python
import requests
import sys
import time
import os



city = sys.argv[1]
interval = int(sys.argv[2])
os.system('echo hello hello >humidity.txt')
#print(city)
#print(interval)

def get_weather(loc):
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=23a8e5b6d7a5c5e91b7c93a703c196bb" % (loc)
    weather = requests.get(url)
    return weather.json()

while(True):
    full = get_weather(city)
    m = full['main']
    h = (m['humidity'])
    print(h)
    if h < 80:
        os.system("cat humidity.txt | wall")
    time.sleep(interval)


