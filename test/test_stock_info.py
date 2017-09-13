import time
from pymongo import MongoClient
import storemgr

uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

db = client["recommond"]

coll = db['stockinfo']

items = coll.find({}, {'_id':0})

for item in items:
    
    if len(item['name']) == 1:
        
        print(item['name'])