import time
from stockmgr.retrive_trade_days import *
import sys

for p in sys.path:
    print(p)

t = getNextTradeDay('2017-9-10')

print(t)
#
# t0 = time.mktime(time.strptime('2017-9-10', '%Y-%m-%d'))
#
# t1 = time.mktime(time.strptime('2017-9-12', '%Y-%m-%d'))
#
# if t1 + 1* 24 *3600 < t0:
#
#     print('ok')

for i in range(100 + 1, 100 + 2):

    print(i)