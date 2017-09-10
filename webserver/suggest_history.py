import json

import storemgr
from analyse.calc_history_recommonds import getHistorySuggest
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager


class FindHistorySuggest(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        if not tokenManager.TokenManagerInstance().checkToken(data['token']):
            
            self.write({'success': -1})
    
            return

        results = getHistorySuggest(int(day))

        jsonvalue = dict()
        
        for stockId in results.keys():
    
            suggests = results[stockId]

            items = []
            
            for suggest in suggests:
                
                items.append(suggest.toJson())
                
            stockName = storemgr.intance().getStockName(stockId)

            jsonvalue[stockName] = items

        self.write({'success': 1, 'data':jsonvalue})