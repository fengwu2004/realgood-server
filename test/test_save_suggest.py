# 将推荐数据重新存储
from pymongo import MongoClient

import storemgr
from data.recommond_unit import RecommondUnit, Consultor, Recommond
from data.stock_info import SuggestStock

uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

db = client['recommond']

coll = db['recommond_copy_2']

items = coll.find({}, {'_id': 0})

restore = db['suggest']

results = []

for item in items:
    
    ruitem = RecommondUnit.fromJson(item)
    
    temp = SuggestStock()

    temp.stockName = ruitem.recommond.stockname
    
    t = ruitem.recommond.date
    
    temp.date = t[0:10]
    
    temp.company = ruitem.consultor.company
    
    temp.name = ruitem.consultor.name

    temp.stockId = storemgr.intance().getStockId(temp.stockName)
    
    results.append(temp.toJson())

restore.insert_many(results)