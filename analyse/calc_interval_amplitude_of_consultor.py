# 计算区间振幅
from stockmgr.stockstoremgr import loadStock
import time
from data.suggest import RangeTrend
from data.stock import Stock, DayValue
from data import storemgr

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
            
    p = ((trend.max - dayvalues[index].open)/dayvalues[index].open) * 100
    
    trend.maxPercent = '%.1f' % p
            
    return trend

def getCloseAfter(date, stockname, days) -> [int]:
    
    stock = Stock.fromJson(loadStock(stockname))

    if stock is None:
        
        return []

    index = 0
    
    for dayvalue in stock.dayvalues:
    
        if getTime(dayvalue.date) > date:
            
            break
    
        index += 1

    index -= 1

    results = []

    for i in days:
    
        if index + i < len(stock.dayvalues):
            
            results.append(100 * (stock.dayvalues[index + i].close - stock.dayvalues[index].close)/stock.dayvalues[index].close)
        
        else:
    
            results.append(0)
            
    return results

def getTradeInfoAfter(date, stockname, days) -> [RangeTrend]:
    
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
    
    results = []
    
    for i in days:
        
        if index + i < len(stock.dayvalues):
            
            trend = getRangeTrend(index, i, stock.dayvalues)

            results.append(trend)
            
    return results