from data import storemgr
from datetime import datetime
from stock.retrive_trade_days import getNextTradeDay
from stock.pool import PoolA

pool = PoolA()

dt = getNextTradeDay('2017-5-31')

while dt:

    dtstr = dt.strftime('%Y-%m-%d')
    
    allSuggests = storemgr.loadSuggestsOfDate(dtstr)

    for suggest in allSuggests:
        
        if pool.addSuggest(suggest):
            
            continue

    pool.run(dt)

    dt = getNextTradeDay(dtstr)

pool.show()