from stockmgr.fill_pool import getPool
from webserver.RequestBaseManager import RequestBaseManager


class FindPoolStocks(RequestBaseManager):
    
    def post (self, *args, **kwargs):

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        pool = getPool()

        self.write({'success': 1, 'data': pool.getReuslt()})
