# 计算区间涨跌幅度
import json

from data.recommond_unit import ConsultorRecommondsTrends
from webserver.RequestBaseManager import RequestBaseManager
from webserver.tokenManager import TokenManagerInstance
import storemgr

class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        res = {'success': -1}
        
        if not TokenManagerInstance().checkToken(data['token']):

            self.write(res)
        
        temps = storemgr.intance().findInfoIn('recommondtrends', {'consultor.name':data['consultor']})

        result = None
        
        for temp in temps:
            
            result = temp
            
        res = {'success': 1, 'data': result}

        self.write(res)