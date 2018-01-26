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

            if stock is None or stock.isNew():

                continue

            lowvolatility = StockMgr.instance().checkIsLowVolatility(stock.id)

            increase = stock.increaseTrend()

            stockbasic = StockMgr.instance().getStockbasic(item['id'])

            if stockbasic is None:

                continue

            results.append({'stock':stock.toJson(), 'increase':increase, 'lowvolatility':lowvolatility, 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding, 'isselfselect':True})

        self.write({'success': 1, 'data':results})