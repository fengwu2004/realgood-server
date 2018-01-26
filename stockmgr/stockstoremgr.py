from os import walk
from stockmgr.load import getLines, formatData
from data.databasemgr import DatabaseMgr
import json
import tushare as ts
import math
from collections import defaultdict

def fun():

    df = ts.get_stock_basics()

    d = df.loc[:,['industry']]

    dic = defaultdict(list)

    for index, item in enumerate(d.index):

        name = d.loc[item, 'industry']

        dic[d.loc[item, 'industry']].append(item)

    industrys = []

    for key in dic:

        arrays = list()

        realkey = key

        print(key)

        if isinstance(key, str) is not True:

            realkey = '其他'

        for value in dic[key]:

            stockid = value

            arrays.append({'id':stockid})

        temp = {'firstindustry':realkey, 'stocks':arrays}

        industrys.append(temp)

    DatabaseMgr.instance().industry.remove({})

    DatabaseMgr.instance().industry.insert_many(industrys)

fun()

def saveToDB():
    
    mypath = '/Users/yan/Desktop/export/'
    
    f = []
    
    for (dirpath, dirname, filenames) in walk(mypath):
        
        f.extend(filenames)
    
    print(f)

    stocks = []
    
    for file in f:

        filePath = mypath + file
        
        if filePath.find('.txt') == -1:
            
            continue
        
        stock = formatData(getLines(filePath))
    
        stocks.append(stock.toJson())

    DatabaseMgr.instance().stocks.remove({})

    DatabaseMgr.instance().stocks.insert_many(stocks)

    result = []

    for stock in stocks:

        unit = dict()

        unit['id'] = stock['id']

        unit['name'] = stock['name']

        result.append(unit)

    DatabaseMgr.instance().stockInfos.remove({})

    DatabaseMgr.instance().stockInfos.insert_many(result)

saveToDB()