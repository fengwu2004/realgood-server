from data import storemgr
from datetime import datetime

from stockmgr.consultor_score_manager import ConsultorScoreManager
from stockmgr.retrive_trade_days import getNextTradeDay
from stockmgr.pool import PoolA

def getPool():

    pool = PoolA()

    dt = getNextTradeDay('2017-4-30')

    while dt:

        dtstr = dt.strftime('%Y-%m-%d')

        print(dtstr)

        allSuggests = storemgr.loadSuggestsOfDate(dtstr)

        for suggest in allSuggests:

            pool.addSuggest(suggest)

        t = datetime.now()

        pool.run(dt)

        print(datetime.now() - t)

        dt = getNextTradeDay(dtstr)

    pool.show()

    return pool

def test():

    print(getPool().getReuslt())

# test()