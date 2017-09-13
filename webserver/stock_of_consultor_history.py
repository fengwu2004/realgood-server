import json

import storemgr
from analyse import SuggestHistoryManager
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager


class FindStockSuggestHistory(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        stockname = data['stockname']
        
        stockId = storemgr.intance().getStockId(stockname)

        if not 'token' in data or not tokenManager.TokenManagerInstance().checkToken(data['token']):
            
            self.write({'success': -1})
    
            return
        
        items = SuggestHistoryManager.instance().findAllSuggest(stockId)

        jsonvalue = list()
        
        for item in items:
            
            jsonvalue.append(item.toJson())
        
        self.write({'success': 1, 'data': jsonvalue})