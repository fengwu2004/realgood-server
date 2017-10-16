import json

from data import storemgr, SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager
from stock.consultor_manager import ConsultorManager
from data.suggest import *

def getSuggestInfo(suggest:Suggest):

    data = suggest.toJson()

    consultor = ConsultorManager.instance().retriveConsultorBy(suggest.consultorId)

    return dict(data, **(consultor.toJson()))

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

            items = list(map(lambda suggest: getSuggestInfo(suggest), suggests))

            stockName = storemgr.getStockName(stockId)

            jsonvalue[stockName] = items

        self.write({'success': 1, 'data':jsonvalue})