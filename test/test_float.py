import pandas as pd
from collections import defaultdict
import tushare as ts
from data.databasemgr import DatabaseMgr

def fun():

    df = ts.get_stock_basics()

    d = df.loc[:,['industry']]

    dic = defaultdict(list)

    for index, item in enumerate(d.index):

        name = d.loc[item, 'industry']

        # print(index, name)

        dic[d.loc[item, 'industry']].append(item)

    industrys = []

    for key in dic:

        arrays = list()

        print(key)

        for value in dic[key]:

            stockid = value

            arrays.append({'id':stockid})

        temp = {'firstindustry':key, 'stocks':arrays}

        industrys.append(temp)

    DatabaseMgr.instance().industry.remove({})

    DatabaseMgr.instance().industry.insert_many(industrys)

fun()