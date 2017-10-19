import time
from pymongo import MongoClient
from data.storemgr import *

def run():
    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
    client = MongoClient(uri)
    
    db = client["recommond"]
    
    coll = db['suggest']
    
    suggeststocks = loadSuggests()
    
    # items = sorted(set(suggeststocks), key = lambda suggeststock: time.strptime(suggeststock.date, '%Y-%m-%d'), reverse = True)
    
    result = set()
    
    for item in suggeststocks:
        
        item.stockName = getStockName(item.stockId)
        
        if item.stockName is not None:
        
            result.add(item)
            
            print(item.toJson())
            
    coll.remove()

    coll.insert_many(list(map(lambda suggest: suggest.toJson(), result)))

run()
    
    