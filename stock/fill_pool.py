from data import storemgr
from datetime import datetime

from stock.consultor_score_manager import ConsultorScoreManager
from stock.retrive_trade_days import getNextTradeDay
from stock.pool import PoolA

def getPool():

    pool = PoolA()

    dt = getNextTradeDay('2017-4-30')

    while dt:

        dtstr = dt.strftime('%Y-%m-%d')

        allSuggests = storemgr.loadSuggestsOfDate(dtstr)

        for suggest in allSuggests:

            if pool.addSuggest(suggest):

                continue

        pool.run(dt)

        dt = getNextTradeDay(dtstr)

    pool.show()

    return pool