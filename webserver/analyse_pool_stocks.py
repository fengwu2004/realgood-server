import json

from data import storemgr, SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager
from stock.fill_pool import getPool

class FindPoolStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        pool = getPool()

        self.write({'success': 1, 'data': pool.getReuslt()})
