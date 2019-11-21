import pymongo


def connect_db():
    """Returns an object with the conection"""
    dbClient = pymongo.MongoClient("mongodb://localhost:27017/")

    return dbClient


def create_db(name):
    """At least it needs database_name, collection, and document"""
    db_client = connect_db()
    mydb = db_client[name]
    mycol = mydb["nombres"]
    mydict = {"name": "John", "address": "Highway 37"}
    x = mycol.insert_one(mydict)

    return x


def insert_one(db_name, collection_name, insert):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]
    x = mycol.insert_one(insert)

    return x


def insert_many(db_name, collection_name, insert):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]
    x = mycol.insert_many(insert)

    return x


def find_one(db_name, collection_name):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]

    x = mycol.find_one()
    return x


def find_all(db_name, collection_name):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]

    x = mycol.find()
    return x


def query(db_name, collection_name, myquery):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]

    x = mycol.find(myquery)
    return x


def delete(db_name, collection_name, myquery):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]106.

    x = mycol.delete_one(myquery)
    return x


def update_one(db_name, collection_name, myquery, new_value):
    db_client = connect_db()
    mydb = db_client[db_name]
    mycol = mydb[collection_name]

    x = mycol.update_one(myquery, new_value)
    return x


# CREATE
# new_insert =[dict(name='Faustina Salazar Cabrera', dni='03508254H', phone=628343611, address='Calle Niquel 17,1C',
#                   nss=281277830345, grupo_sangre=''),
#             dict(name='Marcos Gabriel Arizaga Salazar', dni='', phone=None, address='Calle Niquel 17,1C',
#                               nss=0, grupo_sangre=''),
#             dict(name='Amelie Arizaga Salazar', dni='', phone=None, address='Calle Niquel 17,1C',
#                               nss=0, grupo_sangre=''),
#             dict(name='Martha Foronda Coca', dni='03170591H', phone=None, address='Calle Concepcion de la oliva 14, 4A',
#                               nss=281207498574, grupo_sangre='')
#              ]
# insert_Many_result = insert_many('mis_datos', 'nombres', new_insert)
# READ
myquery = {"name": {}}
query_results = find_all('mis_datos', 'nombres')
for query_result in query_results:
    print(query_result)
# UPDATE
# myquery = {"address": "Calle Niquel 17,1C"}
# newvalues = {"$set": dict(address="Canyon 123")}
# update_result = update_one('mis_datos', 'nombres', myquery, newvalues)
# print(update_result.raw_result)
# DELETE
# myquery = {"name": {"$regex": "^J"}}
# delete_results = delete('mis_datos', 'nombres', myquery)
# for dele in delete_results:
#     print(dele)


# all = find_all('mis_datos', 'nombres')
# for one in all:
#     print(one)
# print(x['_id'], x['name'], x['address'])

#
# db_client = connect_db()
# db_list = db_client.list_database_names()
# # print(db_list)
# collections_list = db_client.list_collection_names()
# print(collections_list)
