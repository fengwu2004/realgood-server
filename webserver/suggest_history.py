import json

from data import storemgr, SuggestHistoryManager
from webserver.RequestBaseManager import RequestBaseManager
from data.suggest import *

class FindHistorySuggest(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        items = SuggestHistoryManager.instance().getHistorySuggest(int(day))

        results = list(map(lambda suggest: suggest.toJson(), items))

        self.write({'success': 1, 'data':results})