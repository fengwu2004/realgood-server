# 将推荐数据重新存储
from pymongo import MongoClient
from data.recommond_unit import RecommondUnit, Consultor, Recommond

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

    ruitem.recommond = Recommond()
    
    ruitem.recommond.stockname = item['focus']
    
    ruitem.recommond.date = item['date']
    
    ruitem.recommond.urgent = item['urgent']
    
    ruitem.recommond.amorpm = item['amorpm']

    results.append(ruitem.toJson())
    
restore.insert_many(results)