import json

from data.databasemgr import DatabaseMgr
from data.storemgr import StockMgr
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class HandleFilterStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        results = []

        items = DatabaseMgr.instance().stocks.find({}, {'_id': 0})

        for item in items:

            if 'id' in item is False:

                continue

            stockId = item['id']

            stock = StockMgr.instance().getStock(stockId)

            if stock is None or stock.isNew():

                continue

            increase = stock.increaseTrend()

            lowvolatility = StockMgr.instance().checkIsLowVolatility(stock.id)

            if lowvolatility is not True and increase is not True:

                continue

            isselfselect = StockMgr.instance().checkIsSelfSelect(stock.id)

            stockbasic = StockMgr.instance().getStockbasic(stock.id)

            if stockbasic is None:

                continue

            results.append({'stock':stock.toJson(), 'increase':increase, 'lowvolatility':lowvolatility, 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding, 'isselfselect':isselfselect})

        self.write({'success': 1, 'data':results})