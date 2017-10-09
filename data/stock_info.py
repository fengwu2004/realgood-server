from datetime import datetime
from typing import List
from stock.retrive_trade_days import getNextTradeDay, getTradeDayCount
from analyse import SuggestHistoryManager
from stock.consulter_rate_system import getMaxIncrease, retriveConsulterRate, ConsultorWinsLevelManager


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

class Consultor(object):
    
    def __init__(self):
        
        self.name = ''
        
        self.company = ''

    def __eq__(self, other):

        if isinstance(other, Consultor):

            return self.toJson() == other.toJson()

        return False

    def __hash__(self):

        return hash(str(self.toJson()))
        
    def toJson(self):
        
        return {
            'name':self.name,
            'company':self.company
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
        
        obj = Consultor()
        
        obj.company = jsonvalue['company']

        obj.name = jsonvalue['name']
        
        return obj

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

class SuggestStock(object):
    
    def __init__(self):
        
        self.stockName = ''
        
        self.stockId = None
        
        self.date = None

        self.consultor = None
        
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
            'date': self.date,
            'consultor': self.consultor.toJson()
        }
    
    @classmethod
    def fromJson(cls, jsonvalue):
    
        obj = SuggestStock()
        
        obj.consultor = Consultor.fromJson(jsonvalue['consultor'])

        obj.stockId = jsonvalue['stockId']
        
        obj.stockName = jsonvalue['stockName']

        obj.date = jsonvalue['date']

        return obj

class SuggestScore(SuggestStock):

    def __init__(self, score, suggest:SuggestStock):

        super().__init__()

        self.stockId = suggest.stockId

        self.stockName = suggest.stockName

        self.date = suggest.date

        self.consultor = suggest.consultor

        self.score = score

class PoolStock(object):
    
    def __init__(self):
        
        self.stockId = ''
        
        self.addedDate = ''
        
        self.live = 20

        self.weight = 0
        
        self.living = True
        
        self.suggests = []
        
    def checkDie(self, dt:datetime) -> bool:

        startdt = datetime.strptime(self.addedDate, '%Y-%m-%d')

        count = getTradeDayCount(startdt, dt)

        return count > self.live

    def addSuggest(self, suggest:SuggestStock):
        
        self.suggests.append(suggest)
        
        if len(self.suggests) > 1:
            
            self.live = 30
            
        self.weight += 1
        
    def updateConsultorScore(self, dt:datetime):

        for suggest in self.suggests:

            startdt = datetime.strptime(suggest.date, '%Y-%m-%d')

            increase = getMaxIncrease(self.stockId, startdt, dt)

            score = retriveConsulterRate(increase[0], increase[1])

            ConsultorWinsLevelManager.instance().addConsultorScore(score, suggest)


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
        
        obj.suggest = SuggestStock.fromJson(jsonvalue['suggeststock'])
        
        for item in jsonvalue['trends']:
            
            obj.trends.append(RangeTrend.fromJson(item))
        
        return obj