from data.stock_info import StockInfo
from data.recommond_unit import RecommondUnit
import time

import storemgr

results = dict()

#
def save(stockId:int, recommondunit:RecommondUnit):
    
    if not stockId in results:
        
        results[stockId] = list()

    results[stockId].append(recommondunit)

#
def findRecommondAfter(date:time.struct_time):
    
    recommonds = storemgr.intance().loadRecommondUnit()

    for recommondunit in recommonds:
        
        if time.strptime(recommondunit.recommond.date, '%Y-%m-%dT%H:%M:%S.%fZ') < date:
            
            continue
        
        stockId = storemgr.intance().getStockId(recommondunit.recommond.stockname)
        
        if stockId is not None:
            
            save(stockId, recommondunit)
            
            
def doSortWithData():

    for key in results.keys():
        
        results[key] = sorted(results[key], key = lambda k:time.strptime(k.recommond.date, '%Y-%m-%dT%H:%M:%S.%fZ'))
        

theTime = time.gmtime(time.time() - 30 * 24 * 3600)

findRecommondAfter(theTime)

doSortWithData()

print(results)
    
    
    
