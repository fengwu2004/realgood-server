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
        
        if filePath.find('.txt') == -1:
            
            continue
        
        stock = formatData(getLines(filePath))
    
        stocks.append(stock.toJson())

    # uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"
    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

    client = MongoClient(uri)

    # client = MongoClient('localhost', 27017)
    
    db = client["recommond"]
    
    coll = db['stocks']

    coll.remove({})
    
    coll.insert_many(stocks)

def loadStock(stockname):
    
    # uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"
    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
    client = MongoClient(uri)
    
    db = client["recommond"]
    
    coll = db['stocks']
    
    results = coll.find({'name':stockname}, {'_id': 0})

    for r in results:
        
        return r

    return None

# saveToDB()