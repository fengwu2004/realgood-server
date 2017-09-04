# 以分析师为key
from pymongo import MongoClient
import storemgr
from data.recommond_unit import ConsultorWithRecommonds

items = storemgr.intance().loadRecommondUnit()

results = []

def findConsultorWithRecommonds(name) -> ConsultorWithRecommonds:
    
    for value in results:
        
        if value.consultor.name == name:
            
            return value
        
    return None

for item in items:

    unit = findConsultorWithRecommonds(item.consultor.name)
    
    if unit:
        
        unit.recommonds.append(item.recommond)
    
    else:
    
        unit = ConsultorWithRecommonds()
        
        unit.consultor = item.consultor
        
        unit.recommonds.append(item.recommond)
        
        results.append(unit)
        

temps = []

for v in results:
    
    temps.append(v.toJson())
        
storemgr.intance().saveManyTo('consultors', temps)
