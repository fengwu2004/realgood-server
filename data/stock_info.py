
class StockInfo(object):
    
    def __init__(self):
        
        self.stockId = None
        
        self.count = 0
        
        self.lasttime = None
    
    def toJson(self):
        
        pass
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        pass