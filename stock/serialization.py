from pymongo import MongoClient
import json
from data.stock_unit import Stock

def loadFromDB():
    
    stocks = []

    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

    client = MongoClient(uri)

    db = client["recommond"]
    
    coll = db['stocks']
    
    results = coll.find({}, {'_id': 0})

    for r in results:
        
        stocks.append(Stock.fromJson(r))

    return stocks