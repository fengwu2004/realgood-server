from datetime import datetime
from data.storemgr import *
from data.stock import *

# stock = StockMgr.instance().getStock('600125')
#
# maxvalue = max(stock.dayvalues, key = lambda dayvalue:dayvalue.close)

maxvalue = '%.1f' % ((928.3 - 4848)/234)

print(maxvalue)