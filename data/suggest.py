from datetime import datetime
from typing import List, Tuple
from functools import reduce

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
        
        obj.suggeststock = Suggest.fromJson(jsonvalue['suggeststock'])
        
        obj.counts = jsonvalue['counts']
        
        obj.trends = jsonvalue['trends']
        
        return obj

class Consultor(object):
    
    def __init__(self, name:str, company:str, id:int):
        
        self.name = name
        
        self.company = company

        self.id = id

    def __eq__(self, other):

        if isinstance(other, Consultor):

            return self.toJson() == other.toJson()

        return False

    def __hash__(self):

        return hash(str(self.toJson()))
        
    def toJson(self):
        
        return {
            'id':self.id,
            'name':self.name,
            'company':self.company
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        return Consultor(jsonvalue['name'], jsonvalue['company'], jsonvalue['id'])

class ConsultorWinsLevel(Consultor):

    def __init__(self):

        self.suggest_wins = []

        self.average = 0

    def addScore(self, score:float):

        self.suggest_wins.append(score)

        sumscore = 0

        for score in self.suggest_wins:

            sumscore += score

        self.average = sumscore/len(self.suggest_wins)

class Suggest(object):
    
    def __init__(self):
        
        self.stockName = ''
        
        self.stockId = None
        
        self.date = None

        self.consultorId = -1

    def __eq__(self, other):

        if isinstance(other, Suggest):

            return self.toJson() == other.toJson()

        return False

    def __hash__(self):

        return hash(str(self.toJson()))
        
    def toJson(self):
        
        return {
        
            'stockName': self.stockName,
            'stockId': self.stockId,
            'date': self.date,
            'consultorId': self.consultorId
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
    
        obj = Suggest()
        
        obj.consultorId = jsonvalue['consultorId']

        obj.stockId = jsonvalue['stockId']
        
        obj.stockName = jsonvalue['stockName']

        obj.date = jsonvalue['date']

        return obj

class SuggestScore(Suggest):

    def __init__(self, score, suggest:Suggest):

        super().__init__()

        self.stockId = suggest.stockId

        self.stockName = suggest.stockName

        self.date = suggest.date

        self.consultorId = suggest.consultorId

        self.score = score

    def toJson(self):

        data = super().toJson()

        data['data'] = self.score

        return data

    @classmethod
    def fromJson(cls, jsonvalue):

        suggest = Suggest.fromJson(jsonvalue)

        score = jsonvalue['score']

        return SuggestScore(score, suggest)

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
        return {'range': self.range, 'max': self.max, 'maxPercent': self.maxPercent, 'min': self.min,
            'maxOffset': self.maxOffset, }

class SuggestTrends(object):

    def __init__(self):

        self.suggeststock = None

        self.trends = []

    def toJson(self):

        trends = []

        for item in self.trends:

            trends.append(item.toJson())

        return {'suggeststock': self.suggeststock.toJson(), 'trends': trends}

    @classmethod
    def fromJson(cls, jsonvalue):

        obj = SuggestTrends()

        obj.suggest = Suggest.fromJson(jsonvalue['suggeststock'])

        for item in jsonvalue['trends']:

            obj.trends.append(RangeTrend.fromJson(item))

        return obj

class SuggestStockTrends(object):

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
        
        obj = SuggestStockTrends()
        
        obj.suggest = Suggest.fromJson(jsonvalue['suggeststock'])
        
        for item in jsonvalue['trends']:
            
            obj.trends.append(RangeTrend.fromJson(item))
        
        return obj