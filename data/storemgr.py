
from data.recommond_unit import RecommondUnit, ConsultorWithRecommonds, Consultor
from data.stock_info import SuggestStock
from data import databasemgr
from datetime import datetime
from typing import Tuple

def checkUser (name, pwd):
    
    user = databasemgr.instance().users.find({'name': name})
    
    for u in user:
        
        if u['pwd'] == pwd:
            
            return True
    
    return False

def loadSuggestOfConsultor(name, company) -> [SuggestStock]:

    items = databasemgr.instance().suggests.find({'name': name, 'company': company}, {'_id': 0})

    results = []

    for item in items:
        
        results.append(SuggestStock.fromJson(item))

    return results

def getStockName (stockId:str):

    items = databasemgr.instance().stocks.find({'id': stockId}, {'_id': 0})

    for item in items:
        
        return item['name']

    return None

def getStockId(name:str):

    items = databasemgr.instance().stockInfos.find({'name': name}, {'_id': 0})

    results = []

    for item in items:
        
        return item['id']

    return None

def saveSuggests(items: [SuggestStock]):

    reuslts = []

    for item in items:
        
        reuslts.append(item.toJson())

    databasemgr.instance().suggests.insert_many(reuslts)

def loadSuggests() -> [SuggestStock]:

    items = databasemgr.instance().suggests.find({}, {'_id': 0})

    results = []

    for item in items:
        
        results.append(SuggestStock.fromJson(item))

    return results

def loadSuggestsOfDate(date:str) -> [SuggestStock]:
    
    items = databasemgr.instance().suggests.find({'date':date}, {'_id': 0})

    results = []

    for item in items:
    
        results.append(SuggestStock.fromJson(item))

    return results

def formatSuggests():
    
    items = databasemgr.instance().suggests.find({}, {'_id': 0})
    
    results = []
    
    for item in items:
        
        obj = SuggestStock()
        
        obj.stockId = item['stockId']

        obj.date = item['date']

        obj.stockName = item['stockName']
        
        obj.consultor = Consultor.fromJson(item)
        
        results.append(obj.toJson())

    databasemgr.instance().suggestscopy.remove({})
    
    databasemgr.instance().suggestscopy.insert_many(results)
        
        