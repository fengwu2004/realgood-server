# 计算区间振幅
from data.recommond_unit import RecommondUnit
from stock.stockstoremgr import loadStock
import time
from data.stock_unit import Stock

import storemgr

class RangeTrend(object):
    
    def __init__(self):
        
        # 区间
        self.range = 0
        # 最大值
        self.max = 0
        # 最小值
        self.min = 0
        # 出现最大值的时间
        self.maxOffset = 0
        
    def toJson(self):
        
        return self.__dict__

def getTime (value):
    
    return time.strptime(value, '%Y/%m/%d')

def getRangeTrend(index, offset, dayvalues):
    
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
            
    return trend
    
def getTradeInfoAfter(date, stockname):
    
    stock = Stock.fromJson(loadStock(stockname))

    if stock is None:
        
        return None

    index = 0

    for dayvalue in stock.dayvalues:
    
        if getTime(dayvalue.date) > date:
            
            break

        index += 1

    index -= 1
        
    if index >= len(stock.dayvalues):
        
        return None
    
    days = [1, 3, 5, 10, 20, 40, 60]
        
    results = []
    
    for i in days:
        
        if index + i < len(stock.dayvalues):
            
            trend = getRangeTrend(index, i, stock.dayvalues)

            results.append(trend.toJson())
            
    return results

def doRun(consultorname):
    
    recommonds = []
    
    items = storemgr.intance().findInfoWith({'consultor.name': consultorname})

    for item in items:
        
        recommonds.append(RecommondUnit.fromJson(item))

    results = []
    
    for recommond in recommonds:
        
        stockOfTrend = dict()
        
        stockOfTrend['recommond'] = recommond.toJson()
    
        stockOfTrend['trend'] = getTradeInfoAfter(time.strptime(recommond.date, '%Y-%m-%dT%H:%M:%S.%fZ'),
                                                       recommond.stockname)

        results.append(stockOfTrend)
        
    print(results)
        
    return results
