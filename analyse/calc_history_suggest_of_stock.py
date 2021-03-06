from data.suggest import Suggest
import time

import storemgr

results = list()


#
def save (stockId: int, unit: Suggest):
    if not stockId in results:
        results[stockId] = list()
    
    results[stockId].append(unit)


#
def findAllSuggest(stockId:int):
    
    results.clear()
    
    suggeststocks = storemgr.intance().loadSuggests()
    
    for suggeststock in suggeststocks:
        
        if suggeststock.stockId == stockId:
            
            results.append(suggeststock)
        
    return results



