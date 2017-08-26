
from pymongo import MongoClient

coll = None

class StoreManger(object):

    def __init__(self):
        
        # uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"
        uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
        client = MongoClient(uri)
    
        self.db = client['recommond']
        
        self.coll = self.db['recommond']
        
    def checkUser(self, name, pwd):
    
        usercoll = self.db['users']

        user = usercoll.find({'name': name})

        for u in user:
    
            if u['pwd'] == pwd:
                
                return True

        return False
    
    def saveToDb(self, data):
    
        self.coll.insert_one(data)
        
    def findInfoWith(self, condition):
    
        return self.coll.find(condition, {'_id':0})
        

_instance = None

def intance():
    
    global _instance
    
    if _instance is None:
        
        _instance = StoreManger()
        
    return _instance