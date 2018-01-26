from data.storemgr import StockMgr
from stockmgr.pool import PoolA
from webserver.RequestBaseManager import RequestBaseManager


class FindPoolStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        StockMgr.instance().loadStocks()

        self.write({'success': 1})
        # PoolA.intance().doRunFrom('2017-4-30')

        # self.write({'success': 1, 'data': PoolA.intance().getReuslt()})
