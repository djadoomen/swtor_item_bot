import json,pymongo,re
from os import getenv
from dotenv import load_dotenv

load_dotenv()
_URI = getenv('MONGO_URI')
_DB = getenv('MONGO_DB')
_COLL = getenv('MONGO_COLLECTION')

mConnection = pymongo.MongoClient(_URI)
mDatabase = mConnection[_DB] # Specify the Database
mCollection = mDatabase[_COLL] # Specify the Collection

inFile = "Items.json"

with open(inFile) as file:
    lines = file.readlines()
for line in lines:
    line = re.sub(r':(\d{19,}),', r':"\1",', line)
    js_line = json.loads(line)
    query = {"Id": js_line["Id"]}
    inMongo = mCollection.find(query)
    aDoc = 0
    for amount in inMongo:
        aDoc = aDoc+1
    if aDoc == 0:
        ins_success = mCollection.insert_one(js_line)
        print(ins_success.inserted_id)
