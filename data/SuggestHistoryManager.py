from data.stock import Stock, DayValue
from data.suggest import Suggest, SuggestTrends, Consultor, RangeTrend
import time

from data.databasemgr import DatabaseMgr
from data import storemgr
from typing import Dict, List
from datetime import datetime
from stock.retrive_trade_days import getPreTradeDay

def loadAllStockFromDB() -> Dict[str, Stock]:
    
    stocks = dict()
    
    items = DatabaseMgr.instance().stocks.find({}, {'_id': 0})

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
        
        if i >= len(dayvalues):
            
            break

        dayvlaue = dayvalues[i]
        
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
        
        self.stocks = loadAllStockFromDB()

    def getStock(self, stockId:str) -> Stock:

        if stockId in self.stocks:

            return self.stocks[stockId]

        return None
    
    def save(self, stockId:int, unit:Suggest):
        
        if not stockId in self.results:
            
            self.results[stockId] = list()
    
        self.results[stockId].append(unit)

    def findSuggestAfter(self, date:time.struct_time):
        
        suggeststocks = storemgr.loadSuggests()
    
        for suggest in suggeststocks:

            thetime = time.strptime(suggest.date, '%Y-%m-%d')

            if thetime < date:

                continue
            
            if suggest.stockId is not None:
                
                self.save(suggest.stockId, suggest)

    def getHistorySuggest(self, day:int) -> dict:

        dt = datetime.now()

        results = []

        while day > 0:

            dt = getPreTradeDay(dt.strftime('%Y-%m-%d'))

            items = storemgr.loadSuggestsOfDate(dt.strftime('%Y-%m-%d'))

            results.extend(items)

            day -= 1

        return results
    
    def getTradeInfoAfter(self, date:str, stockId:str, days:[int]) -> [RangeTrend]:

        if not stockId in self.stocks:

            return []

        stock = self.stocks[stockId]

        index = stock.getDayIndex(date)

        results = []

        for i in days:

            if index + i < len(stock.dayvalues):

                trend = getRangeTrend(index, i, stock.dayvalues)

                results.append(trend)

        return results
    
    def findAllSuggest(self, stockId:int) -> dict:

        suggests = storemgr.loadSuggests()

        return list(filter(lambda suggest:suggest.stockId == stockId, suggests))

    def getCloseAfter(self, date:str, stockId:str, days:[int]) -> [int]:
    
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
    
        suggests = storemgr.loadSuggestOfConsultor(consultor.id)
    
        results = []
    
        for suggest in suggests:
            
            obj = SuggestTrends()
        
            obj.suggest = suggest
        
            obj.trends = self.getTradeInfoAfter(suggest.date, suggest.stockId, [1, 3, 5, 10, 20, 40, 60])
        
            results.append(obj.toJson())
            
        return results
    
    @property
    def findTrends(self) -> List[SuggestTrends]:
    
        suggeststocks = storemgr.loadSuggests()
        
        items = list()
        
        for suggeststock in suggeststocks:
            
            item = SuggestTrends()
            
            item.suggest = suggeststock
            
            item.trends = self.getTradeInfoAfter(suggeststock.date, suggeststock.stockId, [1, 3, 5, 10, 20, 40, 60])

            items.append(item.toJson())
            
        return items
    
_instance = None

def instance():
    
    global _instance
    
    if _instance is None:
        
        _instance = SuggestHistoryManager()
        
    return _instance
