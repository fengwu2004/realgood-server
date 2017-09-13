from data.stock_info import SuggestStock, SuggestStockTrends, Consultor, RangeTrend
from data.stock_unit import Stock, DayValue
import time
import storemgr
from pymongo import MongoClient
from typing import Dict

def loadFromDB() -> Dict[str, Stock]:
    
    stocks = dict()
    
    uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"
    
    client = MongoClient(uri)
    
    db = client["recommond"]
    
    coll = db['stocks']
    
    items = coll.find({}, {'_id': 0})
    
    for item in items:
        
        if 'id' in item:
            
            stockId = item['id']
        
            stocks[stockId] = Stock.fromJson(item)
            
    return stocks

def getRangeTrend(index, offset, dayvalues: [DayValue]):
    
    trend = RangeTrend()
    
    trend.range = offset
    
    trend.max = 0
    
    trend.min = 1000
    
    for i in range(index + 1, index + offset + 1):
        
        with dayvalues[i] as dayvlaue:
        
            if trend.max < dayvlaue.max:
                trend.max = dayvlaue.max
                
                trend.maxOffset = i - index
            
            if trend.min > dayvlaue.min:
                trend.min = dayvlaue.min
    
    p = ((trend.max - dayvalues[index].open) / dayvalues[index].open) * 100
    
    trend.maxPercent = '%.1f' % p
    
    return trend

class SuggestHistoryManager(object):
    
    def __init__(self):
        
        self.results = dict()
        
        self.stocks = loadFromDB()
    
    def save(self, stockId:int, unit:SuggestStock):
        
        if not stockId in self.results:
            
            self.results[stockId] = list()
    
        self.results[stockId].append(unit)

    def findRecommondAfter(self, date:time.struct_time):
        
        suggeststocks = storemgr.intance().loadSuggests()
    
        for suggeststock in suggeststocks:
            
            with time.strptime(suggeststock.date, '%Y-%m-%d') as thetime:
            
                if thetime < date:
                    
                    continue
            
            if suggeststock.stockId is not None:
                
                self.save(suggeststock.stockId, suggeststock)
            
    def doSortWithData(self):
    
        for key in self.results.keys():
            
            self.results[key] = sorted(self.results[key], key = lambda k:time.strptime(k.date, '%Y-%m-%d'))
        
    def getHistorySuggest(self, day:int) -> dict:
        
        self.results.clear()
    
        theTime = time.gmtime(time.time() - day * 24 * 3600)
    
        self.findRecommondAfter(theTime)
    
        self.doSortWithData()
    
        return self.results
    
    def findAllSuggest(self, stockId:int) -> dict:
        
        self.results.clear()
    
        suggeststocks = storemgr.intance().loadSuggests()
    
        for suggeststock in suggeststocks:
        
            if suggeststock.stockId == stockId:
                
                self.results.append(suggeststock)
    
        return self.results
    
    def getTradeInfoAfter (self, date:str, stockId:int, days:[int]) -> [RangeTrend]:
    
        with self.stocks[stockId] as stock:
        
            if stock is None:
                
                return []
                
        index = stock.getDayIndex(date)
    
        results = []
    
        for i in days:
        
            if index + i < len(stock.dayvalues):
                
                trend = getRangeTrend(index, i, stock.dayvalues)
            
                results.append(trend)
    
        return results

    def getCloseAfter(self, date:str, stockId:int, days:[int]) -> [int]:
    
        with self.stocks[stockId] as stock:
        
            if stock is None:
                
                return []

        index = stock.getDayIndex(date)
    
        results = []
    
        for i in days:
        
            if index + i < len(stock.dayvalues):
            
                results.append(
                    100 * (stock.dayvalues[index + i].close - stock.dayvalues[index].close) / stock.dayvalues[
                        index].close)
        
            else:

                results.append(0)
    
        return results
    
    def findRangetrends(self, consultor:Consultor):
    
        suggeststocks = storemgr.intance().loadSuggestOfConsultor(consultor.name, consultor.company)
    
        results = []
    
        for suggeststock in suggeststocks:
            
            obj = SuggestStockTrends()
        
            obj.suggeststock = suggeststock
        
            obj.trends = self.getTradeInfoAfter(suggeststock.date, suggeststock.stockId, [1, 3, 5, 10, 20, 40, 60])
        
            results.append(obj.toJson())
            
        pass
    
_instance = None

def instance():
    
    global _instance
    
    if _instance is None:
        
        _instance = SuggestHistoryManager()
        
    return _instance

loadFromDB()
