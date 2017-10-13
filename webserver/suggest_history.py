import json

from data import storemgr, SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager


class FindHistorySuggest(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        results = SuggestHistoryManager.instance().getHistorySuggest(int(day))

        jsonvalue = dict()
        
        for stockId in results.keys():
    
            suggests = results[stockId]

            items = []
            
            for suggest in suggests:
                
                items.append(suggest.toJson())
                
            stockName = storemgr.intance().getStockName(stockId)

            jsonvalue[stockName] = items

        self.write({'success': 1, 'data':jsonvalue})