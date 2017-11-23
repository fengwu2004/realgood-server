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

        stockids = set()

        for suggest in suggests:

            stockids.add(suggest.stockId)

        for stockid in list(stockids):

            stock = StockMgr.instance().getStock(stockid)

            stockbasic = StockMgr.instance().getStockbasic(stockid)

            results.append({'stock':stock.toJson(), 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding})

        self.write({'success': 1, 'data':results})