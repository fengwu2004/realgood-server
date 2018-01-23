from data.databasemgr import DatabaseMgr
from data.stock import Stock
from data.storemgr import StockMgr

items = DatabaseMgr.instance().stocks.find({'id':'002807'}, {'_id': 0})

stock = None

for item in items:

    if 'id' in item:

        # print(item['id'])

        stockId = item['id']

        stock = Stock.fromJson(item)

        break

value = stock.findHeighestValue('2017/1/1')

value0 = stock.findLowestValue(value.date)

value1 = stock.findHeighestValue(value0.date)

if value1 is not None:

    if (value1.high - value0.low)/value0.open < 0.15:

        pass

if value0.isHammer():

    print('是锤子线')

else:

    print('不是锤子线')

print(value)