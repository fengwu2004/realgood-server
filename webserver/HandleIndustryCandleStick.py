import json

from data.databasemgr import DatabaseMgr
from data.storemgr import StockMgr
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class HandleIndustryCandlestickRequest(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        data = json.loads(self.request.body.decode('utf-8'))

        industry = data['industry']

        items = StockMgr.instance().getIndustryStocks(industry)

        results = []

        for item in items:

            stock = StockMgr.instance().getStock(item['id'])

            if stock is None or stock.isNew():

                continue

            increase = stock.increaseTrend()

            lowvolatility = StockMgr.instance().checkIsLowVolatility(stock.id)

            isselfselect = StockMgr.instance().checkIsSelfSelect(item['id'])

            stockbasic = StockMgr.instance().getStockbasic(item['id'])

            if stockbasic is None:

                continue

            results.append({'stock':stock.toJson(), 'increase':increase, 'lowvolatility':lowvolatility, 'pe':stockbasic.pe, 'marketcap':stockbasic.outstanding, 'isselfselect':isselfselect})

        self.write({'success': 1, 'data':results})