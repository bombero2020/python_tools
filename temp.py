import requests
from pprint import pprint

debug__ = False


def get_all_data():
    """ 'main': { 'humidity': 72,
                  'pressure': 1017,
                  'temp': 278.05, in Kelvins
                  'temp_max': 280.37,
                  'temp_min': 276.48},
    """
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Madrid,es&APPID=45d2d8a0c4c58025df4d1f0472d9e1d1')
    if debug__ is True:
        pprint(r.json())
    return r


def get_temperature():
    r = get_all_data()
    if debug__ is True:
        pprint(r.json()['main'])
    temp_celcius = r.json()['main']['temp']-273.15
    relative_hum = r.json()['main']['humidity']
    temp.config(text="Temp: {} ºC \n Hum: {}%".format(round(temp_celcius), relative_hum))
    temp.after(3600, get_temperature)
    # print(temp_celcius)
    # return temp_celcius


def get_humidity():
    r = get_all_data()
    if debug__ is True:
        pprint(r.json()['main'])
    humidity = r.json()['main']['humidity']
    # print(humidity)
    return humidity


import time
from tkinter import *


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


root = Tk()
clock = Label(root, font=("times", 85, "bold"), bg="white")
clock.grid(row=0, column=1)
tick()
temp = Label(root, font=("times", 65, "bold"), bg="white")
temp.grid(row=1, column=1)
get_temperature()


root.mainloop()

# r.json().main
# pprint(r.json()['main']['temp'])

# get_humidity()