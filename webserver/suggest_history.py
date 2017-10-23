import json

from data.suggest_manager import SuggestMgr
from webserver.RequestBaseManager import RequestBaseManager


class FindHistorySuggest(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        items = SuggestMgr.instance().getHistorySuggest(int(day))

        results = list(map(lambda suggest: suggest.toJson(), items))

        self.write({'success': 1, 'data':results})