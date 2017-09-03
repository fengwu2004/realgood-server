import json

import storemgr
from data.recommond_unit import RecommondUnit, Consultor
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager

def serializationRecommondUnit(item):
    
    ruitem = RecommondUnit()
    
    ruitem.consultor = Consultor()
    
    ruitem.consultor.name = item['consultor']
    
    ruitem.consultor.company = item['company']
    
    ruitem.consultor.pm = item['ispm']
    
    ruitem.stockname = item['focus']
    
    ruitem.date = item['date']
    
    ruitem.urgent = item['urgent']
    
    ruitem.amorpm = item['amorpm']
    
    return ruitem

class SaveRecommond(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        token = data['token']

        res = {'success': -1}
        
        if not tokenManager.TokenManagerInstance().checkToken(token):
        
            self.write(res)
            
            return

        ruitem = serializationRecommondUnit(data)
        
        storemgr.intance().saveToDb(ruitem.toJson())

        items = storemgr.intance().findInfoWith({'consultor.name':ruitem.consultor.name})
        
        result = []
        
        for item in items:
            
            result.append(item)
            
            if len(result) >= 5:
                
                break
                
        res = {'success':1,'data':result}
        
        self.write(res)