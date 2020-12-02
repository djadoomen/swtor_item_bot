import pymongo,re,json
from os import getenv
from dotenv import load_dotenv

load_dotenv()
_URI = getenv('MONGO_URI')
_DB = getenv('MONGO_DB')
_COLL = getenv('MONGO_COLLECTION')

mConnection = pymongo.MongoClient(_URI)
mDatabase = mConnection[_DB] # Specify the Database
mCollection = mDatabase[_COLL] # Specify the Collection

def search_db(search_subject):
    sss = search_subject.split()
    q_base = '{"$and":['
    for s in sss:
        s = s.replace("(",".")
        s = s.replace(")",".")
        q_base += '{"Name": {"$regex":"'+ s +'","$options":"i"}}'
        q_base += ','
    q_base = q_base.rstrip(",")
    q_base += ']}'
    query = json.loads(q_base)
    return mCollection.find(query,{"Name":1, "Id":1}).limit(10)

def getOne(id):
    query = json.loads('{"Id": "'+ id +'"}')
    print(query)
    return mCollection.find_one(query)
