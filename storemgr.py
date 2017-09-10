
from pymongo import MongoClient

from data.recommond_unit import RecommondUnit, ConsultorWithRecommonds
from data.stock_info import SuggestStock


class StoreManger(object):

    def __init__(self):
        
        # uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"
        uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
        client = MongoClient(uri)
    
        self.db = client['recommond']
        
    def checkUser(self, name, pwd):
    
        usercoll = self.db['users']

        user = usercoll.find({'name': name})

        for u in user:
    
            if u['pwd'] == pwd:
                
                return True

        return False
    
    def saveToConsultor(self, dataList):
        
        consultorColl = self.db['consultors']

        consultorColl.insert_many(dataList)
    
    def saveToDb(self, data):
    
        coll = self.db['recommond']
    
        coll.insert_one(data)
        
    def saveManyTo(self, collectionName, datas):
    
        coll = self.db[collectionName]

        coll.remove({})
    
        coll.insert_many(datas)
        
    def findInfoWith(self, condition):
    
        coll = self.db['recommond']
    
        return coll.find(condition, {'_id':0})

    def findInfoIn(self, collectionName, condition):
    
        coll = self.db[collectionName]
    
        return coll.find(condition, {'_id': 0})
    
    def loadConsultors(self) -> [ConsultorWithRecommonds]:
    
        coll = self.db['consultors']

        items = coll.find({}, {'_id': 0})

        results = []

        for item in items:
            
            results.append(ConsultorWithRecommonds.fromJson(item))

        return results
    
    def loadSuggestOfConsultor(self, name, company) -> [SuggestStock]:
    
        coll = self.db['suggest']
        
        items = coll.find({'name':name, 'company':company}, {'_id':0})
        
        results = []
        
        for item in items:
            
            results.append(SuggestStock.fromJson(item))
            
        return results

    def getStockName(self, stockId):

        coll = self.db['stockinfo']

        items = coll.find({'id': stockId}, {'_id': 0})

        results = []

        for item in items:
            
            return item['name']

        return None
    
    def getStockId(self, name):
    
        coll = self.db['stockinfo']
    
        items = coll.find({'name':name}, {'_id': 0})
    
        results = []
    
        for item in items:
            
            return item['id']
    
        return None
    
    def saveSuggests(self, items:[SuggestStock]):
    
        coll = self.db['suggest']
        
        reuslts = []
        
        for item in items:
            
            reuslts.append(item.toJson())
        
        coll.insert_many(reuslts)

    def loadSuggests(self) -> [SuggestStock]:
    
        coll = self.db['suggest']
    
        items = coll.find({}, {'_id': 0})
    
        results = []
    
        for item in items:
            
            results.append(SuggestStock.fromJson(item))
    
        return results
        
_instance = None

def intance():
    
    global _instance
    
    if _instance is None:
        
        _instance = StoreManger()
        
    return _instance