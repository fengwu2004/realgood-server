# 计算区间涨跌幅度
import json

from data.suggest import Consultor
from stock.consultor_manager import ConsultorManager
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager
from data import storemgr
from data import SuggestHistoryManager

class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        consultorName = data['name']

        consultorCompany = data['company']

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        consltor = ConsultorManager.instance().retriveConsultor(consultorName, consultorCompany)
        
        temps = SuggestHistoryManager.instance().findRangetrends(consltor)
    
        res = {'success': 1, 'data': temps}

        self.write(res)