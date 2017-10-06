import json

from analyse import SuggestHistoryManager
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager
from data import storemgr

class FindStockSuggestHistory(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))

        with data['stockname'] as stockname:
            
            stockId = storemgr.getStockId(stockname)
            
            items = SuggestHistoryManager.instance().findAllSuggest(stockId)
    
            jsonvalue = list()
            
            for item in items:
                
                jsonvalue.append(item.toJson())
            
            self.write({'success': 1, 'data': jsonvalue})