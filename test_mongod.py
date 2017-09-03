from pymongo import MongoClient
import storemgr
import json
import time
from recommond_unit import RecommondUnit
from stock.storemgr import loadStock
from stock.stock_unit import Stock

uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

db = client['recommond']

restore = db['recommond_clone']

items = restore.find({'consultor.name':'王广群'}, {'_id':0})

t = time.strptime('2017-08-23T03:29:00', '%Y-%m-%dT%H:%M:%S')

def getTime (value):
    
    return time.strptime(value, '%Y/%m/%d')

for item in items:
    
    unit = RecommondUnit.fromJson(item)

    date = time.strptime(unit.date, '%Y-%m-%dT%H:%M:%S.%fZ')

    stock = loadStock(unit.stockname)
    
    stockunit = Stock.fromJson(stock)
    
    i = 0
    
    for dayvalue in stockunit.dayvalues:
        
        if getTime(dayvalue.date) > date:
            
            break

        i += 1

    firstday = stockunit.dayvalues[i]

    print('ok')
    
    # ruitem = RecommondUnit.__dict__.update(**item)
    
    
    
    