# pip3 install requests
import requests
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirmed Cases: {data["cases"]} Deaths: {data["deaths"]} Recovered: {data["recovered"]}'
    
    while True:
        print(text)
        time.sleep(60)
        
update()