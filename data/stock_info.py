
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
    
class SuggestStock(object):
    
    def __init__(self):
        
        self.stockName = ''
        
        self.stockId = None
        
        self.name = ''
        
        self.date = None
        
        self.company = ''
        
    def toJson(self):
        
        return {
        
            'stockName': self.stockName,
            'stockId': self.stockId,
            'name': self.name,
            'date': self.date,
            'company': self.company,
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
    
        obj = SuggestStock()
        
        obj.stockName = jsonvalue['stockName']

        obj.stockId = jsonvalue['stockId']

        obj.name = jsonvalue['name']

        obj.date = jsonvalue['date']

        obj.company = jsonvalue['company']
        
        return obj