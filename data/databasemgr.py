from pymongo import MongoClient

_instance = None

_debug = True

class DatabaseMgr(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = DatabaseMgr()

        return _instance
    
    def __init__(self):

        # uri = "mongodb://yanli:9394@localhost:27017/recommond?authMechanism=SCRAM-SHA-1"

        uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
        self.client = MongoClient(uri)
    
        self.db = self.client["recommond"]

    @property
    def consultors(self):

        return self.db['consultors']
    
    @property
    def stocks(self):

        if _debug:

            client = MongoClient('localhost', 27017)

            db = client["recommond"]

            return db['stocks']
        
        return self.db['stocks']

    @property
    def consultorLevels(self):

        return self.db['consultor_level']

    @property
    def stockLevels(self):

        return self.db['stock_level']

    def industry(self):

        return self.db['industry']

    @property
    def suggests(self):
        
        return self.db['suggest']

    @property
    def suggestscopy(self):
        
        return self.db['suggest_copy']

    @property
    def stockInfos(self):

        if _debug:

            client = MongoClient('localhost', 27017)

            db = client["recommond"]

            return db['stockinfo']
        
        return self.db['stockinfo']

    def stockvolumof(self, dt:str):

        client = MongoClient('localhost', 27017)

        db = client["recommond"]

        return db[dt]

    @property
    def users(self):
        
        return self.db['users']