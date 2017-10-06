# 计算区间涨跌幅度
import json

from analyse import calc_interval_amplitude_of_consultor
from data.recommond_unit import ConsultorRecommondsTrends
from webserver import tokenManager
from webserver.RequestBaseManager import RequestBaseManager
from data import storemgr

class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))
        
        consultorName = data['name']

        consultorCompany = data['company']

        if not self.checkToken():
            
            self.write({'success': -1})
    
            return
        
        temps = calc_interval_amplitude_of_consultor.findRangetrends(consultorName, consultorCompany)
    
        res = {'success': 1, 'data': temps}

        self.write(res)