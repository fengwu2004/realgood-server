from pymongo import MongoClient

class DatabaseMgr(object):
    
    def __init__(self):
        
        uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
        self.client = MongoClient(uri)
    
        self.db = self.client["recommond"]
    
    @property
    def stocks(self):
        
        client = MongoClient('localhost', 27017)
    
        db = client["test"]
    
        return db['stocks']
        
        return self.db['stocks']


    @property
    def consultorLevels(self):

        return self.db['consultor_level']

    @property
    def stockLevels(self):

        return self.db['stock_level']

    @property
    def suggests(self):
        
        return self.db['suggestcopy']

    @property
    def suggestscopy(self):
        
        return self.db['suggestcopy']

    @property
    def stockInfos(self):
        
        return self.db['stockinfo']

    @property
    def users(self):
        
        return self.db['users']
    
_instance = None

def instance():
    
    global _instance
    
    if _instance is None:
        
        _instance = DatabaseMgr()
        
    return _instance

