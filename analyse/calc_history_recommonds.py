from data.stock_info import StockInfo, SuggestStock
from data.recommond_unit import RecommondUnit
import time

import storemgr

results = dict()

#
def save(stockId:int, unit:SuggestStock):
    
    if not stockId in results:
        
        results[stockId] = list()

    results[stockId].append(unit)

#
def findRecommondAfter(date:time.struct_time):
    
    suggeststocks = storemgr.intance().loadSuggests()

    for suggeststock in suggeststocks:
        
        # print(suggeststock.stockName)
        
        if time.strptime(suggeststock.date, '%Y-%m-%d') < date:
            
            continue
        
        stockId = storemgr.intance().getStockId(suggeststock.stockName)
        
        if stockId is not None:
            
            save(stockId, suggeststock)
            
def doSortWithData():

    for key in results.keys():
        
        results[key] = sorted(results[key], key = lambda k:time.strptime(k.date, '%Y-%m-%d'))
        

def getHistorySuggest(day:int):
    
    results.clear()

    theTime = time.gmtime(time.time() - day * 24 * 3600)

    findRecommondAfter(theTime)

    doSortWithData()

    return results
    
    
    
