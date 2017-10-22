from os import walk
from stock.load import getLines, formatData
from pymongo import MongoClient
import json

# uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"
uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

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

    db = client["recommond"]
    
    coll = db['stocks']

    coll.remove({})
    
    coll.insert_many(stocks)

    db = client["recommond"]

    collection = db['stockinfo']

    collection.remove({})

    result = []

    for stock in stocks:

        unit = dict()

        unit['id'] = stock['id']

        unit['name'] = stock['name']

        result.append(unit)

    collection.insert_many(result)

saveToDB()