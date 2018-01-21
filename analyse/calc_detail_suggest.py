import time

import storemgr
from analyse.calc_interval_amplitude_of_consultor import getTradeInfoAfter, getCloseAfter
from data.suggest import SuggestInfo
from data.suggest import Suggest

suggeststocks = storemgr.loadSuggests()
#
def getSuggestCount(suggeststock:Suggest, day):
    
    count = 0

    t0 = time.mktime(time.strptime(suggeststock.date, '%Y/%m/%d'))

    for item in suggeststocks:

        if item.stockName == suggeststock.stockName:
        
            t = time.mktime(time.strptime(item.date, '%Y/%m/%d'))
            
            if t0 < t < t0 + day * 24 * 3600:
                
                count += 1
            
    return count

#
def getSuggestCounts(suggeststock:Suggest, days:[int]):
    
    results = []
    
    for day in days:
        
        results.append(getSuggestCount(suggeststock, day))

    return results

#
def getSuggestTrends(suggeststock:Suggest, days:[int]):
    
    items = getCloseAfter(time.strptime(suggeststock.date, '%Y/%m/%d'), suggeststock.stockName, days)
    
    return items

def run():

    suggestdays = [3, 5, 10, 20]

    trenddays = [1, 3, 5, 10, 20]

    results = []

    for suggeststock in suggeststocks:

        item = SuggestInfo()

        item.suggeststock = suggeststock

        item.counts = getSuggestCounts(suggeststock, suggestdays)

        item.trends = getSuggestTrends(suggeststock, trenddays)

        results.append(item)
        
    return results