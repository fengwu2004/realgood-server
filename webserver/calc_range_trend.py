# 计算区间涨跌幅度
import json

from webserver.RequestBaseManager import RequestBaseManager

from analyse import calc_interval_amplitude_of_consultor
from webserver.tokenManager import TokenManagerInstance

class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        res = {'success': -1}
        
        if not TokenManagerInstance().checkToken(data['token']):
            
            self.write(res)
        
        results = calc_interval_amplitude_of_consultor.doRun(data['consultor'])

        res = {'success': 1, 'data': results}
        
        self.write(res)