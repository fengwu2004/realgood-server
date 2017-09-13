import time

class DayValue(object):
    
    def __init__(self):
        
        self.open = 0
        
        self.close = 0
        
        self.min = 0
        
        self.max = 0
        
        self.date = ''
        
        self.tradeamount = 0
        
        self.tradevolume = 0
        
    def toJson(self):
        
        return {
            'open':self.open,
            'close':self.close,
            'min': self.min,
            'max': self.max,
            'date': self.date,
            'tradeamount': self.tradeamount,
            'tradevolume': self.tradevolume,
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = DayValue()

        obj.open = jsonvalue['open']

        obj.close = jsonvalue['close']

        obj.min = jsonvalue['min']

        obj.max = jsonvalue['max']

        obj.date = jsonvalue['date']

        obj.tradeamount = jsonvalue['tradeamount']

        obj.tradevolume = jsonvalue['tradevolume']
        
        return obj
        
class Stock(object):
    
    def __init__ (self):
        
        self.id = 0
        
        self.name = ''
        
        self.dayvalues = []
        
    def getDayIndex(self, date:str):
    
        t0 = time.strptime(date, '%Y-%m-%dT')
        
        index = 0
        
        for dayvalue in self.dayvalues:
            
            t = time.strptime(dayvalue.date, '%Y/%m/%dT')
            
            if t < t0:
                index += 1
            else:
                break
                
        return index
    
    def toJson(self):
        
        dayvalues = []
        
        for dayvalue in self.dayvalues:
            
            dayvalues.append(dayvalue.toJson())
    
        return {
            'id':self.id,
            'name':self.name,
            'dayvalues':dayvalues
        }
        
        pass
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        if jsonvalue is None:
            
            return None
        
        obj = Stock()
        
        obj.id = jsonvalue['id']

        obj.name = jsonvalue['name']

        obj.dayvalues = []
        
        for item in jsonvalue['dayvalues']:
            
            obj.dayvalues.append(DayValue.fromJson(item))
        
        return obj