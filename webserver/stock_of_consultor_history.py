import json

import storemgr
from analyse.calc_history_suggest_of_stock import findAllSuggest
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager


class FindStockSuggestHistory(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        stockname = data['stockname']
        
        stockId = storemgr.intance().getStockId(stockname)
        
        # token = data['token']
        
        # if not tokenManager.TokenManagerInstance().checkToken(token):
        #
        #     self.write({'success': -1})
        #
        #     return
        
        items = findAllSuggest(stockId)

        jsonvalue = list()
        
        for item in items:
            
            jsonvalue.append(item.toJson())
        
        self.write({'success': 1, 'data': jsonvalue})