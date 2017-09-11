import json

import storemgr
from data.recommond_unit import RecommondUnit, Consultor, Recommond
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager

def serializationRecommondUnit(item):
    
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
    
    return ruitem

class SaveRecommond(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        if not 'token' in data or not tokenManager.TokenManagerInstance().checkToken(data['token']):
            
            self.write({'success': -1})
    
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