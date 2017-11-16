import tushare as ts
from datetime import datetime
from time import sleep
from data.databasemgr import DatabaseMgr
from collections import namedtuple
from stockmgr.retrive_trade_days import getPreTradeDay
import math

dayvolums = dict()

stocklist = list()

def loadYestodayVolums():

    dt = getPreTradeDay('2017-10-27')

    dtstr = dt.strftime('%Y-%m-%d')

    items = DatabaseMgr.instance().stockvolumof(dtstr).find({}, {'_id':0})

    global dayvolums

    global stocklist

    for item in items:

        stockid = item['id']

        stocklist.append(stockid)

        dayvolums[ stockid ] = item['volume']

results = []

alreadyexist = dict()

def run():

    global results

    everycount = 1

    total = math.ceil(len(stocklist)/everycount)

    for t in range(1, total):

        sleep(3)

        start = everycount * (t - 1)

        end = everycount * t

        endindex = min(end, len(stocklist) - 1)

        df = ts.get_hist_data(stocklist[start], start='2017-10-26',end='', ktype = 5)

        codes = df.code

        volumes = df.volume

        for i in range(0, codes.size):

            stockid = codes[i]

            if int(dayvolums[stockid]) == 0:

                continue

            if int(volumes[i]) * 0.01 >= 2.00 * int(dayvolums[stockid]) and stockid not in alreadyexist:

                alreadyexist[stockid] = float(volumes[i]) / float(dayvolums[stockid])

    print(alreadyexist.keys())

    print('------------------------------')

    run()

loadYestodayVolums()

run()









































