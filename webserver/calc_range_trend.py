# 计算区间涨跌幅度
import json

from data import suggest_manager
from stockmgr.consultor_manager import ConsultorManager
from webserver.RequestBaseManager import RequestBaseManager


class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        consultorName = data['name']

        consultorCompany = data['company']

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return

        consltor = ConsultorManager.instance().retriveConsultor(consultorName, consultorCompany)
        
        temps = suggest_manager.instance().findRangetrends(consltor)
    
        res = {'success': 1, 'data': temps}

        self.write(res)