import json

from data.storemgr import *
from data.suggest_manager import *
from webserver.RequestBaseManager import RequestBaseManager


class FindStockSuggestHistory(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))

        stockname = data['stockname']

        stockId = storemgr.getStockId(stockname)

        items = SuggestMgr.instance().findAllSuggest(stockId)

        jsonvalue = list(map(lambda item: item.toJson(), items))

        self.write({'success': 1, 'data': jsonvalue})
