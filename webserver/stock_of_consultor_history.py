import json

from data import storemgr, SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager


class FindStockSuggestHistory(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))

        with data['stockname'] as stockname:
            
            stockId = storemgr.getStockId(stockname)
            
            items = SuggestHistoryManager.instance().findAllSuggest(stockId)
    
            jsonvalue = list(map(lambda item: item.toJson(), items))
            
            self.write({'success': 1, 'data': jsonvalue})