from datetime import datetime

from data.stock import Stock, DayValue
from data.suggest import Suggest, Consultor, SuggestScore
from data.databasemgr import DatabaseMgr

def getStockLevel(stockId:str) -> int:

    items = DatabaseMgr.instance().stockLevels.find({'id':stockId})

    for item in items:

        return item['level']

    return -1

def getConsultorLevel(consultor:Consultor) -> int:

    items = DatabaseMgr.instance().consultorLevels.find({'name':consultor.name, 'company':consultor.company})

    for item in items:

        return item['level']

    return -1

def checkUser(name, pwd):
    
    user = DatabaseMgr.instance().users.find({'name': name})
    
    for u in user:
        
        if u['pwd'] == pwd:
            
            return True
    
    return False

def getStock(stockId:str) -> Stock:

    items = DatabaseMgr.instance().stocks.find({'id': stockId}, {'_id': 0})

    for item in items:

        return Stock.fromJson(item)

    return None

def getStockDayvalue(stockId:str, day:str) -> DayValue:

    stock = getStock(stockId)

    index = stock.getDayIndex(day)

    return stock.getDayValue(index - 1)

def loadSuggestOfConsultor(consultorId:int) -> [Suggest]:

    items = DatabaseMgr.instance().suggests.find({'consultorId': consultorId}, {'_id': 0})

    results = []

    for item in items:
        
        results.append(Suggest.fromJson(item))

    return results

def getStockName(stockId:str):

    items = DatabaseMgr.instance().stocks.find({'id': stockId}, {'_id': 0})

    for item in items:
        
        return item['name']

    return None

def getStockId(name:str):

    items = DatabaseMgr.instance().stockInfos.find({'name': name}, {'_id': 0})

    results = []

    for item in items:
        
        return item['id']

    return None

def saveSuggests(newsuggests: set):

    suggests = loadSuggests()

    for suggest in suggests:

        newsuggests.add(suggest)

    reuslts = list(map(lambda item: item.toJson(), newsuggests))

    DatabaseMgr.instance().suggests.remove({})

    DatabaseMgr.instance().suggests.insert_many(reuslts)

def loadSuggests() -> [Suggest]:

    items = DatabaseMgr.instance().suggests.find({}, {'_id': 0})

    return list(map(lambda item: Suggest.fromJson(item), items))

def loadSuggestsOfDate(date:str) -> [Suggest]:

    suggests = loadSuggests()

    return list(filter(lambda suggest: suggest.date == date, suggests))

def formatSuggests():
    
    items = DatabaseMgr.instance().suggests.find({}, {'_id': 0})
    
    results = []
    
    for item in items:
        
        obj = Suggest()
        
        obj.stockId = item['stockId']

        obj.date = item['date']

        obj.stockName = item['stockName']
        
        obj.consultorId = item['consultorId']
        
        results.append(obj.toJson())

    DatabaseMgr.instance().suggestscopy.remove({})

    DatabaseMgr.instance().suggestscopy.insert_many(results)

def checkIsNewStock(stockId, dtstr:str):

    stock = getStock(stockId)

    if stock is None:

        return True

    index = stock.getDayIndex(dtstr)

    if index <= 10:

        return True

    return False
        