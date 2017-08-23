from pymongo import MongoClient

uri = "mongodb://yanli:9394@123.207.213.131/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

db = client['recommond']

coll = db['recommond']

coll.insert_one({"name":'abcd'})