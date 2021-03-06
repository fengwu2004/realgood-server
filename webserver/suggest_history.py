import json
from data.suggest_manager import SuggestMgr
from stockmgr.consultor_score_manager import ConsultorScoreManager
from webserver.RequestBaseManager import RequestBaseManager

class FindHistorySuggest(RequestBaseManager):
    
    def post (self, *args, **kwargs):
        
        if self.checkToken() is not True:
            
            self.write({'success': -1})
    
            return

        data = json.loads(self.request.body.decode('utf-8'))
        
        day = data['history']

        suggests = SuggestMgr.instance().getHistorySuggest(int(day))

        results = []

        for suggest in suggests:

            item = suggest.toJson()

            maxminincrease = SuggestMgr.instance().getMaxMinIncreaseInDays(suggest, int(day))

            item['high'] = maxminincrease[0]

            item['low'] = maxminincrease[1]

            results.append(item)

        self.write({'success': 1, 'data':results})