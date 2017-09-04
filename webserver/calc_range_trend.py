# 计算区间涨跌幅度
import json
from webserver.RequestBaseManager import RequestBaseManager
from webserver.tokenManager import TokenManagerInstance
import storemgr

class CalcRangeTrend(RequestBaseManager):

    def post(self, *args, **kwargs):
        
        data = json.loads(self.request.body.decode('utf-8'))

        res = {'success': -1}
        
        if not TokenManagerInstance().checkToken(data['token']):
            
            self.write(res)
        
        results = storemgr.intance().findInfoIn('recommondtrends', {'consultor.name':data['consultor']})
        
        res = {'success': 1, 'data': results}
        
        self.write(res)