from pymongo import MongoClient
import json
from data.stock_unit import Stock

def loadFromDB():
    
    stocks = []
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    results = coll.find({}, {'_id': 0})

    for r in results:
        
        stocks.append(Stock.fromJson(r))

    return stocks