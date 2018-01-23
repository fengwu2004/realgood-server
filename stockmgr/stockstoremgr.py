from os import walk
from stockmgr.load import getLines, formatData
from data.databasemgr import DatabaseMgr
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

    DatabaseMgr.instance().stocks.remove({})

    DatabaseMgr.instance().stocks.insert_many(stocks)

    result = []

    for stock in stocks:

        unit = dict()

        unit['id'] = stock['id']

        unit['name'] = stock['name']

        result.append(unit)

    DatabaseMgr.instance().stockInfos.remove({})

    DatabaseMgr.instance().stockInfos.insert_many(result)

saveToDB()