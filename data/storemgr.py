
from data.suggest import Suggest, Consultor, SuggestScore
from data import databasemgr

def getStockLevel(stockId:str) -> int:

    items = databasemgr.instance().stockLevels.find({'id':stockId})

    for item in items:

        return item['level']

    return -1

def getConsultorLevel(consultor:Consultor) -> int:

    items = databasemgr.instance().consultorLevels.find({'name':consultor.name, 'company':consultor.company})

    for item in items:

        return item['level']

    return -1

def checkUser(name, pwd):
    
    user = databasemgr.instance().users.find({'name': name})
    
    for u in user:
        
        if u['pwd'] == pwd:
            
            return True
    
    return False

def loadSuggestOfConsultor(name, company) -> [Suggest]:

    items = databasemgr.instance().suggests.find({'name': name, 'company': company}, {'_id': 0})

    results = []

    for item in items:
        
        results.append(Suggest.fromJson(item))

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

def saveSuggests(items: [Suggest]):

    reuslts = []

    for item in items:
        
        reuslts.append(item.toJson())

    databasemgr.instance().suggests.insert_many(reuslts)

def loadSuggests() -> [Suggest]:

    items = databasemgr.instance().suggests.find({}, {'_id': 0})

    results = []

    for item in items:
        
        results.append(Suggest.fromJson(item))

    return results

def loadSuggestsOfDate(date:str) -> [Suggest]:
    
    items = databasemgr.instance().suggests.find({'date':date}, {'_id': 0})

    results = []

    for item in items:
    
        results.append(Suggest.fromJson(item))

    return results

def formatSuggests():
    
    items = databasemgr.instance().suggests.find({}, {'_id': 0})
    
    results = []
    
    for item in items:
        
        obj = Suggest()
        
        obj.stockId = item['stockId']

        obj.date = item['date']

        obj.stockName = item['stockName']
        
        obj.consultor = Consultor.fromJson(item)
        
        results.append(obj.toJson())

    databasemgr.instance().suggestscopy.remove({})
    
    databasemgr.instance().suggestscopy.insert_many(results)
        
        