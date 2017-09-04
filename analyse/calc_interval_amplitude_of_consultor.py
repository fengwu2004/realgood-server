# 计算区间振幅
from data.recommond_unit import RecommondUnit, RangeTrend, Recommond, RecommondTrends
from stock.stockstoremgr import loadStock
import time
from data.stock_unit import Stock, DayValue

import storemgr

def getTime (value):
    
    return time.strptime(value, '%Y/%m/%d')

def getRangeTrend(index, offset, dayvalues:[DayValue]):
    
    trend = RangeTrend()

    trend.range = offset

    trend.max = 0
    
    trend.min = 1000
    
    for i in range(index, index + offset):
    
        dayvlaue = dayvalues[i]
        
        if trend.max < dayvlaue.max:
            
            trend.max = dayvlaue.max
            
            trend.maxOffset = i - index
            
        if trend.min > dayvlaue.min:
            
            trend.min = dayvlaue.min
            
    trend.maxPercent = (trend.max - dayvalues[index].open)/dayvalues[index].open

    trend.maxPercent *= 100
            
    return trend
    
def getTradeInfoAfter(date, stockname):
    
    stock = Stock.fromJson(loadStock(stockname))

    if stock is None:
        
        return []

    index = 0

    for dayvalue in stock.dayvalues:
    
        if getTime(dayvalue.date) > date:
            
            break

        index += 1

    index -= 1
        
    if index >= len(stock.dayvalues):
        
        return []
    
    days = [1, 3, 5, 10, 20, 40, 60]
        
    results = []
    
    for i in days:
        
        if index + i < len(stock.dayvalues):
            
            trend = getRangeTrend(index, i, stock.dayvalues)

            results.append(trend)
            
    return results

def doRun(reommonds:[Recommond]) -> [RecommondTrends]:
    
    results = []
    
    for recommond in reommonds:
        
        obj = RecommondTrends()

        obj.recommond = recommond

        obj.trends = getTradeInfoAfter(time.strptime(recommond.date, '%Y-%m-%dT%H:%M:%S.%fZ'),
                                                       recommond.stockname)

        results.append(obj)
        
    print(results)
        
    return results