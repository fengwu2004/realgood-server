from datetime import datetime
from data.storemgr import *
from data.stock import *
import tushare as ts

value = ts.get_today_all()

print(value[0:1])