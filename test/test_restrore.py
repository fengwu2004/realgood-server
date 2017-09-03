# 将推荐数据重新存储
from pymongo import MongoClient
from data.recommond_unit import RecommondUnit, Consultor

uri = "mongodb://yanli:9394@123.207.213.131:27017/recommond?authMechanism=SCRAM-SHA-1"

client = MongoClient(uri)

db = client['recommond']

coll = db['recommond_copy']

items = coll.find({}, {'_id':0})

restore = db['recommond_clone']

results = []

for item in items:
    
    ruitem = RecommondUnit()
    
    ruitem.consultor = Consultor()
    
    ruitem.consultor.name = item['consultor']
    
    ruitem.consultor.company = item['company']
    
    ruitem.consultor.pm = item['ispm']
    
    ruitem.stockname = item['focus']
    
    ruitem.date = item['date']
    
    ruitem.urgent = item['urgent']
    
    ruitem.amorpm = item['amorpm']

    results.append(ruitem.toJson())
    
restore.insert_many(results)