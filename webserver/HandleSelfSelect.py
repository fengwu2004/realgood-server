import json

from data.databasemgr import DatabaseMgr
from data.storemgr import StockMgr
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class HandleSelfSelectRequest(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        results = []

        items = DatabaseMgr.instance().selfselect.find({}, {'_id':0})

        for item in items:

            stock = StockMgr.instance().getStock(item['stockid'])

            try:
                stockbasic = StockMgr.instance().getStockbasic(item['stockid'])

            except Exception:

                continue

            results.append({'stock':stock.toJson(), 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding, 'isselfselect':True})

        self.write({'success': 1, 'data':results})