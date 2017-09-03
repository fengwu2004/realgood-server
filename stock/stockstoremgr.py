from os import walk
from stock.load import getLines, formatData
from pymongo import MongoClient
import json
import jsonpickle

def saveToDB():
    
    mypath = '/Users/yan/Desktop/export/'
    
    f = []
    
    for (dirpath, dirname, filenames) in walk(mypath):
        
        f.extend(filenames)
    
    print(f)
    
    stocks = []
    
    for file in f:
    
        filePath = mypath + file
        
        stock = formatData(getLines(filePath))
    
        stocks.append(stock.toJson())
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    coll.insert_many(stocks)


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
    
    for strValue in strValues:
        
        obj = jsonpickle.decode(strValue)
        
        stocks.append(obj)
    
    return stocks

def loadStock(stockname):
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    results = coll.find({'name':stockname}, {'_id': 0})

    for r in results:
        
        strValue = json.dumps(r)

        obj = jsonpickle.decode(strValue)
        
        return obj

    return None