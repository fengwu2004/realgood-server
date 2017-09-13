import time
from pymongo import MongoClient
import storemgr

def run():
    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
    client = MongoClient(uri)
    
    db = client["recommond"]
    
    coll = db['suggest']
    
    suggeststocks = storemgr.intance().loadSuggests()
    
    # items = sorted(set(suggeststocks), key = lambda suggeststock: time.strptime(suggeststock.date, '%Y-%m-%d'), reverse = True)
    
    result = []
    
    for item in suggeststocks:
        
        item.stockName = storemgr.intance().getStockName(item.stockId)
        
        if item.stockName is not None:
        
            result.append(item.toJson())
            
            print(item.toJson())
            
    coll.remove()
    
    coll.insert_many(result)
    
    