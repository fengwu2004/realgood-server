from data.stock_info import SuggestStock


class RangeTrend(object):
    def __init__ (self):
        # 区间
        self.range = 0
        # 最大值
        self.max = 0
        # 最大百分比
        self.maxPercent = 0
        # 最小值
        self.min = 0
        # 出现最大值的时间
        self.maxOffset = 0
    
    def toJson (self):
        
        return {
            'range':self.range,
            'max': self.max,
            'maxPercent': self.maxPercent,
            'min': self.min,
            'maxOffset': self.maxOffset,
        }

class SuggestTrends(object):
    
    def __init__ (self):
        
        self.suggeststock = None
        
        self.trends = []
    
    def toJson (self):
        
        trends = []
        
        for item in self.trends:
            
            trends.append(item.toJson())
        
        return {'suggeststock': self.suggeststock.toJson(), 'trends': trends}
    
    @classmethod
    def fromJson (cls, jsonvalue):
        
        obj = RecommondTrends()
        
        obj.suggest = SuggestStock.fromJson(jsonvalue['suggeststock'])
        
        for item in jsonvalue['trends']:
            
            obj.trends.append(RangeTrend.fromJson(item))
        
        return obj

# RecommondTrends
class RecommondTrends(object):
    
    def __init__(self):
        
        self.recommond = None
        
        self.trends = []
        
    def toJson(self):
        
        trends = []
        
        for item in self.trends:
        
            trends.append(item.toJson())
            
        return {
            'recommond':self.recommond.toJson(),
            'trends':trends
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
    
        obj = RecommondTrends()
    
        obj.recommond = Recommond.fromJson(jsonvalue['recommond'])
    
        for item in jsonvalue['trends']:
            
            obj.trends.append(RangeTrend.fromJson(item))
    
        return obj
    
    
# ConsultorRecommondsTrends
class ConsultorRecommondsTrends(object):
    
    def __init__(self):
        
        self.consultor = None
        
        self.recommondsTrends = []
        
    def toJson(self):
        
        temps = []
        
        for item in self.recommondsTrends:
            
            temps.append(item.toJson())
            
        return {
            'consultor':self.consultor.toJson(),
            'recommondsTrends':temps
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = ConsultorRecommondsTrends()
        
        obj.consultor = Consultor.fromJson(jsonvalue['consultor'])

        for item in jsonvalue['recommondsTrends']:
            
            obj.recommondsTrends.append(RecommondTrends.fromJson(item))
            
        return obj


# Consultor
class Consultor(object):
    def __init__ (self):
        
        self.name = None
        
        self.company = None
        
    def toJson (self):
        
        return self.__dict__
    
    @classmethod
    def fromJson (cls, jsonvalue):
        
        obj = Consultor()
        
        obj.name = jsonvalue['name']
        
        obj.company = jsonvalue['company']
        
        return obj
    
    
# Recommond
class Recommond(object):
    
    def __init__ (self):
        
        self.date = None
        
        self.stockname = None
        
        self.urgent = False
        
        self.amorpm = None

    def toJson (self):
        
        return self.__dict__

    @classmethod
    
    def fromJson (cls, jsonvalue):
        
        obj = Recommond()
        
        obj.date = jsonvalue['date']
        
        obj.stockname = jsonvalue['stockname']
        
        obj.urgent = jsonvalue['urgent']

        obj.amorpm = jsonvalue['amorpm']
        
        return obj


# RecommondUnit
class RecommondUnit(object):
    
    def __init__(self):
        
        self.consultor = None
        
        self.recommond = None
        
    def toJson(self):
        
        return {
            'recommond':self.recommond.toJson(),
            'consultor':self.consultor.toJson()
        }

    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = RecommondUnit()
        
        obj.recommond = Recommond.fromJson(jsonvalue['recommond'])

        obj.consultor = Consultor.fromJson(jsonvalue['consultor'])
        
        return obj


# ConsultorWithRecommonds
class ConsultorWithRecommonds(object):
    
    def __init__(self):
        
        self.consultor = None
        
        self.recommonds = []
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = ConsultorWithRecommonds()
        
        obj.consultor = Consultor.fromJson(jsonvalue['consultor'])
        
        for item in jsonvalue['recommonds']:
            
            obj.recommonds.append(Recommond.fromJson(item))
    
        return obj
    
    
    def toJson(self):
        
        recommonds = []
        
        for item in self.recommonds:
            
            recommonds.append(item.toJson())
            
        return {
            'consultor':self.consultor.toJson(),
            'recommonds':recommonds
        }