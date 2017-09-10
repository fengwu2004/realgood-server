from os import walk
from stock.load import getLines, formatData
from pymongo import MongoClient
import json

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

    coll.remove({})
    
    coll.insert_many(stocks)


def loadStock(stockname):
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['stocks']
    
    results = coll.find({'name':stockname}, {'_id': 0})

    for r in results:
        
        return r

    return None