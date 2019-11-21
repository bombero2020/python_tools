import datetime
import json
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.admin
# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)


def cargar_Datos(file_name):
    f = open(file_name, 'r')
    my_json = json.load(f)
    print(my_json)
    f.close()

    return my_json


with open('nombres.json', 'r') as fp:
    myjson = json.load(fp)
    print(myjson)

# cargar_Datos('nombres.json')

# print(obj)

# print(datetime.datetime.now())
