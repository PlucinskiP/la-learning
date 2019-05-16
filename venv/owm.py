import requests
import sys
import time

city: object = sys.argv[1]
interval = int(sys.argv[2])

print(city)
print(interval)

url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=23a8e5b6d7a5c5e91b7c93a703c196bb" % city
print(url)
json_data = requests.get(url).json()
#print(json_data)


while(True):
    json_data = requests.get(url).json()
    print(json_data)
    time.sleep(interval)