from analyse import SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager

class HandleSuggestTrends(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})

        self.write({'success': 1, 'data': SuggestHistoryManager.instance().findTrends})
        
        return

        