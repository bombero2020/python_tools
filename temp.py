import requests, socket
from pprint import pprint

debug__ = False


def get_all_data():
    """ 'main': { 'feels_like': 272.26,
                  'humidity': 72,
                  'pressure': 1017,
                  'temp': 278.05, in Kelvins
                  'temp_max': 280.37,
                  'temp_min': 276.48},
    """
    r = ''
    error = None
    try:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Madrid,es&APPID=45d2d8a0c4c58025df4d1f0472d9e1d1')
    except Exception as e:
        error = e
    if debug__ is True:
        if error:
            print(error)
        else:
            pprint(r.json())
    if error:
        return None
    else:
        return r


def get_temperature():
    r = get_all_data()
    if debug__ is True and r is not None:
        print('##################################')
        print('time: ', time.strftime('%H:%M:%S'))
        pprint(r.json()['main'])
    if r is None:
        temp_celcius = ''
        relative_hum = ''
        feels_like = ''
        temp.config(text="Temp: {} ºC \n Hum: {}% \n Sen: {} ºC".format(temp_celcius, relative_hum, feels_like))
        temp.after(1000 * 3600, get_temperature)
    else:
        temp_celcius = r.json()['main']['temp']-273.15
        relative_hum = r.json()['main']['humidity']
        feels_like = r.json()['main']['feels_like']-273.15
        temp.config(text="Temp: {} ºC \n Hum: {}% \n Sen: {} ºC".format(round(temp_celcius), relative_hum, round(feels_like)))
        temp.after(1000*3600, get_temperature)
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
    time_string = time.strftime("%H:%M:%S\n%d/%m/%Y")
    clock.config(text=time_string)
    clock.after(200, tick)


def get_IP_n_hostname():
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    # print("Hostname: {}".format(hostname))
    # print("IP Address: {}".format(ip_address))
    ip.config(text="IP: {} ".format(ip_address))
    ip.after(1000 * 3600, get_IP_n_hostname)


root = Tk()
root.configure(background='black')
clock = Label(root, font=("times", 65, "bold"), fg="white", bg="black")
clock.grid(row=0, column=1)
tick()
temp = Label(root, font=("times", 45, "bold"), fg="white", bg="black")
temp.grid(row=1, column=1)
get_temperature()
# ip = Label(root, font=("times", 25, "bold"), fg="white", bg="black")
# ip.grid(row=2, column=1)
# get_IP_n_hostname()

root.mainloop()

# r.json().main
# pprint(r.json()['main']['temp'])

# get_humidity()