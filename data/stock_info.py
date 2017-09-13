
class SuggestInfo(object):
    
    def __init__(self):
    
        self.suggeststock = None
        
        self.counts = []
        
        self.trends = []
        
    def toJson(self):
        
        return {
            'suggeststock':self.suggeststock.toJson(),
            'counts':self.counts,
            'trends':self.trends
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = SuggestInfo()
        
        obj.suggeststock = SuggestStock.fromJson(jsonvalue['suggeststock'])
        
        obj.counts = jsonvalue['counts']
        
        obj.trends = jsonvalue['trends']
        
        return obj

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
    
class Consultor(object):
    
    def __init__(self):
        
        self.name = ''
        
        self.company = ''
        
    def toJson(self):
        
        return {
            'name':self.name,
            'company':self.company
        }
    
    @classmethod
    def fromJson(cls, jsonvalue) -> Consultor:
        
        obj = Consultor()
        
        obj.company = jsonvalue['company']

        obj.name = jsonvalue['name']
        
        return obj

class SuggestStock(object):
    
    def __init__(self):
        
        self.stockName = ''
        
        self.stockId = None
        
        self.name = ''
        
        self.date = None
        
        self.company = ''
        
    def __eq__(self, other):
        
        if isinstance(other, SuggestStock):
            
            return self.toJson() == other.toJson()
        
        return False
        
    def __hash__(self):
        
        return hash(str(self.toJson()))
        
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