import time
from stockmgr.retrive_trade_days import *
import sys
import math

# for p in sys.path:
#     print(p)
#
# t = getNextTradeDay('2017-9-10')
#
# print(t)
#
# t0 = time.mktime(time.strptime('2017-9-10', '%Y-%m-%d'))
#
# t1 = time.mktime(time.strptime('2017-9-12', '%Y-%m-%d'))
#
# if t1 + 1* 24 *3600 < t0:
#
#     print('ok')

stocklist = ['394848', '2384', '323', '34', '546765', '77876']

print(stocklist[0:1])

v = 3300/500

print(math.ceil(v))

# for i in range(100 + 1, 100 + 2):
#
#     print(i)