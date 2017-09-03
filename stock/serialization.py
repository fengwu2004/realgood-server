from pymongo import MongoClient
import json
import jsonpickle

def loadFromDB():
    
    stocks = []
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    results = coll.find({}, {'_id': 0})

    strValues = []
    
    for r in results:

        strValue = json.dumps(r)

        strValues.append(strValue)

    for strvalue in strValues:
        
        obj = jsonpickle.decode(strvalue)

        stocks.append(obj)

    return stocks