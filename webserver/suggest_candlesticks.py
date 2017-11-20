import json

from data.storemgr import StockMgr
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class FindCandlesticks(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        suggests = SuggestMgr.instance().getHistorySuggest(int(day))

        results = []

        for suggest in suggests:

            stock = StockMgr.instance().getStock(suggest.stockId)

            stockbasic = StockMgr.instance().getStockbasic(suggest.stockId)

            results.append({'stock':stock.toJson(), 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding})

        self.write({'success': 1, 'data':results})