from pymongo import MongoClient

alpha = 0.12

client = MongoClient('localhost', 27017)

db = client["test"]

name = "alpha_increase_%s" % alpha

coll = db[name]

tempitems = coll.find({}, {'_id': 0})

for temp in tempitems:

    print(temp['id'] + ' ' + temp['name'])

