import tushare as ts
from datetime import datetime
from time import sleep
from data.databasemgr import DatabaseMgr
from collections import namedtuple
from stockmgr.retrive_trade_days import getPreTradeDay

dt = getPreTradeDay('2017-10-27')

dtstr = dt.strftime('%Y-%m-%d')

stocks = DatabaseMgr.instance().stockInfos.find({}, {'_id':0})

stocklist = []

for stock in stocks:

    if len(str(stock['id'])) < 6:

        continue

    stocklist.append(str(stock['id']))

results = []

StockVolum = namedtuple('StockVolum', 'code volume')

t = 0

while t < len(stocklist):

    print(stocklist[t])

    df = ts.get_k_data(stocklist[t], start='2017-10-26',end='')

    if 'volume' not in df or len(df.volume.values) <= 0:

        t += 1

        continue

    volume = df.volume.values[0]

    results.append({'id': stocklist[t], 'volume': volume})

    t += 1

DatabaseMgr.instance().stockvolumof(dtstr).remove({})

DatabaseMgr.instance().stockvolumof(dtstr).insert_many(results)

print('finish')








