from stockmgr.retrive_trade_days import *

from data.stock import Stock, DayValue
from data.suggest import Suggest, SuggestTrends, Consultor, RangeTrend
import time

from data.databasemgr import DatabaseMgr
from data import storemgr
from typing import Dict, List
from datetime import datetime


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

_instance = None

class SuggestMgr(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = SuggestMgr()

        return _instance

    def __init__(self):

        self.suggests = storemgr.loadSuggests()

    def loadSuggestsOfDate(self, dtstr:str):

        return [suggest for suggest in self.suggests if suggest.date == dtstr]

    def getHistorySuggest(self, day:int) -> dict:

        dt = datetime.now()

        results = []

        while day > 0:

            dt = getPreTradeDay(dt.strftime('%Y-%m-%d'))

            items = self.loadSuggestsOfDate(dt.strftime('%Y-%m-%d'))

            results.extend(items)

            day -= 1

        return results

    def getTradeInfoAfter(self, date:str, stockId:str, days:[int]) -> [RangeTrend]:

        stock = storemgr.getStock(stockId)

        index = stock.getDayIndex(date)

        results = []

        for i in days:

            if index + i < len(stock.dayvalues):

                trend = getRangeTrend(index, i, stock.dayvalues)

                results.append(trend)

        return results

    def findAllSuggest(self, stockId:int) -> dict:

        return [suggest for suggest in self.suggests if suggest.stock == stockId]

    def getCloseAfter(self, date:str, stockId:str, days:[int]) -> [int]:

        stock = storemgr.getStock(stockId)

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

    def loadSuggestOfConsultor(self, consultorId:int):

        return [suggest for suggest in self.suggests if suggest.consultorId == consultorId]

    def findRangetrends(self, consultor:Consultor):

        suggests = self.loadSuggestOfConsultor(consultor.id)

        results = []

        for suggest in suggests:

            obj = SuggestTrends()

            obj.suggest = suggest

            obj.trends = self.getTradeInfoAfter(suggest.date, suggest.stockId, [1, 3, 5, 10, 20, 40, 60])

            results.append(obj.toJson())

        return results

    @property
    def findTrends(self) -> List[SuggestTrends]:

        items = list()

        for suggeststock in self.suggests:

            item = SuggestTrends()

            item.suggest = suggeststock

            item.trends = self.getTradeInfoAfter(suggeststock.date, suggeststock.stockId, [1, 3, 5, 10, 20, 40, 60])

            items.append(item.toJson())

        return items