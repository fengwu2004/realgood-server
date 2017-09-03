class Consultor(object):
    def __init__ (self):
        self.name = None
        
        self.company = None
        
        self.pm = False
    
    def toJson (self):
        return self.__dict__
    
    @classmethod
    def fromJson (cls, jsonvalue):
        obj = Consultor()
        
        obj.name = jsonvalue['name']
        
        obj.company = jsonvalue['company']
        
        obj.pm = jsonvalue['pm']
        
        return obj
    
class RecommondUnit(object):
    
    def __init__(self):
        
        self.consultor = None
        
        self.date = None
        
        self.stockname = None
        
        self.urgent = False
        
        self.amorpm = None
        
    def toJson(self):
        
        return {
            'date':self.date,
            'stockname':self.stockname,
            'urgent':self.urgent,
            'amorpm':self.amorpm,
            'consultor':self.consultor.toJson()
        }

    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = RecommondUnit()
        
        obj.date = jsonvalue['date']

        obj.stockname = jsonvalue['stockname']

        obj.urgent = jsonvalue['urgent']

        obj.amorpm = jsonvalue['amorpm']

        obj.consultor = Consultor.fromJson(jsonvalue['consultor'])
        
        return obj
