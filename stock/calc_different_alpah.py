import stock.serialization
from stock.wave_strategy import WaveStrategyUnit
import jsonpickle
from pymongo import MongoClient
from stock.strategy_find_increase import checkInAdjustWave

import json

stocks = stock.serialization.loadFromDB()

results = []

alpha = 0.12

for stock in stocks:
    
    wavaUnit = WaveStrategyUnit(stock, alpha)
    
    if checkInAdjustWave(wavaUnit):
    
        results.append(wavaUnit)

def save():
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    name = "alpha_increase_%s" % alpha
    
    coll = db[name]

    coll.remove({})
        
    v = json.loads(jsonpickle.encode(results))
    
    coll.insert_many(v)
    
save()

