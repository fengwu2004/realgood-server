from datetime import datetime
from data.storemgr import *

items = DatabaseMgr.instance().stocks.find({'id':'600125'}, {'_id': 0})

p = 1.02030239239

b = '%.1f' % p

print(b)

t = datetime.strptime('2018-9-8', '%Y-%m-%d').strftime('%Y-%m-%d')

print(t)