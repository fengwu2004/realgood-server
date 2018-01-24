import pandas as pd
from collections import defaultdict

def getStockId(value):

    length = len(value)

    if length == 6:

        return value

    if length == 5:

        return '0' + value

    if length == 4:

        return '00' + value

    if length == 3:

        return '000' + value

    if length == 2:

        return '0000' + value

    if length == 1:

        return '00000' + value


from data.databasemgr import DatabaseMgr

xls_file = pd.ExcelFile('/Users/yan/Desktop/sw.xlsx')

df = xls_file.parse('Sheet1')

print(df)

t = df.loc[:,['行业名称','股票代码'] ]

dic = defaultdict(list)

for item in t.index:

    dic[t.loc[item, '行业名称']].append(t.loc[item, '股票代码'])

print(dic)

industrys = []

for key in dic:

    arrays = list()

    for value in dic[key]:

        stockid = getStockId(str(value))

        arrays.append({'id':stockid})

    temp = {'firstindustry':key, 'stocks':arrays}

    industrys.append(temp)

DatabaseMgr.instance().industry.remove({})

DatabaseMgr.instance().industry.insert_many(industrys)

